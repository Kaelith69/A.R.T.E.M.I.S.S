# Installation

Complete installation guide for A.R.T.E.M.I.S.S. covering all supported platforms.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Platform-Specific Instructions](#platform-specific-instructions)
  - [Linux / macOS](#linux--macos)
  - [Windows](#windows)
- [GPU Setup (Optional)](#gpu-setup-optional)
- [Configuration](#configuration)
- [Database Initialisation](#database-initialisation)
- [Running the Bot](#running-the-bot)
- [Running the Dashboard](#running-the-dashboard)
- [Running as a Service (Linux)](#running-as-a-service-linux)
- [Verifying the Installation](#verifying-the-installation)
- [Uninstalling](#uninstalling)

---

## Prerequisites

| Requirement | Minimum Version | Notes |
|---|---|---|
| Python | 3.10 | Required for `set[int]` and `X \| Y` union type syntax |
| pip | 23.0+ | Comes with Python; upgrade with `pip install --upgrade pip` |
| Telegram Bot Token | — | Create with [@BotFather](https://t.me/BotFather) |
| Admin user IDs | — | Your Telegram numeric user ID (use [@userinfobot](https://t.me/userinfobot)) |
| Group admin permissions | — | Bot needs *Delete Messages* + *Ban Users* |
| Disk space | ~2 GB | For the ViT model weights (downloaded once) |
| RAM | 2 GB minimum | 4 GB recommended for smooth CPU inference |

---

## Platform-Specific Instructions

### Linux / macOS

```bash
# 1. Clone the repository
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up configuration
cp .env.example .env
# Edit .env with your values (see Configuration section below)

# 6. Initialise the database
python setup_db.py

# 7. Run the bot
python artemis_bot.py
```

### Windows

```powershell
# 1. Clone the repository
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Upgrade pip
pip install --upgrade pip

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up configuration
copy .env.example .env
# Edit .env with Notepad or VS Code

# 6. Initialise the database
python setup_db.py

# 7. Run the bot
python artemis_bot.py
```

> **Windows note:** If `opencv-python-headless` fails to install, try `opencv-python` as a fallback (adds GUI dependencies but works on Windows).

---

## GPU Setup (Optional)

By default, the bot uses CPU inference. To enable GPU acceleration with CUDA:

```bash
# Deactivate current venv if active
deactivate

# Recreate venv (optional but clean)
python3 -m venv venv
source venv/bin/activate

# Install PyTorch with CUDA 12.1 support
pip install torch --index-url https://download.pytorch.org/whl/cu121

# Then install remaining requirements
pip install -r requirements.txt
```

Visit [pytorch.org/get-started](https://pytorch.org/get-started/locally/) to choose the correct CUDA version for your GPU driver.

The bot automatically detects CUDA at runtime:
```python
_device = 0 if torch.cuda.is_available() else -1
```

No configuration change is needed — GPU is used automatically when available.

---

## Configuration

Copy the example file and fill in your values:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# ── REQUIRED ────────────────────────────────────────────
# Your Telegram bot token from @BotFather
BOT_TOKEN=1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Comma-separated Telegram user IDs of administrators
# Find your ID via @userinfobot on Telegram
ADMIN_IDS=123456789,987654321

# ── OPTIONAL ────────────────────────────────────────────
# Number of violations before a user is auto-banned (default: 3)
FLAG_THRESHOLD=3

# Path to the SQLite database file (default: violations.db)
DB_FILE=violations.db

# Directories for caching flagged media (created automatically)
FLAGGED_IMAGES_DIR=flagged_images
FLAGGED_VIDEOS_DIR=flagged_videos

# Flask dashboard secret key (auto-generated if omitted)
DASHBOARD_SECRET_KEY=change_me_to_a_long_random_string
```

### Getting Your Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a name and username for your bot
4. Copy the token that BotFather provides

### Getting Your Admin Telegram User ID

1. Open Telegram and search for [@userinfobot](https://t.me/userinfobot)
2. Start a conversation — it will reply with your numeric user ID
3. Add that number to `ADMIN_IDS`

---

## Database Initialisation

```bash
python setup_db.py
```

Expected output:
```
Database 'violations.db' initialised successfully.
```

This creates the `violations.db` file with all four tables and seeds the initial stat counters. The script is **idempotent** — running it multiple times is safe and will not delete existing data.

---

## Running the Bot

```bash
python artemis_bot.py
```

On first run, the HuggingFace model weights (~330 MB) are downloaded and cached in `~/.cache/huggingface/`. Subsequent starts are fast.

Expected startup output:
```
INFO - Loading model Falconsai/nsfw_image_detection...
INFO - VideoContentAnalyzer initialized using model: Falconsai/nsfw_image_detection
INFO - 🚀 Bot is starting...
INFO - Application started
```

The bot will now monitor any Telegram groups it has been added to as admin.

---

## Running the Dashboard

In a separate terminal (with the same virtual environment activated):

```bash
python dashboard.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

> **Note:** The dashboard and bot share the same `violations.db` file. Both can run simultaneously without conflict.

---

## Running as a Service (Linux)

For production deployments, run the bot as a `systemd` service so it restarts automatically on failure and survives reboots.

### Bot service: `/etc/systemd/system/artemis-bot.service`

```ini
[Unit]
Description=A.R.T.E.M.I.S.S. Telegram Bot
After=network.target

[Service]
Type=simple
User=YOUR_LINUX_USERNAME
WorkingDirectory=/path/to/A.R.T.E.M.I.S.S
EnvironmentFile=/path/to/A.R.T.E.M.I.S.S/.env
ExecStart=/path/to/A.R.T.E.M.I.S.S/venv/bin/python artemis_bot.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

### Dashboard service: `/etc/systemd/system/artemis-dashboard.service`

```ini
[Unit]
Description=A.R.T.E.M.I.S.S. Dashboard
After=network.target

[Service]
Type=simple
User=YOUR_LINUX_USERNAME
WorkingDirectory=/path/to/A.R.T.E.M.I.S.S
EnvironmentFile=/path/to/A.R.T.E.M.I.S.S/.env
ExecStart=/path/to/A.R.T.E.M.I.S.S/venv/bin/python dashboard.py
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start
sudo systemctl daemon-reload
sudo systemctl enable artemis-bot artemis-dashboard
sudo systemctl start artemis-bot artemis-dashboard

# Check status
sudo systemctl status artemis-bot
sudo journalctl -u artemis-bot -f
```

---

## Verifying the Installation

1. **Bot responds to commands:** Open Telegram, find your bot, send `/start` — it should reply with a welcome message.
2. **Bot moderates media:** Send a safe image in a monitored group — the bot should process it silently (nothing happens for SFW content).
3. **Dashboard loads:** Open `http://localhost:5000` — the loading spinner should disappear and show the stats cards.
4. **Database exists:** `ls -la violations.db` should show the file.

---

## Uninstalling

```bash
# Stop the bot process (Ctrl+C or kill the process)

# Deactivate the virtual environment
deactivate

# Remove the project directory
cd ..
rm -rf A.R.T.E.M.I.S.S

# Remove cached HuggingFace model weights (optional, ~330 MB)
rm -rf ~/.cache/huggingface/hub/models--Falconsai--nsfw_image_detection
```
