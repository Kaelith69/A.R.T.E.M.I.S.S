# Architecture

How A.R.T.E.M.I.S.S. is built, what each component does, and how they talk to each other.

---

## Overview

A.R.T.E.M.I.S.S. is a single-process Python application split across a few focused files. There's no microservices architecture, no message queues, no Kubernetes. It's a bot. It runs. It works. That's the goal.

```
Telegram API
    │
    │ (long-polling)
    ▼
artemis_bot.py  ──────── Falconsai ViT Model (PyTorch)
    │                      (CUDA or CPU inference)
    │
    ├──── SQLite DB (violations.db)
    │         └── violations / stats / actions / contents
    │
    ├──── File System
    │         ├── flagged_images/
    │         └── flagged_videos/
    │
    └──── Admin Telegram DMs (via Bot API)

dashboard.py ──── SQLite DB (same file, read-only queries)
    │
    └──── Browser (HTTP + Socket.IO)
```

---

## Components

### `artemis_bot.py` — The Brain

This is the main application. It runs an async event loop (via `python-telegram-bot`'s `ApplicationBuilder`) and registers handlers for every relevant Telegram event type.

**What it does:**
- Receives media events via Telegram long-polling
- Downloads media to a temp file
- Passes it to the ML model
- Makes moderation decisions
- Updates SQLite
- Notifies admins
- Cleans up temp files

**Key classes and functions:**

| Symbol | Type | Purpose |
|---|---|---|
| `VideoContentAnalyzer` | class | Wraps the ViT model for per-frame video analysis |
| `get_video_analyzer()` | function | Returns a module-level singleton of `VideoContentAnalyzer` |
| `nsfw_detector` | pipeline | Module-level HuggingFace pipeline for image classification |
| `handle_image()` | async handler | Processes photo messages |
| `handle_video()` | async handler | Processes video and GIF/animation messages |
| `add_violation()` | function | Increments user violation count; returns new count |
| `init_db()` | function | Creates all tables if they don't exist |

**Initialization order on startup:**
1. Load `.env`
2. Parse `ADMIN_IDS` and `BOT_TOKEN` from environment
3. Load Falconsai image pipeline (downloads model if needed)
4. Load `VideoContentAnalyzer` (singleton instantiated on first video)
5. `init_db()` — ensure schema exists
6. Register all command and message handlers
7. Start long-polling

---

### Falconsai ViT Model — The Starer of Pixels

The ML model is `Falconsai/nsfw_image_detection`, a Vision Transformer fine-tuned for binary classification: `nsfw` vs `normal`.

**Image path:**
```
temp file → HuggingFace pipeline() → [{"label": "nsfw", "score": 0.97}]
```

**Video path:**
```
video file → OpenCV frame extraction (6 frames)
           → each frame → PIL Image → ViTImageProcessor → model
           → torch.softmax → argmax → label + confidence
           → if nsfw AND confidence ≥ 0.5 → stop early
```

The `stop_on_nsfw=True` flag means the video analyzer bails out as soon as it finds a NSFW frame. No point analyzing 5 more frames once the verdict is in — saves compute and time.

Model inference runs on:
- `cuda:0` if a CUDA GPU is detected (`torch.cuda.is_available()`)
- `cpu` otherwise

The model is a **module-level singleton** — it loads once when the bot starts, then every incoming message reuses the same model instance. Avoids reloading 350MB into memory for every cat video.

---

### `dashboard.py` — The Dashboard

A Flask web application that provides a real-time view into what the bot is doing.

**Endpoints:**

| Route | Method | Returns |
|---|---|---|
| `/` | GET | Renders `templates/index.html` |
| `/api/stats` | GET | JSON: key/value stats from `stats` table |
| `/api/actions` | GET | JSON: all rows from `actions` table, newest first |
| `/api/all_data` | GET | JSON: combined stats + violations + actions + content_types |

**Socket.IO:**
- On `connect`: emits `initial_data` with current DB state
- Background thread: every 10 seconds, emits `update_data` to all connected clients

The dashboard and the bot share the same `violations.db` file. The dashboard only reads — it never writes to the database.

> ⚠️ The dashboard has no authentication in v0.1. Bind it to localhost and use a reverse proxy if you need to expose it beyond your local machine.

---

### `setup_db.py` — Database Init

A standalone script that creates all four tables and inserts the initial zero-values for stats counters. It's idempotent — safe to run multiple times (`CREATE TABLE IF NOT EXISTS`, `INSERT OR IGNORE`).

Run it once before the first bot start, or let `init_db()` inside `artemis_bot.py` handle it automatically on startup.

---

### `templates/index.html` — Dashboard UI

A single-page HTML application using:
- **Tailwind CSS** (CDN) for styling — dark theme by default
- **Chart.js** (CDN) for data visualizations
- **Socket.IO client** (CDN) for live updates
- **html2pdf** (CDN) for PDF export support

The page connects to the Socket.IO server on load, receives `initial_data`, then updates live whenever `update_data` events arrive.

---

## Database Schema

```sql
-- Per-user violation counts
CREATE TABLE violations (
    user_id INTEGER PRIMARY KEY,
    count   INTEGER
);

-- Aggregate counters
CREATE TABLE stats (
    key   TEXT PRIMARY KEY,
    value INTEGER
);

-- Moderation action audit log
CREATE TABLE actions (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id   INTEGER,
    action    TEXT,          -- e.g. "content_removed", "user_banned"
    timestamp TEXT           -- "YYYY-MM-DD HH:MM:SS"
);

-- Scanned content log (type + NSFW flag)
CREATE TABLE contents (
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    type    TEXT,             -- "image" or "video"
    is_nsfw INTEGER           -- 0 or 1
);
```

**Stats keys:**

| Key | Meaning |
|---|---|
| `total_contents_scanned` | Total items processed |
| `total_nsfw_detected` | Total NSFW items found |
| `total_sfw` | Total clean items |
| `total_users_banned` | Total auto-ban events |
| `total_violations` | Total violation increments |

---

## Configuration

All runtime configuration lives in environment variables (loaded from `.env` via `python-dotenv`):

| Variable | Default | Purpose |
|---|---|---|
| `BOT_TOKEN` | — | Telegram Bot API token (required) |
| `ADMIN_IDS` | — | Comma-separated admin user IDs (required) |
| `FLAG_THRESHOLD` | `3` | Violations before ban |
| `DB_FILE` | `violations.db` | SQLite file path |
| `FLAGGED_IMAGES_DIR` | `flagged_images` | Where to cache flagged images |
| `FLAGGED_VIDEOS_DIR` | `flagged_videos` | Where to cache flagged videos |
| `DASHBOARD_SECRET_KEY` | auto-generated | Flask session secret |

---

## Moderation Decision Logic

```
Media received
    ↓
Download to temp file
    ↓
Run model → label, confidence
    ↓
label == "nsfw"?
    │
   YES → delete message
       → increment violation count → check threshold
       → threshold reached? → ban user (group only)
       → notify each admin (DM + media)
       → cache media in flagged_*/ dir
    │
    NO → delete temp file → done
```

The `VideoContentAnalyzer.analyze_video()` method returns a `dict` with:
- `frames_analyzed`: how many frames were processed
- `nsfw_detected`: boolean
- `frame_results`: list of per-frame results
- `first_nsfw_frame`: the first frame that triggered NSFW, or `None`
