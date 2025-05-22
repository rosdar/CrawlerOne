import pytest

from crawler.filters import (
    filter_long_titles_by_number_comments_asc,
    filter_short_title_entries_with_rest,
    filter_short_titles_by_points_asc,
)
from crawler.models.entry import Entry
from tests.conftest import (
    load_sample_entries_filter_long_comments_fixture,
    load_sample_entries_filter_short_points_fixture,
    load_sample_entries_fixture,
)

# Filter all previous entries with more than five words in the title, ordered by the number of comments first.
# Filter all previous entries with less than or equal to five words in the title, ordered by points.


@pytest.mark.unit
def test_filter_title_short() -> None:
    filtered_entries: list[Entry] = filter_short_title_entries_with_rest(load_sample_entries_fixture())[0]
    titles = [entry.title for entry in filtered_entries]

    assert len(filtered_entries) == 3

    assert "" in titles
    assert "Short title" in titles
    assert "This is - a self-explained example" in titles


@pytest.mark.unit
def test_filter_long_titles_by_number_comments_asc() -> None:
    filtered_sample: list[Entry] = filter_long_titles_by_number_comments_asc(load_sample_entries_fixture())
    correct_sample: list[Entry] = load_sample_entries_filter_long_comments_fixture()


    assert filtered_sample[0].title == correct_sample[0].title
    assert filtered_sample[0].number_comments == correct_sample[0].number_comments

    assert filtered_sample[1].title == correct_sample[1].title
    assert filtered_sample[1].number_comments == correct_sample[1].number_comments

    assert filtered_sample[2].title == correct_sample[2].title
    assert filtered_sample[2].number_comments == correct_sample[2].number_comments


@pytest.mark.unit
def test_filter_short_titles_by_points_asc() -> None:
    filtered_sample: list[Entry] = filter_short_titles_by_points_asc(load_sample_entries_fixture())
    correct_sample: list[Entry] = load_sample_entries_filter_short_points_fixture()


    assert filtered_sample[0].title == correct_sample[0].title
    assert filtered_sample[0].points == correct_sample[0].points

    assert filtered_sample[1].title == correct_sample[1].title
    assert filtered_sample[1].points == correct_sample[1].points

    assert filtered_sample[2].title == correct_sample[2].title
    assert filtered_sample[2].points == correct_sample[2].points

# Not testing ordering because there's no added logic
