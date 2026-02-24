# Privacy

What A.R.T.E.M.I.S.S. stores, what it doesn't, how long it keeps things, and how to delete it.

---

## What Data is Stored

### SQLite Database (`violations.db`)

| Table | What's stored | Personal data? |
|---|---|---|
| `violations` | Telegram user ID + violation count | User ID only (no name, no username) |
| `stats` | Aggregate counters (totals only) | No |
| `actions` | User ID + action type + timestamp | User ID only |
| `contents` | Media type + NSFW flag (no user ID) | No |

**Key point:** The bot stores Telegram user IDs — numeric identifiers. It does not store:
- Usernames
- First/last names
- Phone numbers
- Profile photos
- Message content (text, captions, etc.)

If you need to look up who a user ID belongs to, you'd need to cross-reference with Telegram — the bot doesn't maintain that mapping.

### Cached Flagged Media

NSFW content that is flagged is **cached to disk** for admin review:
- Images → `flagged_images/user_<id>_<timestamp>.jpg`
- Videos/GIFs → `flagged_videos/user_<id>_<timestamp>.mp4|gif`

This media stays on disk indefinitely until an admin manually cleans it up. The bot never automatically deletes cached flagged media.

SFW media is **never cached** — the temp file is deleted immediately after classification.

### Temporary Files

During processing, media is written to a temp file (`temp_<user_id>.jpg`, `temp_<user_id>.mp4`, etc.) in the bot's working directory. These files are:
- Deleted immediately after a SFW classification
- Renamed and moved to the cache directory after a NSFW classification

If the bot crashes mid-processing, temp files may be left behind. They can be safely deleted manually.

---

## What Data is NOT Stored

- Message text or captions
- Usernames or display names
- Profile pictures
- Group names or chat IDs (beyond what the Telegram event contains in memory)
- Media from SFW messages (deleted immediately)
- Any analytics beyond the counters in the `stats` table

---

## Where Data Lives

Everything is stored **locally on your server**. There is no external data transmission beyond:
- The Telegram Bot API connection (required for the bot to function — messages flow through Telegram's servers as normal)
- The HuggingFace model download (one-time download of model weights on first run)

**The model runs locally.** Your users' media is not sent to HuggingFace or any external API for classification. All inference happens on your machine.

---

## Data Retention

The bot has no automatic data retention policy. Everything accumulates until you clean it up.

### Recommended practices

**Violations table:** Old violation records for users who were banned or are no longer in the group can be cleaned up:
```sql
DELETE FROM violations WHERE count = 0;
```

**Actions table:** The audit log grows indefinitely. If it gets large:
```sql
DELETE FROM actions WHERE timestamp < '2025-01-01 00:00:00';
```

**Cached flagged media:** Review and delete files in `flagged_images/` and `flagged_videos/` periodically once you've reviewed them.

**Stats table:** Counters only — no personal data. Leave them alone or reset if you want a fresh start:
```sql
UPDATE stats SET value = 0;
```

---

## Access Control

- The SQLite database is a local file. Protect it with filesystem permissions (read/write for the bot user only).
- The flagged media directories contain NSFW content. Restrict access appropriately.
- The **dashboard has no authentication** in v0.1 — it exposes the DB contents over HTTP. Do not expose it to the public internet. Bind to localhost and use an authenticated reverse proxy (nginx + htpasswd, etc.) if you need remote access.

---

## GDPR / Data Subject Requests

If you're operating this bot in a context subject to GDPR (or similar regulation), and a user requests deletion of their data:

1. Find their Telegram user ID
2. Run the following:

```sql
DELETE FROM violations WHERE user_id = <user_id>;
DELETE FROM actions WHERE user_id = <user_id>;
```

3. Manually delete any cached flagged media files matching `user_<id>_*.jpg/mp4/gif`

The `contents` table doesn't contain user IDs, so nothing to delete there.

---

## Summary

| Data type | Stored | Where | How long |
|---|---|---|---|
| Violation counts | Yes | SQLite | Until manually deleted |
| Action audit log | Yes | SQLite | Until manually deleted |
| Flagged media | Yes | Disk | Until manually deleted |
| SFW media | No | Temp file (deleted after scan) | < seconds |
| Usernames / names | No | — | — |
| Message text | No | — | — |
| Analytics telemetry | No | — | — |
