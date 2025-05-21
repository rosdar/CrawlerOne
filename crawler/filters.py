import re

from crawler.models.entry import Entry


def filter_short_title_entries_with_rest(entries: list[Entry]) -> tuple[list[Entry], list[Entry]]:
    filtered_entries: list[Entry] = []
    rest_of_entries: list[Entry] = []

    for entry in entries:
        title_words = re.findall(r'\b[\w-]+\b', entry.title)
        word_count = len(title_words)

        if word_count <= 5:
            filtered_entries.append(entry)
        else:
            rest_of_entries.append(entry)

    return filtered_entries, rest_of_entries


def order_by_number_comments_asc(entries: list[Entry]) -> list[Entry]:
    return sorted(entries, key=lambda e: e.number_comments, reverse=False)


def order_by_points_asc(entries: list[Entry]) -> list[Entry]:
    return sorted(entries, key=lambda e: e.points, reverse=False)


def filter_long_titles_by_number_comments_asc(entries: list[Entry]) -> list[Entry]:
    long_title_entries: list[Entry] = filter_short_title_entries_with_rest(entries)[1]
    return order_by_number_comments_asc(long_title_entries)


def filter_short_titles_by_points_asc(entries: list[Entry]) -> list[Entry]:
    short_title_entries: list[Entry] = filter_short_title_entries_with_rest(entries)[0]
    return order_by_points_asc(short_title_entries)
