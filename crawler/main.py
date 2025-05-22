from pathlib import Path

from crawler.fetcher import fetch_url, get_first_30_entries
from crawler.filters import (
    filter_long_titles_by_number_comments_asc,
    filter_short_titles_by_points_asc,
)
from crawler.models.entry import Entry
from crawler.storage import clear_db, get_all_logs, init_db, log_request

BASE_URL = "https://news.ycombinator.com"
DB_PATH = Path("crawler.db")


def crawler_setup(db_path: Path) -> None:

    init_db(db_path)


def user_menu_print_options() -> None:

    print("------------------------------")
    print("Choose an option:")
    print("1 - Refresh fetch the HackerNews entries")
    print("2 - Show the entries")
    print("3 - Filter by long titles and number of comments")
    print("4 - Filter by short titles and points")
    print("5 - Show user logs")
    print("6 - Clear logs")
    print("7 - Quit\n")


def user_menu_clear_logs(db_path: Path) -> None:

    print("Clearing logs...")
    clear_db(db_path)
    init_db(db_path)
    print("Logs cleared.\n")


def user_menu_show_logs(db_path: Path) -> None:

    logs = get_all_logs(db_path)
    if len(logs) == 0:
        print("There are no logs yet for filters usage. Try using a filter.")
    else:
        for log in logs:
            print(f"Log ID: {log[0]}, timestamp: {log[1]}, filter option: {log[2]}")

    print()


def user_menu_filter_long_comments(entries: list[Entry], db_path: Path) -> None:

    log_request("filter_long_titles_by_number_comments_asc", db_path)
    filtered_entries = filter_long_titles_by_number_comments_asc(entries)
    user_menu_print_entries(filtered_entries)


def user_menu_filter_short_points(entries: list[Entry], db_path: Path) -> None:

    log_request("filter_short_titles_by_points_asc", db_path)
    filtered_entries = filter_short_titles_by_points_asc(entries)
    user_menu_print_entries(filtered_entries)


def user_menu_print_entries(entries: list[Entry]) -> None:

    for entry in entries:
        print(entry)

    print()


def fetch(url: str) -> list[Entry]:

    print("Fetching HackerNews entries...")
    response = fetch_url(url)
    entries = get_first_30_entries(response.text)
    print("Entries fetched successfully.\n")
    return entries


def main() -> None:

    db_path = DB_PATH

    crawler_setup(db_path)
    entries = fetch(BASE_URL)
    while True:

        user_menu_print_options()

        choice = input("Enter your choice: ")

        if choice == "1":
            entries = fetch(BASE_URL)

        elif choice == "2":
            user_menu_print_entries(entries)

        elif choice == "3":
            user_menu_filter_long_comments(entries, db_path)

        elif choice == "4":
            user_menu_filter_short_points(entries, db_path)

        elif choice == "5":
            user_menu_show_logs(db_path)

        elif choice == "6":
            user_menu_clear_logs(db_path)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

    print()

if __name__ == "__main__":
    main()
