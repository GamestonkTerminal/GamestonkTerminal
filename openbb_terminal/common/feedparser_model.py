""" Feedparser Model """
__docformat__ = "numpy"

import feedparser
import pandas as pd
from openbb_terminal.rich_config import console


def get_news(
    term: str,
    sources: str = "bloomberg.com",
) -> pd.DataFrame:
    """Get news for a given term and source. [Source: Feedparser]

    Parameters
    ----------
    term : str
        term to search on the news articles
    sources: str
        sources to exclusively show news from

    Returns
    ----------
    articles : dict
        term to search on the news articles
    """
    have_data = False
    console.print("[yellow]Fetching data. Please be patient\n[/yellow]")
    limit = 0
    while not have_data:
        if term:
            if sources:
                data = feedparser.parse(
                    f"https://news.google.com/rss/search?q={term}&hl=en-US&gl=US&ceid=US:en&when:24h+allinurl"
                    f':{sources.replace(" ", "%20")}'
                )
            else:
                data = feedparser.parse(
                    f"https://news.google.com/rss/search?q={term}&when:24h&hl=en-US&gl=US&ceid=US:en"
                )
        else:
            if sources:
                data = feedparser.parse(
                    f'https://news.google.com/rss/search?q=when:24h+allinurl:{sources.replace(" ", "%20")}'
                    "&hl=en-US&gl=US&ceid=US:en"
                )
            else:
                data = feedparser.parse(
                    "https://news.google.com/rss/search?q=when:24h&hl=en-US&gl=US&ceid=US:en"
                )

        if data.status == 200:  # Checking if data request succeeded
            if data.entries:
                have_data = True

            elif limit == 60:  # Breaking if 60 successful requests return no data
                console.print("[red]Timeout occurred. Please try again\n[/red")
                break
            limit = limit + 1

        elif data.status != 200:  # If data request failed
            console.print("[red]Status code not 200. Unable to retrieve data\n[/red]")
            break

    return pd.DataFrame(data.entries, columns=["title", "link", "published"])
