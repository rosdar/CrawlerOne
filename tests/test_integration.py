from pathlib import Path

import pytest

from crawler.main import fetch
from crawler.models.entry import Entry
from crawler.storage import clear_db, get_all_logs, init_db

DB_PATH = Path("test.db")


def db_path() -> Path:
    return DB_PATH


@pytest.mark.integration
def test_full_pipeline() -> None:

    clear_db(db_path())
    init_db(db_path())

    entries = fetch("https://news.ycombinator.com")

    assert isinstance(entries, list)
    assert all(isinstance(entry, Entry) for entry in entries)
    assert len(entries) <= 30

    from crawler.main import user_menu_filter_long_comments
    user_menu_filter_long_comments(entries, db_path())

    logs = get_all_logs(db_path())
    assert len(logs) == 1
    assert logs[0][2] == "filter_long_titles_by_number_comments_asc"

    clear_db(db_path())
