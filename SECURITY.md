# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.1.x   | ✅ Yes     |
| < 0.1   | ❌ No      |

Only the latest release receives security fixes. If you're running something older — please update.

---

## Reporting a Vulnerability

Found a security issue? Don't post it in a public issue. Seriously. That's how you accidentally help the wrong people.

### What to do

1. **Email the maintainer directly** — check the GitHub profile for contact info, or use GitHub's private vulnerability reporting feature (Security → Report a vulnerability on this repo page).
2. **Include as much detail as you can:**
   - Description of the issue
   - Steps to reproduce
   - Potential impact (what can an attacker do with this?)
   - Suggested fix if you have one
3. **Give us a reasonable window** — we'll acknowledge within 5 business days and aim to release a fix within 30 days for critical issues, depending on severity and complexity.

We'll keep you updated as we work on a fix, and we'll credit you in the CHANGELOG and release notes unless you'd prefer to stay anonymous.

---

## What Counts as a Security Issue

Things we definitely want to hear about:

- **Bot token or admin ID exposure** — if they can be leaked from the application
- **Admin command bypass** — if a non-admin can execute admin-only commands
- **Path traversal in media caching** — if filenames can be manipulated to write outside the intended directories
- **SQLite injection** — the code uses parameterized queries, but if you find a gap, tell us
- **Denial of service** — if someone can crash or hang the bot with a crafted message
- **Dashboard exposure** — the dashboard currently has no authentication; if running on a public-facing server, that's a known risk and intentional (for now — see Roadmap)

Things that are known and accepted:

- **Dashboard lacks authentication** — it's a v0.1 limitation. Don't expose it to the public internet. Bind to localhost or use a reverse proxy with auth.
- **Flagged media stored locally** — this is by design. It's stored for admin review. Secure your server.
- **Model confidence threshold is 50%** — false positive/negative rate is a product decision, not a vulnerability.

---

## Security Design Notes

- All configuration is loaded via environment variables or `.env` file — never hardcoded
- Media is processed locally; no data is sent to external services (the model runs on your machine)
- Parameterized SQL queries throughout — no string concatenation in database operations
- Temp files are cleaned up after classification (SFW) or renamed to a structured path (NSFW)
- The bot validates that `BOT_TOKEN` is set before starting — it won't silently run without credentials
- `ADMIN_IDS` is loaded from env — if unset, a warning is emitted at startup

---

## Responsible Disclosure

We're a small open-source project. We'll handle reports in good faith, and we ask for the same in return.

If you act in good faith:
- We won't take legal action
- We'll credit you for the discovery
- We'll fix it as fast as we reasonably can

Thank you for helping keep A.R.T.E.M.I.S.S. trustworthy. 🛡️
