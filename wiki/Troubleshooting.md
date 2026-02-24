# Troubleshooting

Solutions to common problems when installing, running, or operating A.R.T.E.M.I.S.S.

The bot stared at pixels until it found a problem. Now it's your turn to stare at logs until you find yours.

---

## Startup Errors

### `RuntimeError: BOT_TOKEN environment variable is not set. Aborting.`

**Cause:** The bot can't find a Telegram bot token.

**Fix:**
1. Make sure you copied `.env.example` to `.env`: `cp .env.example .env`
2. Open `.env` and set `BOT_TOKEN=your_actual_token`
3. Make sure the `.env` file is in the same directory you're running `python artemis_bot.py` from

If you're using systemd, ensure `EnvironmentFile=` points to the correct `.env` path.

---

### `Error loading NSFW detection model (image pipeline): ...`

**Cause:** The Falconsai model failed to load.

**Common sub-causes:**
- No internet connection on first run (model download fails)
- Disk full (model needs ~350MB)
- PyTorch not installed correctly for your platform

**Fix:**
1. Check internet connectivity
2. Check available disk space: `df -h`
3. Try manually downloading the model:
   ```bash
   python -c "from transformers import pipeline; pipeline('image-classification', model='Falconsai/nsfw_image_detection')"
   ```
   If this errors, the issue is with your Python/transformers environment.

---

### `ModuleNotFoundError: No module named 'telegram'` (or any other module)

**Cause:** Dependencies aren't installed, or the virtual environment isn't active.

**Fix:**
```bash
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

---

## Bot Not Responding in Group

### Bot connected but not deleting NSFW content

**Check 1: Bot permissions**
The bot needs to be a group admin with Delete Messages and Ban Users permissions.
Go to group settings → Administrators → check the bot's permissions.

**Check 2: Bot is in the right chat**
Send `/start` in the group. If no response, the bot isn't active there.

**Check 3: Check the logs**
Look for handler activity in the console:
```
INFO - Received image from Alice (ID: 123456789)
INFO - Image analysis - User: Alice, Label: normal, Confidence: 0.98
```
If you see nothing when images are sent, the message handler isn't firing.

---

### `/admin_flagged` returns "You are not authorized"

**Cause:** Your Telegram user ID isn't in `ADMIN_IDS`.

**Fix:**
1. Find your user ID with [@userinfobot](https://t.me/userinfobot) on Telegram
2. Add it to `ADMIN_IDS` in `.env`: `ADMIN_IDS=123456789`
3. Restart the bot — environment variables are read at startup

---

## Media Processing Errors

### `Failed to open video file` or `RuntimeError: Failed to open video file`

**Cause:** OpenCV can't open the downloaded video file.

**Common causes:**
- The video format isn't supported by OpenCV headless (rare)
- The file was corrupted or truncated during download

**Fix:**
Check the log for the temp file path and verify the file exists and has a non-zero size.

---

### Bot sent `⚠️ Error processing your media.` to the group

The bot caught an unhandled exception during processing. Check the console logs — there
should be an `ERROR` line with the exception details.

Common causes:
- Disk full (can't write temp file or cached file)
- Database locked (can happen with multiple concurrent writes)
- Telegram API rate limiting (rare)

---

### `Message to be replied not found` in logs (not visible to users)

**Cause:** The bot tried to reply to a message that was already deleted.

**Impact:** None — this is caught and suppressed. The bot continues operating normally.

---

## Database Issues

### `sqlite3.OperationalError: database is locked`

**Cause:** Multiple processes are writing to the same SQLite file simultaneously.

**Fix:**
1. Make sure only one instance of `artemis_bot.py` is running
2. Stop duplicate processes, then restart

---

### Stats are showing 0 for everything

**Fix:**
```bash
python setup_db.py
```
This creates the initial stat rows with `INSERT OR IGNORE` — existing data is preserved.

---

## Dashboard Issues

### Dashboard shows blank page or "Loading data..." forever

**Check 1:** Make sure `python dashboard.py` is running and shows `Running on http://0.0.0.0:5000`.

**Check 2:** The dashboard looks for `violations.db` in the current working directory.
Run `dashboard.py` from the same directory as `artemis_bot.py`.

**Check 3:** Open browser developer tools (F12) → Console. Look for JavaScript errors.

---

### Dashboard is accidentally accessible from the internet

**This is a security issue — see [SECURITY.md](../SECURITY.md).**

By default, Flask runs on `0.0.0.0:5000`, accessible on all network interfaces.

**Quick fix — bind to localhost only:**
Change the last line in `dashboard.py`:
```python
socketio.run(app, host='127.0.0.1', debug=False)
```

Or use a firewall rule to block external access to port 5000.

---

## Performance Issues

### Bot is very slow on video analysis

**Likely cause:** Running on CPU without a GPU.

**Check:**
```bash
python -c "import torch; print(torch.cuda.is_available())"
```

If this prints `False`, you're on CPU.

**Options:**
- Deploy on a machine with a CUDA GPU
- Reduce `num_frames` in the `handle_video()` call (default is 6)
- Accept that CPU inference is slower but still functional

---

### Bot stops responding after running for a while

**Possible causes:**
- The process ran out of memory (OOM)
- An unhandled exception terminated the event loop

**Fix:**
- Monitor memory usage with `htop` or `free -h`
- Use systemd with `Restart=on-failure` to auto-restart on failure
- Review recent log output for exceptions that appeared before the silence

---

## Still stuck?

1. Check the [GitHub Issues](https://github.com/Kaelith69/A.R.T.E.M.I.S.S/issues) — someone else may have had the same problem
2. Open a new issue with:
   - Your OS and Python version
   - The full error message and stack trace from the console
   - What you were trying to do when the error occurred
