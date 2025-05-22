import sqlite3
from datetime import datetime
from pathlib import Path


def init_db(db_path: Path) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usage_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                filter TEXT NOT NULL
            );
        """)

def log_request(filter_name: str, db_path: Path) -> None:
    with sqlite3.connect(db_path) as conn:
        conn.execute(
            "INSERT INTO usage_log (timestamp, filter) VALUES (?, ?)",
            (datetime.now().isoformat(), filter_name),
        )

def get_all_logs(db_path: Path) -> list[tuple[int, str, str]]:
    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute("SELECT * FROM usage_log")
        return cursor.fetchall()

def clear_db(db_path: Path) -> None:
    db_path.unlink(missing_ok=True)
