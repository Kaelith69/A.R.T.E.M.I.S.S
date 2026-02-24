# Changelog

All notable changes to A.R.T.E.M.I.S.S. are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

Things that are cooking. Don't hold your breath, but do check back.

- Text spam detection (NLP classifier)
- Configurable ban escalation (mute before ban)
- Dashboard authentication
- Multi-group per-group configuration
- Docker Compose deployment

---

## [0.1.0] — 2025-02-27

### The "It Works, Ship It" Release

This is where A.R.T.E.M.I.S.S. became a real thing instead of a folder of unfinished scripts.

### Added

- **Core Telegram bot** (`artemis_bot.py`) with `python-telegram-bot ≥ 21.0`
  - Long-polling event loop with async handlers
  - Photo handler: downloads image, runs Falconsai ViT pipeline, acts on result
  - Video handler: downloads video, samples 6 frames via OpenCV, stops on first NSFW hit
  - GIF/Animation handler: same pipeline as video
  - Text handler: stubbed out (does nothing — the bouncer hasn't read a book yet)
- **NSFW detection engine**
  - Image pipeline: `Falconsai/nsfw_image_detection` via HuggingFace `pipeline()`
  - Video analyzer: `VideoContentAnalyzer` class with `AutoModelForImageClassification` + `ViTImageProcessor`
  - GPU auto-detection: uses CUDA if available, falls back to CPU
  - Module-level singleton for video analyzer — loads once, reuses forever
- **Violation system**
  - SQLite-backed per-user violation counts
  - Configurable threshold via `FLAG_THRESHOLD` env var (default: 3)
  - Auto-ban on threshold breach (group/supergroup only; private chat banning is politely declined)
  - Admin override via `/admin_ban`, `/admin_reset`
  - Chat owner cannot be banned — `Can't remove chat owner` is caught and handled gracefully
- **Admin notifications**
  - Every configured admin receives a DM alert when NSFW is detected
  - Cached flagged media (image or video) is forwarded to each admin
- **Media caching**
  - Flagged images saved to `flagged_images/` with `user_<id>_<timestamp>.jpg` naming
  - Flagged videos/GIFs saved to `flagged_videos/` with appropriate extension
  - SFW temp files deleted immediately after scan
- **Bot commands**
  - `/start` — welcome message
  - `/help` — command reference
  - `/violations` — user's own violation count
  - `/stats` — aggregate bot statistics
  - `/admin_flagged` — list all users with violations (admin only)
  - `/admin_reset <user_id>` — reset a user's count (admin only)
  - `/admin_ban <user_id>` — manually ban a user (admin only)
- **SQLite database** (`violations.db`)
  - `violations` table: user_id, count
  - `stats` table: key/value counters (total scanned, NSFW detected, SFW, banned, violations)
  - `actions` table: timestamped audit log of moderation actions
  - `contents` table: type and NSFW flag for each scanned item
- **Database init script** (`setup_db.py`) — idempotent, safe to re-run
- **Admin dashboard** (`dashboard.py`)
  - Flask + Socket.IO web application
  - REST API endpoints: `/api/stats`, `/api/actions`, `/api/all_data`
  - Real-time Socket.IO push every 10 seconds via background thread
  - Tailwind CSS dark theme UI (`templates/index.html`)
  - Chart.js for visualizations
  - html2pdf export support
- **Configuration** via `.env` file
  - `BOT_TOKEN`, `ADMIN_IDS`, `FLAG_THRESHOLD`, `DB_FILE`, `FLAGGED_IMAGES_DIR`, `FLAGGED_VIDEOS_DIR`, `DASHBOARD_SECRET_KEY`
  - `.env.example` provided

### Changed

- Nothing yet. This is v0.1. Everything was added, nothing was changed.

### Removed

- Also nothing. This is the beginning.

### Fixed

- `BadRequest: Message to be replied not found` — caught explicitly so it doesn't crash the bot when a message is deleted before the bot can reply to it

---

## [0.0.1] — 2025-02-21

### The "Does It Even Connect?" Phase

Initial scaffolding. Bot connected. Model loaded. Nothing crashed immediately.
Mostly used to verify that `python-telegram-bot` and `transformers` could coexist in a venv without catastrophe.

*(Not formally tagged — treated as pre-release development.)*

---

[Unreleased]: https://github.com/Kaelith69/A.R.T.E.M.I.S.S/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Kaelith69/A.R.T.E.M.I.S.S/releases/tag/v0.1.0
