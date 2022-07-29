"""Twitter Model"""
__docformat__ = "numpy"

import logging
from typing import Optional

import pandas as pd
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from openbb_terminal import config_terminal as cfg
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import clean_tweet, get_data
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)

analyzer = SentimentIntensityAnalyzer()


@log_start_end(log=logger)
def load_analyze_tweets(
    symbol: str,
    limit: int = 100,
    start_date: Optional[str] = "",
    end_date: Optional[str] = "",
) -> pd.DataFrame:
    """Load tweets from twitter API and analyzes using VADER

    Parameters
    ----------
    symbol: str
        Ticker symbol to search twitter for
    limit: int
        Number of tweets to analyze
    start_date: Optional[str]
        If given, the start time to get tweets from
    end_date: Optional[str]
        If given, the end time to get tweets from

    Returns
    -------
    df_tweet: pd.DataFrame
        Dataframe of tweets and sentiment
    """
    params = {
        "query": rf"(\${symbol}) (lang:en)",
        "max_results": str(limit),
        "tweet.fields": "created_at,lang",
    }

    if start_date:
        # Assign from and to datetime parameters for the API
        params["start_time"] = start_date
    if end_date:
        params["end_time"] = end_date

    # Request Twitter API
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/recent",
        params=params,  # type: ignore
        headers={"authorization": "Bearer " + cfg.API_TWITTER_BEARER_TOKEN},
    )

    # Create dataframe
    df_tweets = pd.DataFrame()

    # Check that the API response was successful
    if response.status_code == 200:
        for tweet in response.json()["data"]:
            row = get_data(tweet)
            df_tweets = df_tweets.append(row, ignore_index=True)
    elif response.status_code == 401:
        console.print("Twitter API Key provided is incorrect\n")
        return pd.DataFrame()
    elif response.status_code == 400:
        console.print(
            """
            Status Code 400.
            This means you are requesting data from beyond the API's 7 day limit"""
        )
        return pd.DataFrame()
    elif response.status_code == 403:
        console.print(
            f"""
            Status code 403.
            It seems you're twitter credentials are invalid - {response.text}
        """
        )
        return pd.DataFrame()
    else:
        console.print(
            f"""
            Status code {response.status_code}.
            Something went wrong - {response.text}
        """
        )
        return pd.DataFrame()

    sentiments = []
    pos = []
    neg = []
    neu = []

    for s_tweet in df_tweets["text"].to_list():
        tweet = clean_tweet(s_tweet, symbol)
        sentiments.append(analyzer.polarity_scores(tweet)["compound"])
        pos.append(analyzer.polarity_scores(tweet)["pos"])
        neg.append(analyzer.polarity_scores(tweet)["neg"])
        neu.append(analyzer.polarity_scores(tweet)["neu"])
    # Add sentiments to tweets dataframe
    df_tweets["sentiment"] = sentiments
    df_tweets["positive"] = pos
    df_tweets["negative"] = neg
    df_tweets["neutral"] = neu

    return df_tweets
