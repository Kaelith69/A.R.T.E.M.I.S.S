# Roadmap

This page documents the planned feature development for A.R.T.E.M.I.S.S., organized by release milestone.

---

## Table of Contents

- [Current State (v1.0)](#current-state-v10)
- [v1.1 — Enhanced Detection](#v11--enhanced-detection)
- [v1.2 — Operator Controls](#v12--operator-controls)
- [v2.0 — Production Readiness](#v20--production-readiness)
- [Long-Term Vision](#long-term-vision)
- [How to Contribute to the Roadmap](#how-to-contribute-to-the-roadmap)

---

## Current State (v1.0)

The following features are implemented and stable in the current release:

| Feature | Status | Notes |
|---|---|---|
| Image NSFW detection | ✅ Released | Falconsai ViT model via HuggingFace pipeline |
| Video frame analysis | ✅ Released | OpenCV 6-frame sampling with early exit |
| GIF / animation moderation | ✅ Released | Treated as video with same pipeline |
| SQLite violation tracking | ✅ Released | Persists across restarts |
| Configurable violation threshold | ✅ Released | `FLAG_THRESHOLD` env var |
| Auto-ban enforcement | ✅ Released | With chat owner protection |
| Admin notifications + media forwarding | ✅ Released | All `ADMIN_IDS` notified |
| Evidence caching | ✅ Released | Timestamped files in configurable dirs |
| Admin commands | ✅ Released | `admin_flagged`, `admin_reset`, `admin_ban` |
| User commands | ✅ Released | `start`, `help`, `violations`, `stats` |
| Real-time Flask dashboard | ✅ Released | Socket.IO + 5 Chart.js charts |
| GPU acceleration support | ✅ Released | Auto-detected CUDA |
| Environment variable configuration | ✅ Released | python-dotenv |
| Full audit log | ✅ Released | `actions` table with timestamps |

---

## v1.1 — Enhanced Detection

**Theme:** Broaden the types of content that can be moderated.

| Feature | Priority | Description |
|---|---|---|
| **Text spam detection** | High | NLP-based classifier to detect repetitive, spammy, or abusive text messages. Planned model: fine-tuned DistilBERT or a rule-based system as fallback. |
| **Escalating ban timers** | High | Instead of permanent ban on first threshold breach, implement progressive timeouts: 1 minute → 5 minutes → 1 hour → permanent. Configurable via environment variables. |
| **Configurable frame count** | Medium | Make `num_frames` and `nsfw_threshold` configurable via environment variables without source code modification. |
| **Sticker moderation** | Medium | Add `filters.Sticker` handler to scan animated and static stickers for NSFW content. |
| **Rate limiting** | Low | Prevent users from flooding the bot with media to cause denial-of-service through inference overload. |

---

## v1.2 — Operator Controls

**Theme:** Give group administrators more fine-grained control without editing source code.

| Feature | Priority | Description |
|---|---|---|
| **`/setthreshold <n>` command** | High | Allow admins to change `FLAG_THRESHOLD` at runtime without restarting the bot. Value persisted in the database. |
| **`/setstats reset` command** | Medium | Allow admins to reset all aggregate statistics counters. |
| **Per-user violation history** | Medium | `/admin_history <user_id>` command showing timestamped list of all past violations for a user. |
| **Whitelist command** | Medium | `/admin_whitelist <user_id>` to exempt specific users from NSFW scanning (e.g., trusted admins). |
| **PostgreSQL backend option** | Low | Optional switch from SQLite to PostgreSQL for high-traffic deployments. Connection string via `DATABASE_URL` env var. |
| **Dashboard authentication** | Low | Optional HTTP Basic Auth for the Flask dashboard to prevent unauthorized access when exposed on a network. |

---

## v2.0 — Production Readiness

**Theme:** Make the bot suitable for large-scale, multi-group production deployments.

| Feature | Priority | Description |
|---|---|---|
| **Webhook mode** | High | Replace `run_polling()` with `run_webhook()` for lower latency and better scalability in production environments. |
| **Docker + Docker Compose** | High | Official `Dockerfile` and `docker-compose.yml` for containerised deployment. Includes bot + dashboard + optional PostgreSQL. |
| **Multi-group configuration** | High | Per-group settings stored in the database: different thresholds, different admin IDs, enable/disable specific modules per group. |
| **Health check endpoint** | Medium | `/health` route in `dashboard.py` returning bot status, uptime, and last processed event — for monitoring systems (Prometheus, Uptime Robot, etc.). |
| **Async database access** | Medium | Replace synchronous `sqlite3` calls with `aiosqlite` to prevent blocking the asyncio event loop during high traffic. |
| **Log rotation** | Low | Structured JSON logging with configurable rotation to prevent unbounded log growth. |
| **CI/CD pipeline** | Low | GitHub Actions workflow for linting (flake8), type checking (mypy), and packaging. |

---

## Long-Term Vision

These are exploratory ideas that may or may not be implemented, depending on community interest and maintainer capacity:

| Idea | Description |
|---|---|
| **Multi-model ensemble** | Combine multiple NSFW classifiers and use a voting mechanism for higher accuracy. |
| **Custom model fine-tuning guide** | Documentation and scripts for fine-tuning the ViT model on custom datasets to adapt to specific community standards. |
| **Telegram Mini App dashboard** | Move the admin dashboard from a web browser into a Telegram Mini App for in-app access. |
| **Cross-group ban sharing** | Optional network of trusted bot operators who share ban lists for repeat offenders across multiple communities. |
| **Audit log export** | One-click CSV/PDF export of the full audit log from the dashboard. |
| **Scheduled reports** | Automatic weekly/monthly moderation summary sent to admin Telegram IDs. |

---

## How to Contribute to the Roadmap

1. **Open an issue** to propose or discuss a roadmap item.
2. **Comment on existing issues** to vote for features or share implementation ideas.
3. **Submit a pull request** if you have implemented a roadmap feature — reference the relevant issue in your PR description.

See [Contributing](Contributing.md) for the full contributor guide.
