""" Finnhub Model """
__docformat__ = "numpy"

import logging

from datetime import datetime, timedelta
from typing import List, Dict
import finnhub
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from openbb_terminal import config_terminal as cfg
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import similar
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_company_news(
    symbol: str,
    start_date: str = (datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
    end_date: str = datetime.now().strftime("%Y-%m-%d"),
) -> List[Dict]:
    """Get news from a company. [Source: Finnhub]

    Parameters
    ----------
    symbol : str
        company ticker to look for news articles
    start_date: str
        date to start searching articles, with format YYYY-MM-DD
    end_date: str
        date to end searching articles, with format YYYY-MM-DD

    Returns
    ----------
    articles : List
        term to search on the news articles
    """
    try:
        finnhub_client = finnhub.Client(api_key=cfg.API_FINNHUB_KEY)
        articles = finnhub_client.company_news(symbol.upper(), _from=start_date, to=end_date)
        return articles

    except Exception as e:
        console.print(f"[red]{e}\n[/red]")
        return [{}]


@log_start_end(log=logger)
def process_news_headlines_sentiment(
    articles: List[Dict],
) -> pd.DataFrame:
    """Process news headlines sentiment of a company using a VADER model.

    Parameters
    ----------
    articles : List[Dict]
        list of articles with `headline` and `datetime` keys

    Returns
    ----------
    pd.DataFrame
        Headlines sentiment using VADER model over time
    """
    l_datetime = list()
    l_compound = list()

    if articles and len(articles) > 1:
        analyzer = SentimentIntensityAnalyzer()

        last_headline = ""
        for article in articles:
            # allows to discard news with similar headline
            if similar(last_headline, article["headline"].upper()) < 0.7:
                l_compound.append(
                    analyzer.polarity_scores(article["headline"])["compound"]
                )
                l_datetime.append(datetime.fromtimestamp(article["datetime"]))
                last_headline = article["headline"].upper()

    return pd.DataFrame(l_compound, index=l_datetime).sort_index()
