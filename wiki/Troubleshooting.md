# Troubleshooting

Solutions to common problems encountered when installing, running, or operating A.R.T.E.M.I.S.S.

---

## Table of Contents

- [Bot Startup Errors](#bot-startup-errors)
- [Bot Not Responding](#bot-not-responding)
- [NSFW Detection Issues](#nsfw-detection-issues)
- [Permission & Ban Errors](#permission--ban-errors)
- [Database Errors](#database-errors)
- [Dashboard Issues](#dashboard-issues)
- [Dependency Installation Errors](#dependency-installation-errors)
- [Performance Issues](#performance-issues)
- [Logs & Diagnostics](#logs--diagnostics)

---

## Bot Startup Errors

### `RuntimeError: BOT_TOKEN environment variable is not set. Aborting.`

**Cause:** The `.env` file does not exist or `BOT_TOKEN` is missing/empty.

**Fix:**
```bash
cp .env.example .env
# Edit .env and set BOT_TOKEN=your_token_here
```

Verify the token is set:
```bash
grep BOT_TOKEN .env
```

---

### `Error loading NSFW detection model: ...`

**Cause:** The HuggingFace model failed to download or load. Common sub-causes:
- No internet connection on first run
- Insufficient disk space (~330 MB needed)
- Corrupted model cache

**Fix:**
```bash
# Check disk space
df -h ~/.cache

# Clear and re-download the model cache
rm -rf ~/.cache/huggingface/hub/models--Falconsai--nsfw_image_detection

# Re-run the bot to trigger a fresh download
python artemis_bot.py
```

If behind a corporate proxy, set the `HTTPS_PROXY` environment variable:
```bash
export HTTPS_PROXY=http://proxy.example.com:8080
python artemis_bot.py
```

---

### `ModuleNotFoundError: No module named 'telegram'`

**Cause:** Dependencies are not installed, or you are running from outside the virtual environment.

**Fix:**
```bash
# Make sure the venv is active
source venv/bin/activate       # Linux/macOS
# venv\Scripts\activate        # Windows

# Re-install dependencies
pip install -r requirements.txt
```

---

### `ModuleNotFoundError: No module named 'cv2'`

**Cause:** OpenCV is not installed.

**Fix:**
```bash
pip install opencv-python-headless>=4.8
```

On Windows, if the headless version fails:
```bash
pip install opencv-python>=4.8
```

---

## Bot Not Responding

### Bot does not respond to `/start` or any command

**Check 1 — Is the bot running?**
```bash
# Look for the process
ps aux | grep artemis_bot
```

**Check 2 — Is the bot token correct?**
Open Telegram → @BotFather → `/mybots` → select your bot → API Token. Verify it matches `BOT_TOKEN` in `.env`.

**Check 3 — Network connectivity**
```bash
curl -s "https://api.telegram.org/bot${BOT_TOKEN}/getMe"
```
If this returns `{"ok":false}`, the token is invalid. If it times out, there is a network issue.

**Check 4 — Check the logs**
```bash
python artemis_bot.py 2>&1 | tee bot.log
```
Look for errors in the output.

---

### Bot responds in private chat but not in the group

**Cause:** The bot has not been added to the group, or lacks the necessary permissions.

**Fix:**
1. Confirm the bot is a member of the group.
2. Confirm the bot has been promoted to **Admin** with *Delete Messages* and *Ban Users* enabled.
3. In supergroups, verify "Privacy mode" is set correctly — by default, bots only receive commands, not all messages. Go to @BotFather → `/mybots` → your bot → Bot Settings → Group Privacy → **Disable** (if you need the bot to see all messages, which it does for media handlers).

> **Note:** `filters.PHOTO`, `filters.VIDEO`, and `filters.ANIMATION` work even with Privacy Mode enabled because media handlers respond to specific update types.

---

## NSFW Detection Issues

### Legitimate content is being deleted (false positives)

**Cause:** The ViT model is probabilistic and may occasionally misclassify borderline content.

**Options:**
1. Review the cached image in `flagged_images/` to confirm it was a false positive.
2. Use `/admin_reset <user_id>` to clear the user's violation count.
3. The confidence threshold (`nsfw_threshold=0.5`) can be raised in `handle_video()` to reduce false positives, at the cost of potentially missing true positives.

---

### NSFW content is not being detected (false negatives)

**Cause:** The model's confidence score for the content may be below the 0.5 threshold, or the content may genuinely be in a grey area.

**Options:**
1. Lower the `nsfw_threshold` in `handle_video()` (e.g., to `0.35`).
2. Increase `num_frames` for video analysis to sample more of the video.
3. Use `/admin_ban <user_id>` for manual enforcement.

---

### Bot processes the image but does nothing

**Cause:** The content was classified as SFW (correct behaviour). Check the logs:

```
INFO - Image analysis - User: John, Label: normal, Confidence: 0.97
```

If `Label: normal`, the model is confident the content is safe.

---

## Permission & Ban Errors

### `Can't remove chat owner`

**Cause:** The bot attempted to ban the group owner, which Telegram prohibits.

**Behaviour:** A.R.T.E.M.I.S.S. handles this gracefully — it sends a warning message instead of crashing:
```
🚫 You have exceeded the NSFW violation threshold, but banning the chat owner is not allowed.
```

This is expected behaviour, not a bug.

---

### `Not enough rights to ban members` or similar

**Cause:** The bot was not granted the **Ban Users** admin permission.

**Fix:** Go to group → Manage Group → Administrators → your bot → enable **Ban Users**.

---

### `Message to be replied not found`

**Cause:** The original message was already deleted (by Telegram, another bot, or the user themselves) before the bot could delete it.

**Behaviour:** The error is caught and logged — the bot continues operating normally. This is a known race condition.

---

## Database Errors

### `sqlite3.OperationalError: no such table: contents`

**Cause:** The database was created before the `contents` table was added.

**Fix:**
```bash
# Option 1: Re-run the setup script (it uses IF NOT EXISTS — safe)
python setup_db.py

# Option 2: Add the table manually
sqlite3 violations.db "
CREATE TABLE IF NOT EXISTS contents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    is_nsfw INTEGER
);"
```

---

### `sqlite3.OperationalError: database is locked`

**Cause:** Two processes are writing to the database simultaneously (rare with SQLite's default WAL mode off).

**Fix:**
```bash
# Check if another bot process is running
ps aux | grep artemis_bot

# If there are multiple instances, kill the extras
kill <PID>
```

For high-traffic deployments, consider switching to PostgreSQL (see [Architecture — Extension Points](Architecture.md#extension-points)).

---

### Database file keeps growing unexpectedly

**Cause:** The `actions` and `contents` tables accumulate a row for every moderation event. This is by design for audit purposes.

**Maintenance:**
```bash
# Delete actions older than 90 days
sqlite3 violations.db "
DELETE FROM actions WHERE timestamp < datetime('now', '-90 days');"

# Reclaim disk space
sqlite3 violations.db "VACUUM;"
```

---

## Dashboard Issues

### Dashboard shows "Loading data..." indefinitely

**Cause:** Socket.IO failed to connect. Common sub-causes:
- `dashboard.py` is not running
- A firewall is blocking WebSocket connections
- The browser does not support WebSockets

**Fix:**
1. Ensure `python dashboard.py` is running.
2. Check the browser console (F12 → Console) for WebSocket errors.
3. Try a different browser.
4. If behind a reverse proxy, ensure WebSocket upgrade headers are forwarded.

---

### Charts are empty or show zeros

**Cause:** The `violations.db` database may be empty (no moderation events have occurred yet), or the dashboard is reading a different database file than the bot.

**Fix:**
1. Verify both processes use the same `DB_FILE` value in `.env`.
2. Check the database directly:
```bash
sqlite3 violations.db "SELECT * FROM stats;"
```

---

### `OSError: [Errno 98] Address already in use`

**Cause:** Port 5000 is already in use by another process.

**Fix:**
```bash
# Find what's using port 5000
lsof -i :5000

# Kill it (replace <PID> with the actual PID)
kill <PID>

# Or run dashboard on a different port
python -c "from dashboard import app, socketio; socketio.run(app, port=5001)"
```

---

## Dependency Installation Errors

### `ERROR: Could not build wheels for opencv-python-headless`

**Cause:** Missing system libraries for OpenCV on headless Linux.

**Fix:**
```bash
sudo apt-get update
sudo apt-get install -y libgl1 libglib2.0-0
pip install opencv-python-headless
```

---

### `torch` installation takes too long or fails

**Cause:** Default PyTorch includes CUDA wheels (~2 GB). If you don't have a GPU, install the CPU-only version:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

---

## Performance Issues

### High CPU usage during video processing

**Cause:** CPU inference for a 6-frame video analysis requires several hundred milliseconds. If many videos are processed simultaneously, CPU usage will spike.

**Solutions:**
1. Install a GPU and enable CUDA (see [Installation — GPU Setup](Installation.md#gpu-setup-optional)).
2. Reduce `num_frames` from 6 to 3 in `handle_video()` for faster processing.
3. If the server is under-powered, consider reducing `FLAG_THRESHOLD` so fewer repeat offenders accumulate before being banned.

---

### Slow startup (model loading)

**Cause:** The first startup downloads the ViT model weights (~330 MB). Subsequent startups load from `~/.cache/huggingface/`.

**Expected startup time:**
- First run: 30–90 seconds (download + load)
- Subsequent runs: 5–15 seconds (load from cache)

---

## Logs & Diagnostics

### Enable verbose logging

The bot logs to stdout at INFO level by default. All logs include timestamps:

```
2025-02-20 14:32:10 - __main__ - INFO - 🚀 Bot is starting...
2025-02-20 14:32:11 - __main__ - INFO - Received image from John (ID: 123456789)
2025-02-20 14:32:11 - __main__ - INFO - Image analysis - User: John, Label: normal, Confidence: 0.98
```

### Save logs to a file

```bash
python artemis_bot.py 2>&1 | tee -a artemis.log
```

### Inspect the database interactively

```bash
sqlite3 violations.db

# Show all tables
.tables

# View recent actions
SELECT * FROM actions ORDER BY timestamp DESC LIMIT 20;

# View all stats
SELECT * FROM stats;

# View all violations
SELECT * FROM violations;

# Exit
.quit
```

### Check the Telegram API directly

```bash
# Verify token is valid
curl "https://api.telegram.org/bot${BOT_TOKEN}/getMe"

# Check for pending updates
curl "https://api.telegram.org/bot${BOT_TOKEN}/getUpdates"
```
