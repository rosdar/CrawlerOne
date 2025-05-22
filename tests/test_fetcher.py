from unittest.mock import Mock, patch

import pytest
from requests.exceptions import HTTPError

from crawler.fetcher import fetch_url, get_first_30_entries
from tests.conftest import load_html_empty_fixture, load_html_fixture


@pytest.mark.unit
def test_fetch_url_success() -> None:
    mock_response = Mock()
    mock_response.text = "fake content"
    mock_response.raise_for_status = Mock()

    with patch("crawler.fetcher.requests.get", return_value=mock_response) as mock_get:
        result = fetch_url("https://example.com")

    mock_get.assert_called_once_with("https://example.com")
    mock_response.raise_for_status.assert_called_once()
    assert result.text == "fake content"


@pytest.mark.unit
def test_fetch_url_raises_on_http_error() -> None:
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = HTTPError("Boom!")

    with patch("crawler.fetcher.requests.get", return_value=mock_response):
        with pytest.raises(HTTPError):
            fetch_url("https://example.com")


@pytest.mark.unit
def test_get_first_30_entries_success() -> None:
    html = load_html_fixture()
    entries = get_first_30_entries(html)

    assert len(entries) == 30
    for entry in entries:
        assert isinstance(entry.rank, int)
        assert isinstance(entry.title, str)
        assert isinstance(entry.points, int)
        assert isinstance(entry.number_comments, int)
        assert entry.rank > 0
        assert entry.title != ""


@pytest.mark.unit
def test_get_first_30_entries_no_entries() -> None:
    html = load_html_empty_fixture()
    with pytest.raises(ValueError, match="No entries found!"):
        get_first_30_entries(html)
