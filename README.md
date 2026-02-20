<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#161b22;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00aaff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#7c3aed;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="800" height="200" fill="url(#bg)" rx="12"/>
  <!-- Accent bar -->
  <rect x="0" y="0" width="800" height="4" fill="url(#accent)" rx="2"/>
  <!-- Shield icon -->
  <text x="60" y="120" font-size="70" text-anchor="middle" fill="url(#accent)" filter="url(#glow)">🛡️</text>
  <!-- Title -->
  <text x="420" y="85" font-family="monospace" font-size="36" font-weight="bold" fill="#ffffff" text-anchor="middle" filter="url(#glow)">A.R.T.E.M.I.S.S.</text>
  <!-- Subtitle -->
  <text x="420" y="118" font-family="monospace" font-size="13" fill="#8b949e" text-anchor="middle">Automated Review for Telegram Environments</text>
  <text x="420" y="137" font-family="monospace" font-size="13" fill="#8b949e" text-anchor="middle">Monitoring Inappropriate Submissions System</text>
  <!-- Tags -->
  <rect x="260" y="155" width="80" height="22" rx="11" fill="#00aaff" fill-opacity="0.2" stroke="#00aaff" stroke-width="1"/>
  <text x="300" y="170" font-family="monospace" font-size="11" fill="#00aaff" text-anchor="middle">Telegram</text>
  <rect x="352" y="155" width="60" height="22" rx="11" fill="#7c3aed" fill-opacity="0.2" stroke="#7c3aed" stroke-width="1"/>
  <text x="382" y="170" font-family="monospace" font-size="11" fill="#a78bfa" text-anchor="middle">AI/ML</text>
  <rect x="424" y="155" width="72" height="22" rx="11" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1"/>
  <text x="460" y="170" font-family="monospace" font-size="11" fill="#10b981" text-anchor="middle">Python 3.10+</text>
  <rect x="508" y="155" width="68" height="22" rx="11" fill="#f59e0b" fill-opacity="0.2" stroke="#f59e0b" stroke-width="1"/>
  <text x="542" y="170" font-family="monospace" font-size="11" fill="#f59e0b" text-anchor="middle">MIT License</text>
</svg>

</div>

---

**A.R.T.E.M.I.S.S.** is an AI-powered Telegram group moderation bot that automatically detects and removes NSFW (Not Safe For Work) images, videos, and GIFs using state-of-the-art machine-learning models. It tracks repeat offenders, notifies administrators, and auto-bans users who exceed a configurable violation threshold — all with zero manual review required.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖼️ **Image Moderation** | Scans every photo with [Falconsai/nsfw_image_detection](https://huggingface.co/Falconsai/nsfw_image_detection) |
| 🎬 **Video & GIF Moderation** | Samples key frames from videos and animations for NSFW analysis |
| ⚠️ **Violation Tracking** | Persists per-user violation counts across bot restarts (SQLite) |
| 🚫 **Auto-Ban** | Automatically bans users who reach the configurable threshold |
| 📣 **Admin Notifications** | Sends flagged media and alerts directly to all configured admins |
| 🗄️ **Evidence Caching** | Saves flagged images/videos to disk for admin review |
| 📊 **Real-Time Dashboard** | Flask + Socket.IO dashboard with live charts (Chart.js) |
| 🛡️ **Chat Owner Protection** | Gracefully skips banning if the offender is the chat owner |
| 🔧 **Environment-Variable Config** | All secrets and settings via `.env` — nothing hard-coded |

---

## 🏗️ Architecture

```
A.R.T.E.M.I.S.S/
├── artemis_bot.py      # Main Telegram bot (handlers, DB logic, ML inference)
├── dashboard.py        # Flask + Socket.IO admin dashboard (REST + WebSocket)
├── setup_db.py         # One-shot database initialisation script
├── templates/
│   └── index.html      # Dashboard UI (Tailwind CSS + Chart.js)
├── .env.example        # Environment variable template
├── requirements.txt    # Python dependencies
└── violations.db       # SQLite database (created at runtime)
```

### Data Flow

```
User sends media
      │
      ▼
artemis_bot.py receives update
      │
      ├─ Image → nsfw_detector pipeline (HuggingFace)
      │
      └─ Video/GIF → VideoContentAnalyzer
              │  samples N frames
              └─ each frame → ViT image classifier
                        │
                        ▼
                 NSFW? ──Yes──► delete message
                  │              add violation
                  │              notify admins
                  │              cache flagged media
                  │              ban if threshold reached
                  │
                 No ──────────► no action
                        │
                        ▼
               update SQLite (stats, actions, contents)
                        │
                        ▼
               dashboard.py reads DB via REST / Socket.IO
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- A Telegram **Bot Token** — create one with [@BotFather](https://t.me/BotFather)
- The bot must be added to your group as an **admin** with *Delete Messages* and *Ban Users* permissions

### 1 — Clone the Repository

```bash
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S
```

### 2 — Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### 4 — Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
BOT_TOKEN=1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ADMIN_IDS=123456789,987654321
FLAG_THRESHOLD=3
```

### 5 — Initialise the Database

```bash
python setup_db.py
```

### 6 — Run the Bot

```bash
python artemis_bot.py
```

### 7 — (Optional) Run the Dashboard

```bash
python dashboard.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## ⚙️ Configuration Reference

All configuration is done via environment variables (loaded from `.env`).

| Variable | Required | Default | Description |
|---|---|---|---|
| `BOT_TOKEN` | ✅ | — | Telegram bot token from @BotFather |
| `ADMIN_IDS` | ✅ | — | Comma-separated admin Telegram user IDs |
| `FLAG_THRESHOLD` | ❌ | `3` | Violations before auto-ban |
| `DB_FILE` | ❌ | `violations.db` | Path to the SQLite database |
| `FLAGGED_IMAGES_DIR` | ❌ | `flagged_images` | Directory for cached flagged images |
| `FLAGGED_VIDEOS_DIR` | ❌ | `flagged_videos` | Directory for cached flagged videos |
| `DASHBOARD_SECRET_KEY` | ❌ | random | Flask session secret key |

---

## 🤖 Bot Commands

| Command | Access | Description |
|---|---|---|
| `/start` | All | Welcome message and overview |
| `/help` | All | Full command reference |
| `/violations` | All | Check your own violation count |
| `/stats` | All | View aggregate bot statistics |
| `/admin_flagged` | Admin | List all users with active violations |
| `/admin_reset <user_id>` | Admin | Reset a user's violation count |
| `/admin_ban <user_id>` | Admin | Manually ban a user from the group |

---

## 📊 Dashboard

The optional Flask dashboard provides a real-time view of bot activity:

- **Status cards** — total scans, NSFW detected, SFW, bans, violations  
- **Action Trend** — line chart of moderation actions over time  
- **Content Breakdown** — SFW vs NSFW bar chart  
- **Actions Distribution** — doughnut chart by action type  
- **Analytics Comparison** — multi-line trend chart  
- **Recent Actions** — live-updating feed of all bot actions  

Data refreshes every 10 seconds via Socket.IO.

---

## 🗄️ Database Schema

```sql
-- Per-user violation counts
violations  (user_id INTEGER PK, count INTEGER)

-- Aggregate statistics
stats       (key TEXT PK, value INTEGER)

-- Full action audit log
actions     (id PK, user_id INTEGER, action TEXT, timestamp TEXT)

-- Every scanned content item
contents    (id PK, type TEXT, is_nsfw INTEGER)
```

---

## 🛠️ How It Works — Deep Dive

### Image Analysis

Every photo sent to a monitored group is downloaded to a temp file and passed through the HuggingFace `pipeline("image-classification", model="Falconsai/nsfw_image_detection")`. The model returns a label (`nsfw` / `normal`) and a confidence score.

### Video & GIF Analysis

Videos and animations are handled by `VideoContentAnalyzer`, which:

1. Opens the video with OpenCV (`cv2.VideoCapture`)
2. Samples `num_frames` (default 6) evenly-spaced frames
3. Converts each frame to a PIL image
4. Runs the same ViT classifier used for images
5. Stops early (`stop_on_nsfw=True`) as soon as NSFW content is found

### Violation Lifecycle

```
1st violation  → warning sent to user
2nd violation  → warning sent to user
3rd violation  → user banned from group (configurable via FLAG_THRESHOLD)
               → violation count reset
               → all admins notified with the flagged media
```

---

## 🔒 Security Notes

- **Never commit `.env`** — it is excluded by `.gitignore`
- The bot token and admin IDs are loaded exclusively from environment variables
- Flagged media directories are also excluded from git
- The Flask dashboard does not expose any write endpoints — it is read-only

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `python-telegram-bot` | Telegram Bot API client |
| `transformers` | HuggingFace model inference |
| `torch` | Deep learning backend |
| `Pillow` | Image handling |
| `opencv-python-headless` | Video frame extraction |
| `Flask` | Dashboard web server |
| `flask-socketio` | Real-time WebSocket updates |
| `python-dotenv` | `.env` file loading |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This bot relies on a machine-learning model and may produce false positives or false negatives. Always review flagged content before taking manual action, and use the tool responsibly in compliance with Telegram's Terms of Service.

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

<div align="center">
<strong>A.R.T.E.M.I.S.S.</strong> — Keeping your Telegram groups clean and safe 🛡️
</div>
