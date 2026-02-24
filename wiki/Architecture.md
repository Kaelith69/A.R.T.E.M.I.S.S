# Architecture

This page provides a deep technical explanation of the A.R.T.E.M.I.S.S. system architecture, module design, and internal component interactions.

---

## Table of Contents

- [High-Level Overview](#high-level-overview)
- [Process Model](#process-model)
- [Module Breakdown](#module-breakdown)
  - [artemis_bot.py](#artemis_botpy)
  - [dashboard.py](#dashboardpy)
  - [setup_db.py](#setup_dbpy)
  - [templates/index.html](#templatesindexhtml)
- [ML Inference Layer](#ml-inference-layer)
- [Database Layer](#database-layer)
- [Data Flow — Detailed](#data-flow--detailed)
- [Configuration System](#configuration-system)
- [Error Handling Strategy](#error-handling-strategy)
- [Extension Points](#extension-points)

---

## High-Level Overview

A.R.T.E.M.I.S.S. is composed of two independent processes that share a single SQLite database file:

```
┌─────────────────────────────────────────────────────────┐
│  Process 1: artemis_bot.py                               │
│  ─────────────────────────────────────────────────────── │
│  Telegram Long-Poll → Message Handlers → ML Inference    │
│  → Action Decider → DB writes → Admin Notifications      │
└──────────────────────────┬──────────────────────────────┘
                           │ shared violations.db
┌──────────────────────────▼──────────────────────────────┐
│  Process 2: dashboard.py                                 │
│  ─────────────────────────────────────────────────────── │
│  Flask HTTP → REST API → SQLite reads → Socket.IO push   │
│  → Browser (Chart.js real-time charts)                   │
└─────────────────────────────────────────────────────────┘
```

The two processes are **fully decoupled** — the bot does not depend on the dashboard being running, and the dashboard is purely read-only.

---

## Process Model

| Process | Entry Point | Role | Communication |
|---|---|---|---|
| **Bot** | `artemis_bot.py` | Content moderation enforcement | Telegram Bot API (long-poll) |
| **Dashboard** | `dashboard.py` | Analytics and audit display | HTTP REST + Socket.IO WebSocket |

Both processes are started independently. In production, they would typically run as separate systemd services or Docker containers.

---

## Module Breakdown

### artemis_bot.py

The core bot file. It is structured into four logical sections:

#### 1. Configuration & Initialization (lines 1–82)

```python
load_dotenv()                           # Load .env file
ADMIN_IDS: set[int] = {…}              # Parse comma-separated admin IDs
BOT_TOKEN = os.environ.get("BOT_TOKEN") # Telegram token
_device = 0 if torch.cuda.is_available() else -1  # GPU detection
nsfw_detector = pipeline(               # Load image classifier once
    "image-classification",
    model="Falconsai/nsfw_image_detection",
    device=_device,
)
```

The NSFW image pipeline is loaded **once at module level** as a module singleton. This is a deliberate design choice — loading the ViT model on every request would be prohibitively slow (~3–10 seconds per load).

#### 2. VideoContentAnalyzer Class (lines 88–179)

```python
class VideoContentAnalyzer:
    def __init__(self, model_name):
        self.model = AutoModelForImageClassification.from_pretrained(model_name)
        self.processor = ViTImageProcessor.from_pretrained(model_name)

    def analyze_frame(self, image: Image) -> Tuple[str, float]:
        # Single-frame ViT inference

    def analyze_video(self, video_path, num_frames=6, stop_on_nsfw=True, nsfw_threshold=0.5) -> dict:
        # OpenCV frame extraction + multi-frame inference
```

A module-level singleton (`_video_analyzer`) is lazily instantiated via `get_video_analyzer()` on the first video message received. This avoids loading the model if no videos are ever sent.

**Key design decisions:**
- `num_frames=6`: Balances detection coverage against inference latency.
- `stop_on_nsfw=True`: Early exit optimization — stops sampling after first NSFW frame.
- Frame positions are calculated as `min(i * interval, total_frames - 1)` to avoid out-of-bounds reads.

#### 3. Database Functions (lines 183–308)

All database operations are implemented as standalone functions using direct `sqlite3` connections (no ORM):

| Function | Description |
|---|---|
| `init_db()` | Creates all tables with `CREATE TABLE IF NOT EXISTS` |
| `get_violation_count(user_id)` | Reads current violation count for a user |
| `add_violation(user_id)` | Atomically increments via `INSERT OR REPLACE` |
| `reset_violation(user_id)` | Deletes the user's row |
| `get_all_violations()` | Returns all users with count > 0 |
| `log_action(user_id, action)` | Appends to audit log with timestamp |
| `increment_stat(key)` | Thread-safe counter increment via `INSERT OR IGNORE` + `UPDATE` |
| `get_stat(key)` | Reads a single stat counter |
| `get_all_stats()` | Returns all stats as a dict |
| `log_content(type, is_nsfw)` | Records each scan result in contents table |

Each function opens and closes its own connection. This is appropriate for a single-process bot with moderate traffic; for high-volume deployments, a connection pool would be preferable.

#### 4. Bot Command & Message Handlers (lines 313–655)

| Handler | Trigger | Logic |
|---|---|---|
| `start` | `/start` command | Welcome message |
| `help_command` | `/help` command | HTML-formatted command list |
| `violations` | `/violations` command | Queries DB for user's count |
| `admin_flagged` | `/admin_flagged` command | Lists all flagged users (admin-gated) |
| `admin_reset` | `/admin_reset <id>` command | Resets a user's violation count (admin-gated) |
| `admin_ban` | `/admin_ban <id>` command | Issues `ban_chat_member` API call (admin-gated) |
| `stats` | `/stats` command | Returns all stat counters |
| `handle_image` | `filters.PHOTO` | Full image moderation pipeline |
| `handle_video` | `filters.VIDEO \| filters.ANIMATION` | Full video/GIF moderation pipeline |
| `handle_text` | `filters.TEXT` | No-op placeholder (for future spam detection) |
| `error_handler` | All errors | Logs errors, sends user-facing error message |

**Admin gate pattern:**
```python
if user.id not in ADMIN_IDS:
    await update.message.reply_text("❌ You are not authorized.")
    return
```

**Image moderation pipeline** (`handle_image`):
```
download temp file → run nsfw_detector → check label →
  if NSFW: delete message, add_violation, notify admins, cache file, maybe ban
  if SFW: remove temp file
in all cases: increment stats, log_content
```

**Video moderation pipeline** (`handle_video`):
```
determine media type (video or animation) → download temp file →
get_video_analyzer() → analyze_video() →
  if NSFW: delete, add_violation, cache, notify admins, maybe ban
  if SFW: remove temp file
in all cases: increment stats, log_content
```

---

### dashboard.py

A lightweight Flask application providing a read-only view of the SQLite database.

#### Routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Renders `templates/index.html` |
| `/api/stats` | GET | Returns `{key: value}` stats dict |
| `/api/actions` | GET | Returns all actions ordered by timestamp desc |
| `/api/all_data` | GET | Returns stats + actions + violations + content_types |

#### Socket.IO

| Event | Direction | Description |
|---|---|---|
| `connect` | Client → Server | Triggers `emit('initial_data', …)` |
| `initial_data` | Server → Client | Full dataset on connect |
| `update_data` | Server → Client | Periodic push every 10 seconds |

The background thread runs `socketio.emit('update_data', get_initial_data())` every 10 seconds, which pushes fresh DB reads to all connected clients simultaneously.

---

### setup_db.py

A one-shot script that creates all four SQLite tables and seeds initial stat counters. Idempotent — safe to run multiple times due to `CREATE TABLE IF NOT EXISTS` and `INSERT OR IGNORE`.

---

### templates/index.html

A single-page application (SPA) served by Flask. Technologies used:

- **Tailwind CSS 2.2.19** — responsive dark-mode UI
- **Chart.js 3.7.1** — 5 chart types: line, bar, doughnut, horizontal bar, multi-line
- **chartjs-plugin-zoom 1.2.1** — scroll zoom and pan on the Action Trend chart
- **Socket.IO 4.4.1** — real-time data push
- **html2pdf.js 0.10.1** — client-side PDF export capability

Chart instances are stored in module-level variables and updated in-place (`.data.labels`, `.data.datasets[0].data`, `.update()`) to avoid recreation on every push — preserving zoom state and render performance.

---

## ML Inference Layer

### Model: Falconsai/nsfw_image_detection

- **Architecture:** Vision Transformer (ViT-base-patch16-224)
- **Task:** Binary image classification (`nsfw` / `normal`)
- **Input:** RGB images, resized to 224×224 by `ViTImageProcessor`
- **Output:** Softmax probabilities over two classes
- **Source:** [huggingface.co/Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection)

### Two access patterns

| Pattern | Used for | API |
|---|---|---|
| `pipeline("image-classification")` | Still images | `nsfw_detector(file_path)` |
| `AutoModelForImageClassification` + `ViTImageProcessor` | Video frames | `VideoContentAnalyzer.analyze_frame(pil_image)` |

Both patterns use the **same underlying model weights** — the difference is only in how inputs are fed. The pipeline pattern is more convenient for single images; the direct model + processor pattern gives finer control for batch frame processing.

### GPU Acceleration

```python
_device = 0 if torch.cuda.is_available() else -1  # for pipeline
self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # for VideoContentAnalyzer
```

When a CUDA GPU is available, inference is 10–20× faster, which is significant for high-traffic groups.

---

## Database Layer

### Schema

```sql
CREATE TABLE violations (
    user_id INTEGER PRIMARY KEY,
    count   INTEGER
);

CREATE TABLE stats (
    key   TEXT PRIMARY KEY,
    value INTEGER
);

CREATE TABLE actions (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id   INTEGER,
    action    TEXT,
    timestamp TEXT
);

CREATE TABLE contents (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    type    TEXT,
    is_nsfw INTEGER
);
```

### Stat Keys

| Key | Incremented when |
|---|---|
| `total_contents_scanned` | Any image or video is processed |
| `total_nsfw_detected` | Content is classified NSFW |
| `total_sfw` | Content is classified SFW |
| `total_users_banned` | A user is auto-banned |
| `total_violations` | Any violation is added |

---

## Data Flow — Detailed

```
Telegram Update (photo/video/animation)
         │
         ▼
python-telegram-bot ApplicationBuilder
         │  dispatches to correct handler
         ▼
handle_image() or handle_video()
         │
         ├─ Download media to temp file (temp_{user_id}.jpg/.mp4/.gif)
         │
         ├─ [Image] nsfw_detector(temp_path)
         │    └─ HuggingFace pipeline → ViT inference → (label, score)
         │
         └─ [Video/GIF] get_video_analyzer().analyze_video(temp_path)
              ├─ cv2.VideoCapture → frame extraction
              ├─ PIL.Image.fromarray() → RGB conversion
              └─ analyze_frame() → ViT inference → (label, confidence)
                        │
                        ▼
              results dict: {nsfw_detected, frames_analyzed, frame_results, …}
         │
         ├─ increment_stat("total_contents_scanned")
         ├─ log_content(type, is_nsfw)
         │
         ├─ [NSFW path]
         │   ├─ increment_stat("total_nsfw_detected")
         │   ├─ violation_count = add_violation(user_id)
         │   ├─ update.message.delete()
         │   ├─ log_action(user_id, "content_removed")
         │   ├─ send warning to group chat
         │   ├─ os.rename(temp_path, cached_path)  ← preserve evidence
         │   ├─ for admin in ADMIN_IDS: send_message() + send_photo/video()
         │   └─ if violation_count >= FLAG_THRESHOLD:
         │       ├─ ban_chat_member(chat_id, user_id)
         │       ├─ log_action(user_id, "user_banned")
         │       ├─ increment_stat("total_users_banned")
         │       └─ reset_violation(user_id)
         │
         └─ [SFW path]
             ├─ increment_stat("total_sfw")
             └─ os.remove(temp_path)
```

---

## Configuration System

All runtime configuration flows through environment variables loaded by `python-dotenv`:

```
.env file
   └─ load_dotenv()
         ├─ BOT_TOKEN        → direct string
         ├─ ADMIN_IDS        → parsed into set[int]
         ├─ FLAG_THRESHOLD   → int()
         ├─ DB_FILE          → string path
         ├─ FLAGGED_IMAGES_DIR → os.makedirs() on startup
         ├─ FLAGGED_VIDEOS_DIR → os.makedirs() on startup
         └─ DASHBOARD_SECRET_KEY → Flask app.config
```

Missing required variables (`BOT_TOKEN`) cause an immediate `RuntimeError` at startup. Missing optional variables silently use defaults.

---

## Error Handling Strategy

| Error type | Handling |
|---|---|
| Model load failure | `logger.error()` + `raise` — bot refuses to start with broken model |
| Telegram API errors | `telegram.error.BadRequest` caught and logged per handler |
| Chat owner ban attempt | Graceful catch — warning sent instead of crash |
| Missing message (already deleted) | `"Message to be replied not found"` caught and logged |
| Video file not found | `FileNotFoundError` raised by `analyze_video` — caught by outer try/except |
| General exceptions | `error_handler` sends user-facing error message |
| Empty ADMIN_IDS | `warnings.warn()` — bot starts but admins won't receive alerts |

---

## Extension Points

| Extension | Where to modify |
|---|---|
| Add a new detection model | Replace or augment `nsfw_detector` in the initialization section |
| Add text spam detection | Implement in `handle_text()` (currently a no-op) |
| Add per-group configuration | Extend the `violations` table with a `chat_id` column |
| Switch to PostgreSQL | Replace `sqlite3` calls with `psycopg2` or SQLAlchemy |
| Add webhook mode | Replace `run_polling()` with `run_webhook()` in `main()` |
| Add more admin commands | Register new `CommandHandler` in `main()` with admin gate |
| Add dashboard authentication | Add Flask-Login or HTTP Basic Auth to `dashboard.py` |
