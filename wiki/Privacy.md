# Privacy

This page describes how A.R.T.E.M.I.S.S. collects, stores, and handles data — including user data, media, and configuration secrets.

---

## Table of Contents

- [Design Philosophy](#design-philosophy)
- [What Data is Collected](#what-data-is-collected)
- [What Data is NOT Collected](#what-data-is-not-collected)
- [Data Storage](#data-storage)
- [Media Retention](#media-retention)
- [Credentials and Secrets](#credentials-and-secrets)
- [Dashboard Security](#dashboard-security)
- [Telegram API Compliance](#telegram-api-compliance)
- [Recommendations for Operators](#recommendations-for-operators)
- [Data Deletion](#data-deletion)

---

## Design Philosophy

A.R.T.E.M.I.S.S. is built on the principle of **data minimalism**: only the data strictly necessary for moderation enforcement is collected and retained. The system is designed to be self-hosted — all data stays on your own server, with no third-party telemetry, analytics services, or cloud storage.

---

## What Data is Collected

| Data | Where stored | Purpose | Retention |
|---|---|---|---|
| Telegram user ID (integer) | `violations` table | Violation tracking and ban enforcement | Until manually deleted or reset |
| Violation count (integer) | `violations` table | Threshold enforcement | Reset to 0 on auto-ban; deleted via `/admin_reset` |
| Action type + timestamp | `actions` table | Audit log | Indefinite (no automatic purging) |
| Content type + NSFW flag | `contents` table | Dashboard analytics | Indefinite |
| Aggregated stat counters | `stats` table | Dashboard counters | Indefinite |
| Flagged media files | `flagged_images/` or `flagged_videos/` | Admin review, evidence retention | Until manually deleted by the operator |

---

## What Data is NOT Collected

- ❌ User names, first names, or usernames
- ❌ Message text content
- ❌ Group names or group IDs
- ❌ User phone numbers or email addresses
- ❌ IP addresses
- ❌ Non-NSFW media (safe content is processed in memory and the temp file is deleted immediately)
- ❌ Any data is sent to external services (all processing is local)

---

## Data Storage

All persistent data is stored in a **local SQLite file** (`violations.db` by default). This file:

- Resides on the server where the bot is running
- Is not encrypted at rest (consider filesystem-level encryption for sensitive deployments)
- Should be excluded from version control (already included in `.gitignore`)
- Contains only integer user IDs — never personally identifiable names or content

---

## Media Retention

When NSFW content is detected, the flagged media is saved to disk:

- **Images:** `flagged_images/user_{user_id}_{timestamp}.jpg`
- **Videos/GIFs:** `flagged_videos/user_{user_id}_{timestamp}.mp4` or `.gif`

These files are retained **indefinitely** until the operator manually deletes them. Operators are responsible for:

1. Establishing a retention policy appropriate for their jurisdiction.
2. Regularly purging old flagged media.
3. Securing the directories from unauthorized access (file system permissions).

The `flagged_images/` and `flagged_videos/` directories are excluded from git via `.gitignore`.

**Example cleanup script:**
```bash
# Delete flagged images older than 30 days
find flagged_images/ -name "*.jpg" -mtime +30 -delete
find flagged_videos/ -name "*.mp4" -mtime +30 -delete
```

---

## Credentials and Secrets

| Secret | Handling |
|---|---|
| `BOT_TOKEN` | Loaded from `.env` only; never hard-coded; `.env` is git-ignored |
| `ADMIN_IDS` | Same as above |
| `DASHBOARD_SECRET_KEY` | Same as above; auto-generated securely with `os.urandom(24).hex()` if omitted |

**Best practices:**
- Never commit `.env` to version control.
- Use strong, random values for `DASHBOARD_SECRET_KEY`.
- Rotate the `BOT_TOKEN` immediately if it is ever accidentally exposed (via @BotFather → `/revoke`).
- Restrict file permissions on `.env`: `chmod 600 .env`

---

## Dashboard Security

The Flask dashboard (`dashboard.py`) is a **read-only** interface:

- No write endpoints are exposed — all `/api/*` routes return data only.
- The dashboard does not authenticate users by default — **do not expose it to the public internet without adding authentication**.
- For production deployments, consider:
  - Running behind a reverse proxy (nginx/Caddy) with HTTPS
  - Adding HTTP Basic Auth at the reverse proxy level
  - Binding to `127.0.0.1` only (the default for Flask in debug mode)
  - Using a VPN or SSH tunnel for remote access

---

## Telegram API Compliance

A.R.T.E.M.I.S.S. operates exclusively through the official Telegram Bot API and adheres to:

- [Telegram Terms of Service](https://telegram.org/tos)
- [Telegram Bot API Terms](https://core.telegram.org/bots/api)
- [Telegram Privacy Policy](https://telegram.org/privacy)

The bot:
- Only processes media sent to groups where it has been explicitly added as an administrator.
- Does not access messages in groups where it is not a member.
- Does not store message text content.
- Does not forward media to any external service — all ML inference is performed locally.

---

## Recommendations for Operators

If you are deploying this bot in a Telegram group, consider informing your members:

1. That automated moderation is active and images/videos are scanned for NSFW content.
2. That flagged content may be temporarily cached for admin review.
3. What the violation threshold is and what consequences violations carry.

Transparency with your community is both ethically sound and may be required under applicable data protection regulations (e.g., GDPR in the EU).

---

## Data Deletion

### Delete a user's violation record

```bash
# Using the bot command
/admin_reset <user_id>

# Or directly in SQLite
sqlite3 violations.db "DELETE FROM violations WHERE user_id = <user_id>;"
sqlite3 violations.db "DELETE FROM actions WHERE user_id = <user_id>;"
```

### Delete all moderation data

```bash
# Full reset — deletes all data but preserves table structure
sqlite3 violations.db "DELETE FROM violations;"
sqlite3 violations.db "DELETE FROM actions;"
sqlite3 violations.db "DELETE FROM contents;"
sqlite3 violations.db "UPDATE stats SET value = 0;"
```

### Delete flagged media for a specific user

```bash
# Remove all cached media for user ID 123456789
rm flagged_images/user_123456789_*.jpg
rm flagged_videos/user_123456789_*.mp4
rm flagged_videos/user_123456789_*.gif
```

### Full deletion

```bash
rm violations.db
rm -rf flagged_images/ flagged_videos/
```
