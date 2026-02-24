# Usage

Complete guide to operating A.R.T.E.M.I.S.S. — including group setup, bot commands, violation lifecycle, and dashboard usage.

---

## Table of Contents

- [Setting Up in a Telegram Group](#setting-up-in-a-telegram-group)
- [Bot Commands Reference](#bot-commands-reference)
- [How Moderation Works](#how-moderation-works)
- [Violation Lifecycle](#violation-lifecycle)
- [Admin Workflow](#admin-workflow)
- [Dashboard Guide](#dashboard-guide)
- [Statistics Explained](#statistics-explained)
- [Adjusting Sensitivity](#adjusting-sensitivity)
- [Edge Cases & Behaviour Notes](#edge-cases--behaviour-notes)

---

## Setting Up in a Telegram Group

### Step 1 — Add the bot to your group

In Telegram, open your group → **Add Member** → search for your bot's username → Add.

### Step 2 — Grant admin permissions

Go to group **Manage Group** → **Administrators** → your bot → enable:

| Permission | Required | Reason |
|---|---|---|
| **Delete Messages** | ✅ Yes | To remove NSFW content |
| **Ban Users** | ✅ Yes | For auto-ban enforcement |
| **Send Messages** | ✅ Yes | To send warnings and notifications |
| Change Group Info | ❌ No | Not used |
| Pin Messages | ❌ No | Not used |

### Step 3 — Start the bot process

```bash
python artemis_bot.py
```

The bot will immediately begin monitoring all media sent to the group.

---

## Bot Commands Reference

### User Commands

These commands can be used by any group member in private chat with the bot or directly in the group.

#### `/start`

Sends the welcome message with a brief overview of the bot's capabilities.

**Example response:**
```
🤖 Welcome to A.R.T.E.M.I.S.S.!

Send me an image or video to check for NSFW content.
Use /violations to check your NSFW violation count.
Use /help for more commands.
```

#### `/help`

Displays the full command reference with HTML formatting.

#### `/violations`

Shows your current violation count.

**Example response:**
```
⚠️ John, you have 1 NSFW violation(s).
```

#### `/stats`

Shows aggregate moderation statistics.

**Example response:**
```
📊 Bot Statistics

Total Contents Scanned: 1,247
Total NSFW Detected: 38
Total SFW: 1,209
Total Users Banned: 4
Total Violations: 87
```

---

### Admin Commands

These commands require your Telegram user ID to be listed in the `ADMIN_IDS` environment variable. Using them without authorization returns an error message.

#### `/admin_flagged`

Lists all users who currently have at least one violation on record.

**Example response:**
```
Flagged Users:
User ID: 123456789, Violations: 2
User ID: 987654321, Violations: 1
```

#### `/admin_reset <user_id>`

Resets a specific user's violation count to zero.

**Usage:**
```
/admin_reset 123456789
```

**Example response:**
```
Reset violation count for user ID: 123456789
```

#### `/admin_ban <user_id>`

Manually bans a specific user from the current group, regardless of their violation count.

**Usage:**
```
/admin_ban 123456789
```

**Example response:**
```
🚫 User ID 123456789 has been banned.
```

> **Note:** This command bans the user from the group in which the command was issued. Ensure you run it from the correct group.

---

## How Moderation Works

### Image Moderation

1. A user sends a photo in a monitored group.
2. The bot downloads the photo to a temporary file.
3. The image is passed through the `Falconsai/nsfw_image_detection` ViT classifier.
4. The classifier returns a label (`nsfw` or `normal`) and a confidence score.
5. If `label == "nsfw"`:
   - The message is deleted
   - The violation count is incremented
   - The image is cached for admin review
   - Admins receive an alert with the image
   - If violations ≥ `FLAG_THRESHOLD`, the user is banned
6. If `label == "normal"`: the temporary file is deleted silently.

### Video & GIF Moderation

1. A user sends a video or GIF (animation) in the group.
2. The bot downloads it to a temporary file.
3. `VideoContentAnalyzer.analyze_video()` extracts 6 evenly-spaced frames using OpenCV.
4. Each frame is converted to a PIL image and classified by the ViT model.
5. Analysis stops immediately on the first NSFW frame detected (`stop_on_nsfw=True`).
6. The same enforcement actions as image moderation are applied if NSFW is found.

### Confidence Threshold

The default NSFW confidence threshold is **0.5 (50%)**. Content with a score below this threshold is treated as safe, even if the top label is `nsfw`. This reduces false positives on ambiguous content.

---

## Violation Lifecycle

```
User sends NSFW content
        │
        ▼
Violation count incremented (violations table)
        │
        ├─ Count = 1 → Warning: "⚠️ NSFW content detected! Violation 1/3"
        ├─ Count = 2 → Warning: "⚠️ NSFW content detected! Violation 2/3"
        └─ Count = 3 → Warning sent
                    → ban_chat_member() called
                    → "🚫 [user] has been banned for multiple NSFW violations."
                    → violation count reset to 0
                    → admin notification with cached media
```

**Changing the threshold:**
Set `FLAG_THRESHOLD` in `.env`. For example, `FLAG_THRESHOLD=5` allows 5 violations before ban.

---

## Admin Workflow

### Reviewing Flagged Content

When NSFW content is detected, each configured admin receives:

1. A text message: `🚨 NSFW content detected from user [name] (ID: [id]). Violation X/Y.`
2. The cached flagged media (photo or video) forwarded directly to the admin's private chat.

Flagged files are also saved to disk:
- Images: `flagged_images/user_{id}_{timestamp}.jpg`
- Videos: `flagged_videos/user_{id}_{timestamp}.mp4` or `.gif`

### Handling False Positives

If a user is incorrectly flagged:

1. Use `/admin_reset <user_id>` to clear their violation count.
2. The original message has already been deleted — you cannot restore it.
3. Consider informing the user that the moderation was a false positive.

### Manual Ban

If you need to ban a user for reasons other than NSFW content (e.g., spam, harassment):

```
/admin_ban <user_id>
```

This issues a direct `ban_chat_member` API call and does **not** require any violations on record.

---

## Dashboard Guide

Start the dashboard:
```bash
python dashboard.py
```

Open [http://localhost:5000](http://localhost:5000).

### Status Cards

The top row shows five live counters:

| Card | What it shows |
|---|---|
| **Total Scanned** | All media items processed since the database was created |
| **NSFW Detected** | Items classified as NSFW |
| **SFW Detected** | Items classified as safe |
| **Users Banned** | Total ban events |
| **Current Violations** | Total accumulated violation increments |

### Charts

| Chart | Type | Description |
|---|---|---|
| **Action Trend** | Line | Number of moderation actions per timestamp |
| **Content Breakdown** | Bar | SFW vs NSFW totals side-by-side |
| **Actions Distribution** | Doughnut | Share of each action type (content_removed, user_banned) |
| **Stats Overview** | Horizontal bar | All five stat counters in one view |
| **Analytics Comparison** | Multi-line | NSFW, SFW, and bans plotted over time |

### Live Updates

The dashboard auto-refreshes every **10 seconds** via Socket.IO. No manual page refresh is needed.

### Action Trend Chart — Zoom

The Action Trend chart supports:
- **Mouse wheel** — zoom in/out on the time axis
- **Click and drag** — pan left/right
- **Pinch** — zoom on touch devices

---

## Statistics Explained

| Statistic | DB key | Description |
|---|---|---|
| Total Scanned | `total_contents_scanned` | Incremented for every photo, video, or GIF processed |
| NSFW Detected | `total_nsfw_detected` | Incremented when classifier returns `nsfw` |
| SFW | `total_sfw` | Incremented when classifier returns `normal` |
| Users Banned | `total_users_banned` | Incremented at auto-ban (not at `/admin_ban`) |
| Violations | `total_violations` | Incremented with every call to `add_violation()` |

> `total_contents_scanned` should equal `total_nsfw_detected + total_sfw` (plus any errors).

---

## Adjusting Sensitivity

### Change the Violation Threshold

In `.env`:
```env
FLAG_THRESHOLD=5
```

Restart the bot for the change to take effect.

### Change the Video Frame Count

The number of sampled frames is set in `handle_video()`:
```python
results = analyzer.analyze_video(
    video_path=temp_path,
    num_frames=6,          # increase for higher accuracy, decrease for speed
    stop_on_nsfw=True,
    nsfw_threshold=0.5
)
```

To change it without modifying source code, this could be made an environment variable in a future release (see [Roadmap](Roadmap.md)).

### Change the NSFW Confidence Threshold

The `nsfw_threshold=0.5` parameter in `analyze_video()` controls the minimum confidence score for video frames to be flagged. The image pipeline uses the model's top-1 label directly (no threshold applied — `label.lower() == "nsfw"` check only). Both can be made configurable via environment variables.

---

## Edge Cases & Behaviour Notes

| Scenario | Behaviour |
|---|---|
| Bot is not group admin | Cannot delete messages or ban users; will log errors |
| User is the chat owner | Ban attempt fails gracefully; warning is sent instead |
| Bot used in private chat | Warning and violation tracking work; ban is not possible in private chats |
| Same user in multiple groups | Violation count is global — violations in any group count towards the threshold |
| Bot restarts | All violation counts, stats, and audit logs are preserved in SQLite |
| Model download fails | Bot refuses to start with a clear error message |
| ADMIN_IDS not set | Bot starts with a warning; no admin notifications will be sent |
| Very long video | Only 6 frames are sampled regardless of duration |
| Animated stickers | Currently not handled (no `filters.Sticker` handler) |
