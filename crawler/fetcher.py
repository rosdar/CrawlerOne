import asyncio

import httpx


async def fetch_url(url: str) -> str:

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        print(response.text)
        return str(response.text)


def main() -> None:

    url = input("Enter a URL to fetch: ")
    asyncio.run(fetch_url(url))


if __name__ == "__main__":

    main()
