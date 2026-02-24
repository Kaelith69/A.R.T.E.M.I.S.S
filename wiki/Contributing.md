# Contributing

Thank you for your interest in contributing to A.R.T.E.M.I.S.S.! This guide covers everything you need to set up a development environment, understand the codebase, and submit a high-quality pull request.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Environment Setup](#development-environment-setup)
- [Project Structure](#project-structure)
- [Coding Conventions](#coding-conventions)
- [Making Changes](#making-changes)
- [Testing Your Changes](#testing-your-changes)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Issue Guidelines](#issue-guidelines)
- [Architecture Decisions](#architecture-decisions)

---

## Code of Conduct

By participating in this project, you agree to maintain a respectful and constructive environment. Harassment, discriminatory language, or personal attacks will not be tolerated.

---

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally.
3. Follow the [Development Environment Setup](#development-environment-setup) section.
4. Look for issues labelled `good first issue` or `help wanted`.
5. **Open an issue** before starting major work to discuss the approach.

---

## Development Environment Setup

```bash
# Clone your fork
git clone https://github.com/<your-username>/A.R.T.E.M.I.S.S.git
cd A.R.T.E.M.I.S.S

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install development tools
pip install flake8 black isort

# Set up test configuration
cp .env.example .env
# Set a test BOT_TOKEN and ADMIN_IDS in .env
# You can use a dedicated test bot from @BotFather

# Initialise the test database
python setup_db.py
```

---

## Project Structure

```
A.R.T.E.M.I.S.S/
├── artemis_bot.py       # Core bot — all main logic lives here
├── dashboard.py         # Flask dashboard — separate from bot
├── setup_db.py          # DB init script
├── templates/
│   └── index.html       # Dashboard SPA
├── wiki/                # Documentation
├── .env.example         # Config template
├── requirements.txt     # Runtime dependencies
└── blueprint.md         # Original design blueprint
```

Key design principle: **all bot logic lives in `artemis_bot.py`**. The dashboard is intentionally separate and reads the database independently.

---

## Coding Conventions

### Python Style

- Follow **PEP 8** — use `flake8` to check.
- Use **Black** for auto-formatting (line length: 88).
- Use **isort** for import ordering.

```bash
black artemis_bot.py dashboard.py setup_db.py
isort artemis_bot.py dashboard.py setup_db.py
flake8 artemis_bot.py dashboard.py setup_db.py
```

### Type Hints

Use type hints for all function signatures:

```python
# Good
def get_violation_count(user_id: int) -> int:
    ...

# Bad
def get_violation_count(user_id):
    ...
```

### Async Handlers

All Telegram handlers are `async` — keep them non-blocking. Do not use `time.sleep()` inside async functions; use `await asyncio.sleep()` instead.

### Database Access

Each database function opens and closes its own connection:

```python
def my_db_function(user_id: int) -> int:
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # ... query ...
    conn.close()
    return result
```

Do not share connections across function calls.

### Logging

Use the module-level logger for all diagnostic output:

```python
logger.info("Processed image for user %s", user_id)
logger.warning("NSFW detected: user %s, violation %d", user_id, count)
logger.error("Failed to ban user %s: %s", user_id, str(e))
```

Do not use `print()` statements.

### Environment Variables

All configurable values must be loaded from environment variables with sensible defaults:

```python
MY_SETTING = int(os.environ.get("MY_SETTING", "42"))
```

Never hard-code tokens, IDs, or paths.

---

## Making Changes

### Adding a New Bot Command

1. Write the handler function in `artemis_bot.py`:

```python
async def my_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Admin gate if needed:
    user = update.message.from_user
    if user.id not in ADMIN_IDS:
        await update.message.reply_text("❌ Not authorized.")
        return
    # ... your logic ...
    await update.message.reply_text("Done.")
```

2. Register it in `main()`:

```python
application.add_handler(CommandHandler("my_command", my_command))
```

3. Update `/help` text in `help_command()`.

### Adding a New Database Table

1. Add `CREATE TABLE IF NOT EXISTS ...` to both `init_db()` in `artemis_bot.py` **and** `setup_database()` in `setup_db.py` — they must stay in sync.

2. Add corresponding helper functions following the existing pattern.

### Adding Dashboard Endpoints

Add new routes to `dashboard.py` following the existing pattern:

```python
@app.route('/api/my_data')
def api_my_data():
    conn = get_db_connection()
    rows = conn.execute('SELECT … FROM …').fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])
```

All dashboard routes must be **read-only** (GET only, no mutations).

### Adding New Environment Variables

1. Add the variable to `.env.example` with a comment explaining it.
2. Load it in the appropriate module with a sensible default.
3. Document it in the [README Configuration Reference](../README.md#-configuration-reference).

---

## Testing Your Changes

There is no automated test suite at this time. Test your changes manually:

### Bot Changes

1. Set up a private test Telegram group.
2. Add your dev bot as admin.
3. Send test images and videos to verify detection behaviour.
4. Test all affected commands in the group and in private chat with the bot.

### Dashboard Changes

1. Run `python dashboard.py`.
2. Open `http://localhost:5000`.
3. Verify charts render correctly.
4. Test Socket.IO updates by leaving the page open and triggering a bot action.

### Database Schema Changes

1. Run `python setup_db.py` on a fresh `violations.db`.
2. Verify all tables are created correctly.
3. Test that the schema migration is backward-compatible if the DB already exists.

---

## Submitting a Pull Request

1. Create a feature branch from `main`:
   ```bash
   git checkout -b feature/my-feature
   ```

2. Make your changes following the conventions above.

3. Commit with a clear, imperative message:
   ```bash
   git commit -m "Add /setstats command for resetting all statistics"
   ```

4. Push to your fork:
   ```bash
   git push origin feature/my-feature
   ```

5. Open a Pull Request against the `main` branch of the upstream repository.

6. In the PR description, include:
   - **What** the change does
   - **Why** it is needed
   - **How** to test it
   - Any relevant screenshots or logs

---

## Issue Guidelines

### Bug Reports

Include:
- Python version (`python --version`)
- Full error traceback
- Steps to reproduce
- Expected vs. actual behaviour
- Relevant environment variables (redact sensitive values)

### Feature Requests

Include:
- The use case / problem being solved
- Proposed implementation approach (if known)
- Any trade-offs or concerns

---

## Architecture Decisions

Before making significant architectural changes, read the [Architecture](Architecture.md) page. Key design decisions to respect:

| Decision | Rationale |
|---|---|
| Module-level model singleton | Avoid multi-second reload on every message |
| SQLite (not PostgreSQL) | Zero-dependency deployment for small groups |
| Bot and dashboard are separate processes | Dashboard failure does not affect moderation |
| Read-only dashboard | Prevents accidental or malicious data modification |
| No ORM | Keeps dependencies minimal; SQLite queries are simple |
| Environment variables for all config | 12-factor app principle; no secrets in source |
