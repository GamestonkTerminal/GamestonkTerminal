""" News View """
__docformat__ = "numpy"

import requests

from gamestonk_terminal import config_terminal as cfg


def news(term: str, num: int, s_from: str):
    """Display news for a given title. [Source: NewsAPI]

    Parameters
    ----------
    term : str
        term to search on the news articles
    num : int
        number of articles to display
    s_from: str
        date to start searching articles from formatted YYYY-MM-DD
    """
    # TODO: Add argument to specify news source being used

    response = requests.get(
        f"https://newsapi.org/v2/everything?q={term}&from={s_from}"
        f"&sortBy=publishedAt&language=en&apiKey={cfg.API_NEWS_TOKEN}",
    )

    # Check that the API response was successful
    if response.status_code != 200:
        print(f"Error in request {response.status_code}. Check News API token", "\n")

    else:
        print(
            f"{response.json()['totalResults']} news articles for {term} were found since {s_from}\n"
        )

        for idx, article in enumerate(response.json()["articles"]):
            print(
                article["publishedAt"].replace("T", " ").replace("Z", ""),
                " ",
                article["title"],
            )
            # Unnecessary to use name of the source because contained in link article["source"]["name"]
            print(article["url"], "\n")

            if idx >= num - 1:
                break
