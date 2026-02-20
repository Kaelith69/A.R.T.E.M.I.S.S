import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

DB_FILE = os.environ.get("DB_FILE", "violations.db")

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Violations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS violations (
            user_id INTEGER PRIMARY KEY,
            count INTEGER
        )
    ''')

    # Stats table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stats (
            key TEXT PRIMARY KEY,
            value INTEGER
        )
    ''')

    # Actions table (matches artemis_bot.py schema)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS actions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            action TEXT,
            timestamp TEXT
        )
    ''')

    # Contents table (tracks type and NSFW flag for dashboard)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT,
            is_nsfw INTEGER
        )
    ''')

    # Insert initial stats if not already present
    initial_stats = [
        ('total_contents_scanned', 0),
        ('total_nsfw_detected', 0),
        ('total_sfw', 0),
        ('total_users_banned', 0),
        ('total_violations', 0),
    ]
    cursor.executemany(
        'INSERT OR IGNORE INTO stats (key, value) VALUES (?, ?)',
        initial_stats,
    )

    conn.commit()
    conn.close()
    print(f"Database '{DB_FILE}' initialised successfully.")

if __name__ == '__main__':
    setup_database()
