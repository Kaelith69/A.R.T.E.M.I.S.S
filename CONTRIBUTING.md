# Contributing to A.R.T.E.M.I.S.S. 🛡️

First of all — thanks for wanting to help. You didn't have to. You could be doing literally anything else right now. We appreciate you.

This document covers how to get set up for development, how we handle branches and commits, and what makes a pull request worth reviewing.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Branching Model](#branching-model)
- [Commit Style](#commit-style)
- [Pull Requests](#pull-requests)
- [Code Style](#code-style)
- [What to Work On](#what-to-work-on)
- [What NOT to Do](#what-not-to-do)

---

## Getting Started

Before anything else, please:

1. **Fork the repo** — don't push directly to `main`
2. **Read the README** — understand what the project actually does
3. **Check open issues** — someone might already be working on your idea

If you're picking up an issue, drop a comment so we know you're on it.

---

## Development Setup

```bash
# Fork then clone your fork
git clone https://github.com/YOUR_USERNAME/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S

# Create a virtual environment (please, for the love of all things holy)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your test config
cp .env.example .env
# Fill in BOT_TOKEN and ADMIN_IDS — use a separate dev/test bot from BotFather
# Don't use your production bot token in development. That's how you cause incidents.

# Init the database
python setup_db.py
```

> ⚠️ The Falconsai ViT model downloads ~350MB on first run. This is expected. Have patience. Have coffee.

---

## Branching Model

We use a simple feature-branch workflow:

```
main                  ← stable, production-ready
  └── feature/your-feature-name    ← your work goes here
  └── fix/short-description-of-bug
  └── docs/what-you-are-documenting
  └── refactor/what-you-are-cleaning-up
```

**Rules:**
- Never commit directly to `main`
- Branch off `main` when starting a new feature or fix
- Keep branches focused — one feature per branch
- Delete your branch after it's merged

```bash
# Start a new feature
git checkout main
git pull origin main
git checkout -b feature/text-spam-detection

# When done, push and open a PR
git push origin feature/text-spam-detection
```

---

## Commit Style

We follow [Conventional Commits](https://www.conventionalcommits.org/) — loosely. The general idea:

```
<type>: <short description>

[optional body explaining WHY, not just what]
```

### Types

| Type | Use when |
|---|---|
| `feat` | Adding a new feature |
| `fix` | Fixing a bug |
| `docs` | Documentation changes only |
| `refactor` | Code changes that don't add features or fix bugs |
| `test` | Adding or fixing tests |
| `chore` | Build process, dependency updates, etc. |
| `style` | Formatting only — no logic changes |

### Examples

```
feat: add text spam detection handler

fix: handle BadRequest when deleting already-deleted messages

docs: update installation guide for Windows

refactor: extract violation threshold logic into helper function

chore: bump python-telegram-bot to 21.3
```

**Don'ts:**
- `fix stuff` ← what stuff? be a human
- `WIP` ← that's not a commit message, that's a cry for help
- `asdfgh` ← genuinely baffling

---

## Pull Requests

When opening a PR:

1. **Fill in the PR template** (or at minimum explain what changed and why)
2. **Link the related issue** if there is one — `Closes #42`
3. **Keep it focused** — a PR that touches 12 unrelated files will get stuck in review forever
4. **Test your changes** — ideally with an actual Telegram bot in a test group
5. **Don't break existing behavior** — if the bot stops working after your PR, that's a problem

### PR Title Format

Follow the same pattern as commits:

```
feat: add configurable confidence threshold per chat
fix: prevent crash when video file is empty
```

### Review Process

- At least one maintainer will review your PR
- Be responsive to feedback — we're not monsters, but we do care about code quality
- If you disagree with feedback, say so respectfully — debate is fine, ghosts are not

---

## Code Style

- **Python 3.10+** — use modern features (match/case, union types with `|`, etc.)
- **Type hints** — new functions should have type annotations
- **Async handlers** — all Telegram handlers must be `async`
- **Logging** — use the `logger` instance, not `print()` (unless it's `setup_db.py`)
- **Environment variables** — all configuration through `.env` / `os.environ`, never hardcoded
- **No bare `except:`** — catch specific exceptions and handle them properly

We don't have a linter enforced in CI right now, but we read the code and we do notice.

---

## What to Work On

Good first issues:
- Improving error messages
- Documentation corrections
- Fixing edge cases in the video frame analyzer
- Tests (we have none, it's fine, everything is fine 🔥)

Meatier contributions:
- Text spam detection module (see `blueprint.md`)
- Dashboard authentication
- Per-group configuration support
- Docker Compose setup

If you're unsure whether your idea fits the project, open an issue and ask before spending 3 hours on it.

---

## What NOT to Do

- Don't add dependencies without a discussion — `requirements.txt` bloat is real
- Don't change the ML model without benchmarking the replacement
- Don't expose sensitive data (bot tokens, user IDs) in commits or logs
- Don't submit PRs that only add blank lines or fix whitespace — that's not helping
- Don't store user-identifying info beyond what's already in the schema

---

Thanks again. PRs welcome. Issues welcome. Questions welcome. Unsolicited NSFW content, however, will be handled by the bot.

🛡️
