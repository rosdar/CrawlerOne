from crawler.fetcher import fetch_url


async def test_fetch_valid_url() -> None:
    url = "https://news.ycombinator.com"
    content = await fetch_url(url)
    assert "Hacker News" in content
