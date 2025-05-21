import json
from pathlib import Path

from crawler.models.entry import Entry

FIXTURES_PATH = Path(__file__).parent / "fixtures"


def load_html_fixture() -> str:
    return _load_fixture("hackernews_sample.html")


def load_html_empty_fixture() -> str:
    return _load_fixture("hackernews_empty_sample.html")


def load_all_entries_fixture() -> list[Entry]:
    return _load_entries_fixture("hackernews_entries.json")


def load_sample_entries_fixture() -> list[Entry]:
    return _load_entries_fixture("sample_entries.json")


def load_sample_entries_filter_long_comments_fixture() -> list[Entry]:
    return _load_entries_fixture("sample_entries_filter_long_comments.json")


def load_sample_entries_filter_short_points_fixture() -> list[Entry]:
    return _load_entries_fixture("sample_entries_filter_short_points.json")


def _load_entries_fixture(filename: str) -> list[Entry]:
    data = _load_fixture(filename)
    entries_data = json.loads(data)
    return [Entry(**entry) for entry in entries_data]


def _load_fixture(filename: str) -> str:
    return (FIXTURES_PATH / filename).read_text(encoding="utf-8")
