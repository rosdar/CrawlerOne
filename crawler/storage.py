import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("crawler.db")

def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usage_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                filter TEXT NOT NULL
            );
        """)

def log_request(filter_name: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO usage_log (timestamp, filter) VALUES (?, ?)",
            (datetime.now().isoformat(), filter_name),
        )

def get_all_logs() -> list[tuple[int, str, str]]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT * FROM usage_log")
        return cursor.fetchall()

def clear_db() -> None:
    DB_PATH.unlink(missing_ok=True)
