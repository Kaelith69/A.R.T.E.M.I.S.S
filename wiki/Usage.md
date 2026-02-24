# Usage

Complete guide to operating A.R.T.E.M.I.S.S. — group setup, commands, violation lifecycle, and dashboard.

---

## Prerequisites

- Bot is installed and running (`python artemis_bot.py`)
- Bot has admin permissions in the target Telegram group (delete messages + ban users)
- `ADMIN_IDS` is configured with at least one admin Telegram user ID

---

## Adding the Bot to a Group

1. Find your bot on Telegram by its username
2. In the group, tap the group name → Add Members → search for your bot
3. After adding, go to group settings → Administrators → promote the bot
4. Grant: **Delete Messages** and **Ban Users**
5. Send `/start` in the group to confirm the bot is online

The bot monitors every photo, video, and GIF from that point on. No configuration needed per-chat — it just works.

---

## Bot Commands

### Available to Everyone

#### `/start`
Sends the welcome message with a quick summary of what the bot does.

```
🤖 Welcome to A.R.T.E.M.I.S.S.!
Send me an image or video to check for NSFW content.
Use /violations to check your NSFW violation count.
Use /help for more commands.
```

#### `/help`
Full command reference.

#### `/violations`
Check your own violation count.

```
⚠️ Alice, you have 1 NSFW violation(s).
```

#### `/stats`
View aggregate bot statistics.

```
📊 Bot Statistics

Total Contents Scanned: 142
Total NSFW Detected: 7
Total SFW: 135
Total Users Banned: 1
Total Violations: 11
```

---

### Admin-Only Commands

These commands only work for user IDs listed in `ADMIN_IDS`. Anyone else gets:
```
❌ You are not authorized to use this command.
```

#### `/admin_flagged`
List all users who have at least one violation.

```
Flagged Users:
User ID: 123456789, Violations: 2
User ID: 987654321, Violations: 1
```

#### `/admin_reset <user_id>`
Reset a specific user's violation count to zero.

```
/admin_reset 123456789
→ Reset violation count for user ID: 123456789
```

Useful when a user was falsely flagged or has served their time.

#### `/admin_ban <user_id>`
Manually ban a user from the current group, regardless of their violation count.

```
/admin_ban 123456789
→ 🚫 User ID 123456789 has been banned.
```

---

## How Moderation Works

### Images

When a user sends a photo:
1. Bot downloads the image to a temp file
2. Runs it through the Falconsai ViT pipeline
3. Gets back `{"label": "nsfw"|"normal", "score": 0.0–1.0}`
4. If label is `"nsfw"` → NSFW action flow
5. If label is `"normal"` → delete temp file, no action

### Videos and GIFs

When a user sends a video or animation:
1. Bot downloads the file to a temp file
2. `VideoContentAnalyzer` opens the file with OpenCV
3. Samples 6 frames at evenly-spaced intervals
4. Each frame runs through the ViT model
5. If any frame is `"nsfw"` with confidence ≥ 50% → **stop early**, NSFW action flow
6. If all 6 frames are clean → delete temp file, no action

The early-stop behavior means the bot doesn't waste compute analyzing the remaining 5 frames of a video once it's found enough evidence to act.

---

## NSFW Action Flow

When NSFW content is detected:

1. **Delete the message** — the offending photo/video/GIF is removed from the group
2. **Warn the user** — bot sends a message: `⚠️ NSFW content detected in your image! Violation 1/3.`
3. **Cache the media** — saved to `flagged_images/` or `flagged_videos/` with a timestamp filename
4. **Notify admins** — each admin receives a DM with:
   - Alert message with user name, ID, and violation count
   - The cached flagged media (forwarded for review)
5. **Check the threshold** — if violation count ≥ `FLAG_THRESHOLD`:
   - Auto-ban the user from the group (group/supergroup only)
   - Log `user_banned` to the actions table
   - Reset the user's violation count
   - Announce the ban in the group

**Private chats:** If the bot is used in a private chat (1:1 with the bot), violations are tracked but the user cannot be banned — Telegram doesn't allow banning in private chats. A message is sent explaining this.

**Chat owners:** Telegram prevents banning a group's owner. If a chat owner somehow triggers the threshold, the bot catches the `BadRequest: Can't remove chat owner` error and sends a polite (and slightly awkward) message instead.

---

## Violation Lifecycle

```
0 violations → user is clean
1 violation  → warning: "1/3"
2 violations → warning: "2/3"
3 violations → banned + count reset to 0
```

Admins can manually reset a user's count at any time with `/admin_reset`.

---

## Admin Dashboard

Start the dashboard server:

```bash
python dashboard.py
```

Open `http://localhost:5000`.

### What you'll see

**Status Cards (top row):**
- Total Scanned
- Total NSFW Detected
- Total SFW
- Total Violations
- Total Users Banned

**Charts:**
- Content type breakdown (images vs videos)
- Violation timeline
- Action log table

**Live updates:**
The dashboard connects via Socket.IO. Stats refresh every 10 seconds automatically — no page reload needed. When the bot processes something, it shows up on the dashboard within the next refresh cycle.

### API Endpoints

You can also hit the REST API directly if you want to build your own tooling:

```
GET /api/stats         → {"total_contents_scanned": 42, ...}
GET /api/actions       → [{id, user_id, action, timestamp}, ...]
GET /api/all_data      → {stats, violations, actions, content_types}
```

---

## Tuning Behavior

All behavior is configurable via `.env`:

| Setting | Effect |
|---|---|
| `FLAG_THRESHOLD=5` | User needs 5 strikes before ban (less aggressive) |
| `FLAG_THRESHOLD=1` | One strike and you're out (zero tolerance) |
| `FLAGGED_IMAGES_DIR=/mnt/storage/flagged` | Store cached media on a different volume |

The model confidence threshold (50%) is currently hardcoded in `artemis_bot.py` and `VideoContentAnalyzer.analyze_video()`. To change it, modify `nsfw_threshold` in the `handle_video()` call or the `score` comparison in `handle_image()`.
