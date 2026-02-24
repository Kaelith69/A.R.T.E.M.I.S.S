<div align="center">

# 🛡️ A.R.T.E.M.I.S.S. Wiki

**Automated Review for Telegram Environments: Monitoring Inappropriate Submissions System**

*AI-powered NSFW content moderation for Telegram groups — because group admins deserve to sleep*

</div>

---

## Welcome

This is the complete technical and operational reference for **A.R.T.E.M.I.S.S.** — an open-source, AI-powered Telegram group moderation bot.

Whether you're an operator deploying the bot, a developer extending its capabilities, or a contributor fixing a bug at 2 AM while questioning your life choices, this wiki has what you need.

---

## Quick Navigation

| Page | What's in it |
|---|---|
| [Architecture](Architecture.md) | How the system is built — modules, data flow, component design |
| [Installation](Installation.md) | Step-by-step setup for all platforms |
| [Usage](Usage.md) | Running the bot, admin commands, dashboard |
| [Privacy](Privacy.md) | What data is stored, how long, and how to purge it |
| [Troubleshooting](Troubleshooting.md) | Common errors and how to fix them |
| [Roadmap](Roadmap.md) | What's coming next |

---

## What is A.R.T.E.M.I.S.S.?

A.R.T.E.M.I.S.S. is a **server-side Python application** that connects to Telegram's Bot API via long-polling. It sits in your Telegram group and watches every image, video, and GIF that gets sent. Each piece of media is run through a Vision Transformer (ViT) machine-learning model — `Falconsai/nsfw_image_detection` on HuggingFace — to classify whether content is SFW or NSFW.

The OCR-free, pixel-staring brain of the operation is the ViT model. It classifies images by looking at the entire image as a sequence of patches — like reading a book one paragraph at a time, except the book is a JPEG and it's asking "should this be deleted?"

### When NSFW content is detected:

1. 🗑️ The offending message is **deleted** from the group immediately
2. ⚠️ The user receives a **warning** with their current violation count
3. 📊 The violation count is **incremented** in SQLite
4. 👮 Configured **admin Telegram IDs** receive a DM alert + the cached flagged media
5. 🔨 If the user hits `FLAG_THRESHOLD` (default: 3), they are **automatically banned**

A companion **Flask + Socket.IO web dashboard** provides real-time statistics and an audit log of all moderation actions.

---

## At a Glance

| Property | Value |
|---|---|
| **Language** | Python 3.10+ |
| **Bot Framework** | python-telegram-bot ≥ 21.0 |
| **ML Model** | Falconsai/nsfw_image_detection (ViT-based) |
| **Inference Backend** | PyTorch (CUDA or CPU) |
| **Database** | SQLite (local file) |
| **Dashboard** | Flask + Socket.IO + Chart.js |
| **License** | MIT |
| **Default violation threshold** | 3 |
| **Video frame sampling** | 6 frames per video |
| **Confidence threshold** | 0.5 (50%) |

---

## Repository Structure

```
A.R.T.E.M.I.S.S/
├── artemis_bot.py       # Core bot logic — all handlers and violation engine
├── dashboard.py         # Admin analytics dashboard
├── setup_db.py          # Database initialisation script (run once)
├── templates/
│   └── index.html       # Dashboard web UI
├── wiki/                # This documentation
├── assets/              # Demo GIFs and static files
├── .env.example         # Configuration template
├── requirements.txt     # Python dependencies
├── blueprint.md         # Original development blueprint
└── LICENSE
```

---

## Getting Started in 60 Seconds

```bash
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # edit BOT_TOKEN and ADMIN_IDS
python setup_db.py
python artemis_bot.py
```

See [Installation](Installation.md) for the full guide including Windows instructions.

---

## Contributing

See the [CONTRIBUTING.md](../CONTRIBUTING.md) in the repo root for development setup, commit conventions, and PR process.
