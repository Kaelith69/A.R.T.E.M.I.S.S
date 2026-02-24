# Installation

Complete installation guide for A.R.T.E.M.I.S.S. on Linux, macOS, and Windows.

---

## Prerequisites

Before you start, make sure you have:

- **Python 3.10 or newer** — check with `python --version` or `python3 --version`
- **pip** — should come with Python; check with `pip --version`
- **A Telegram bot token** — get one from [@BotFather](https://t.me/BotFather) with `/newbot`
- **Your Telegram user ID** — use [@userinfobot](https://t.me/userinfobot) to find it
- **~500MB disk space** — ~350MB for the Falconsai ViT model + your data
- **Internet access** for the initial model download (subsequent starts use the local cache)

Optional but recommended:
- A CUDA-capable NVIDIA GPU — inference is *dramatically* faster. Without it the bot still works, just slower.
- A Linux server or a machine that can run persistently

---

## Step 1 — Get the Code

```bash
git clone https://github.com/Kaelith69/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S
```

Don't have git? Download the zip from the GitHub releases page and unzip it.

---

## Step 2 — Create a Virtual Environment

This is not optional. Don't pollute your system Python. Future you will thank present you.

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

You should see `(venv)` in your terminal prompt when the environment is active.

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `python-telegram-bot` — the Telegram API client
- `torch` — PyTorch for model inference
- `transformers` — HuggingFace Transformers (Falconsai model)
- `Pillow` — image handling
- `opencv-python-headless` — video frame extraction
- `Flask` + `flask-socketio` — the admin dashboard
- `python-dotenv` — `.env` file loading

> ⏳ PyTorch is a large install (~1.5GB depending on platform/CUDA version). Grab a beverage.

### For GPU support (CUDA)

If you have an NVIDIA GPU and want to use it, install the CUDA-enabled version of PyTorch. The default `requirements.txt` installs PyTorch without specifying a CUDA version, which may default to CPU on some platforms. Check the [PyTorch install matrix](https://pytorch.org/get-started/locally/) for your specific CUDA version.

The bot automatically detects CUDA at startup via `torch.cuda.is_available()`.

---

## Step 4 — Configure the Bot

Copy the example config and edit it:

```bash
cp .env.example .env
```

Open `.env` in your editor:

```env
# Required — get this from @BotFather on Telegram
BOT_TOKEN=your_telegram_bot_token_here

# Required — your Telegram user ID (or multiple, comma-separated)
# Use @userinfobot to find yours
ADMIN_IDS=123456789

# Optional — how many violations before a user is banned (default: 3)
FLAG_THRESHOLD=3

# Optional — paths can be left as defaults
DB_FILE=violations.db
FLAGGED_IMAGES_DIR=flagged_images
FLAGGED_VIDEOS_DIR=flagged_videos

# Optional — leave blank for auto-generated (fine for local use)
DASHBOARD_SECRET_KEY=change_me_to_a_long_random_string
```

**The bot will refuse to start without `BOT_TOKEN`.**

If `ADMIN_IDS` is empty, a warning is printed at startup and no admin will receive NSFW notifications — the bot still moderates, but silently.

---

## Step 5 — Initialize the Database

```bash
python setup_db.py
```

This creates `violations.db` with all required tables and initial stats counters. It's safe to run multiple times — all operations are `IF NOT EXISTS` / `INSERT OR IGNORE`.

---

## Step 6 — Start the Bot

```bash
python artemis_bot.py
```

On first run, you'll see something like:

```
Downloading model: Falconsai/nsfw_image_detection ...
...
VideoContentAnalyzer initialized using model: Falconsai/nsfw_image_detection
🚀 Bot is starting...
```

After the model downloads, the bot connects to Telegram and starts long-polling. You'll see `Bot is starting...` when it's ready.

---

## Step 7 — Add the Bot to Your Group

1. Open Telegram, find your bot by its username
2. Add it to the group you want to moderate
3. Promote it to **Group Admin** with these permissions:
   - ✅ Delete messages
   - ✅ Ban users
4. Send `/start` in the group to verify it's alive

---

## Step 8 — (Optional) Start the Dashboard

In a second terminal (with the venv activated):

```bash
python dashboard.py
```

Open `http://localhost:5000` in your browser. You'll see live stats from the bot.

---

## Running on a Server

For persistent operation on a Linux server, use a process manager.

### systemd (recommended for Linux)

Create `/etc/systemd/system/artemiss.service`:

```ini
[Unit]
Description=A.R.T.E.M.I.S.S. Telegram Moderation Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/A.R.T.E.M.I.S.S
ExecStart=/path/to/A.R.T.E.M.I.S.S/venv/bin/python artemis_bot.py
Restart=on-failure
RestartSec=10
EnvironmentFile=/path/to/A.R.T.E.M.I.S.S/.env

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable artemiss
sudo systemctl start artemiss
sudo systemctl status artemiss
```

### tmux / screen (quick and dirty)

```bash
tmux new-session -d -s artemiss 'cd /path/to/A.R.T.E.M.I.S.S && source venv/bin/activate && python artemis_bot.py'
```

---

## Verifying Installation

Send a test image to your group (a SFW one). The bot should:
- Process it silently (no response for clean content)
- Log `Image analysis - User: ..., Label: normal, Confidence: ...` in the console

Send `/stats` in the group — you should see `Total Scanned: 1`.
