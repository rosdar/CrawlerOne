import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from requests import RequestException, Response

from crawler.models.entry import Entry


def fetch_url(url: str) -> Response:

    try:
        response: Response = requests.get(url)
        response.raise_for_status()
        return response
    except RequestException as e:
        # Handle/log if needed
        raise e


def get_first_30_entries(content: str) -> list[Entry]:

    soup = BeautifulSoup(content, 'html.parser')
    entries: list[Entry] = []

    # Extract ranks, titles, points, and comments
    for item in soup.find_all('tr', class_='athing submission'):

        rank_tag: Tag = item.find('span', class_='rank')
        title_tag: Tag = item.find('span', class_='titleline').find_all('a')[0]
        subtext: Tag = item.find_next_sibling('tr').find('td', class_='subtext')

        if rank_tag and title_tag and subtext:

            points_tag: Tag | NavigableString | None = subtext.find('span', class_='score')
            comments_tag: Tag = subtext.find_all('a')[-1]

            rank: int = int(rank_tag.text.strip('.'))
            title: str = title_tag.text
            points: int = int(points_tag.text.split()[0]) if points_tag else 0
            number_comments = int(comments_tag.text.split()[0]) if comments_tag and 'comment' in comments_tag.text else 0

            entries.append(Entry(rank=rank, title=title, points=points, number_comments=number_comments))

    if len(entries) == 0:
        raise ValueError("No entries found!")

    return entries[:30]
