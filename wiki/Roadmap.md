# Roadmap

Planned features, versioning strategy, and the long-term vision for A.R.T.E.M.I.S.S.

---

## Current Status: v0.1.0

The bot works. NSFW images, videos, and GIFs are detected and handled. Violations are tracked. Admins are notified. The dashboard shows live stats. That's the foundation.

Everything on this page is a "would be nice" sorted by priority and grouped into milestones.

---

## v0.2 — Better Moderation

**Text Spam Detection**
- NLP-based classifier for repetitive or spammy text messages
- Original blueprint included this — it just hasn't been implemented yet
- Timer-based mute escalation (mute 1 min → mute 2 min → ban) instead of immediate ban

**Configurable Ban Escalation**
- Current behavior: warn → warn → ban (at threshold)
- Planned: configurable actions per violation level (warn, mute, kick, ban)
- Per-chat configuration would be ideal but is complex — v0.2 may just be global config

**Improved Logging**
- More granular action types in the `actions` table
- Separate tracking for "message deleted" vs "user warned" vs "user banned"

---

## v0.3 — Multi-Group Support

**Per-Group Configuration**
- Currently: one global `FLAG_THRESHOLD`, one set of `ADMIN_IDS`
- Planned: per-chat settings stored in the database
- Each group could have its own threshold, its own admin list, and its own enabled modules

**Dashboard Authentication**
- The dashboard currently has no auth — it's LAN-only for good reason
- v0.3 will add at minimum a simple password or API key requirement
- Longer term: proper session-based auth

---

## v0.4 — More Media Types

**Sticker NSFW Detection**
- Telegram stickers can contain inappropriate content
- Static stickers → treat like images
- Animated stickers (TGS/WebM) → frame extraction similar to video

**Document/File Detection**
- Images sent as documents (not compressed) bypass the current photo handler
- Needs a separate handler for `filters.Document` with image MIME types

---

## v0.5 — Stability and Operations

**Rate Limiting / Flood Protection**
- A user could theoretically spam images faster than the bot can process them
- Need a per-user cooldown or processing queue

**Persistent Model Cache Validation**
- Verify the cached model on startup to detect corrupted downloads
- Graceful re-download if needed

**Health Check Endpoint**
- Simple `/health` endpoint on the dashboard to use with uptime monitors

---

## v1.0 — Production Ready

**Docker Compose Deployment**
- Single `docker-compose.yml` to spin up bot + dashboard
- Environment variables passed securely
- Volume mounts for `violations.db` and flagged media directories

**Documentation**
- Complete installation guide for Docker
- Example reverse proxy configuration (nginx) for the dashboard

**Test Suite**
- Unit tests for violation logic, DB operations, and media routing
- Mock Telegram API for integration tests
- CI pipeline on GitHub Actions

---

## Ideas Under Consideration

These might happen, might not. No timeline.

- **Audio/voice message analysis** — flagging inappropriate voice content
- **URL/link detection** — identifying spam or phishing links
- **Reporting system** — users can report a message to admins for manual review
- **Whitelist system** — trusted users exempt from content scanning
- **Dry-run mode** — bot logs what it *would* do without actually deleting/banning
- **Web-based admin panel** — manage violations and settings via dashboard (not just view)
- **Webhook mode** — alternative to long-polling for lower latency on high-traffic groups

---

## What's NOT on the Roadmap

- **Cloud SaaS version** — this is intentionally self-hosted
- **Paying for ML APIs** — all inference stays local
- **Monetization** — it's MIT licensed, do what you want

---

## Contributing to the Roadmap

If you want to build something from this list, open an issue first so we can discuss the approach before you spend a weekend on it. PRs for roadmap items are very welcome — see [CONTRIBUTING.md](../CONTRIBUTING.md).
