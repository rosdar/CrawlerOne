from crawler.fetcher import fetch_url, get_first_30_entries
from crawler.filters import (
    filter_long_titles_by_number_comments_asc,
    filter_short_titles_by_points_asc,
)

BASE_URL = "https://news.ycombinator.com"

def main() -> None:
    url = BASE_URL
    response = fetch_url(url)
    entries = get_first_30_entries(response.text)

    while True:
        print("Choose an option:")
        print("1 - Refresh fetch the HackerNews entries")
        print("2 - Show the entries")
        print("3 - Filter by long titles and number of comments")
        print("4 - Filter by short titles and points")
        print("5 - Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            response = fetch_url(url)
            entries = get_first_30_entries(response.text)
            print("Entries fetched successfully.")
        elif choice == "2":
            for entry in entries:
                print(entry)
        elif choice == "3":
            filtered_entries = filter_long_titles_by_number_comments_asc(entries)
            for entry in filtered_entries:
                print(entry)
        elif choice == "4":
            filtered_entries = filter_short_titles_by_points_asc(entries)
            for entry in filtered_entries:
                print(entry)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
