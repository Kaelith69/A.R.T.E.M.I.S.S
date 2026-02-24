<div align="center">

# 🛡️ A.R.T.E.M.I.S.S. Wiki

**Automated Review for Telegram Environments: Monitoring Inappropriate Submissions System**

*AI-powered NSFW content moderation for Telegram groups*

</div>

---

## Welcome

This wiki is the complete technical and operational reference for **A.R.T.E.M.I.S.S.** — an open-source, AI-powered Telegram group moderation bot. Whether you are an operator deploying the bot, a developer extending its capabilities, or a contributor fixing a bug, this wiki has everything you need.

---

## Quick Navigation

| Page | Description |
|---|---|
| [Architecture](Architecture.md) | System design, module breakdown, internal component design |
| [Installation](Installation.md) | Step-by-step setup guide for all platforms |
| [Usage](Usage.md) | Operating the bot, admin commands, dashboard guide |
| [Privacy](Privacy.md) | Data model, retention policies, security posture |
| [Contributing](Contributing.md) | Developer onboarding, code style, PR process |
| [Troubleshooting](Troubleshooting.md) | Debugging guide for common errors |
| [Roadmap](Roadmap.md) | Planned features and versioning strategy |

---

## What is A.R.T.E.M.I.S.S.?

A.R.T.E.M.I.S.S. is a **server-side Python application** that connects to Telegram's Bot API via long-polling. It intercepts every image, video, and GIF sent to configured groups and runs them through a Vision Transformer (ViT) machine-learning model — `Falconsai/nsfw_image_detection` on HuggingFace — to classify whether content is safe (SFW) or not safe for work (NSFW).

When NSFW content is detected:

1. The offending message is **deleted** from the group immediately.
2. The user's **violation count** is incremented in SQLite.
3. Configured **admin Telegram IDs** receive an alert message and the cached flagged media.
4. If the user's violation count reaches `FLAG_THRESHOLD` (default: 3), they are **automatically banned** from the group.

A companion **Flask + Socket.IO web dashboard** provides administrators with real-time statistics and an audit log of all moderation actions.

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
├── artemis_bot.py       # Core bot logic
├── dashboard.py         # Admin analytics dashboard
├── setup_db.py          # Database initialisation script
├── templates/
│   └── index.html       # Dashboard web UI
├── wiki/                # This documentation
├── .env.example         # Configuration template
├── requirements.txt     # Python dependencies
├── blueprint.md         # Original development blueprint
└── LICENSE
```

---

## Getting Started Fast

```bash
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # edit BOT_TOKEN and ADMIN_IDS
python setup_db.py
python artemis_bot.py
```

See [Installation](Installation.md) for the full guide.

---

## Contributing

See [Contributing](Contributing.md) for how to set up a development environment, coding conventions, and the pull request process.
