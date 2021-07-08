__docformat__ = "numpy"
import os
import argparse
from typing import List
import pandas as pd
from gamestonk_terminal.helper_funcs import (
    parse_known_args_and_warn,
)
from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.behavioural_analysis.finbrain_view import (
    get_sentiment,
    plot_sentiment,
    sentiment_coloring,
)


PATH = os.path.dirname(os.path.abspath(__file__))
COINS_JSON = pd.read_json(PATH + "/finbrain_coins.json")
COINS = COINS_JSON["SYMBOL"].tolist()


def crypto_sentiment_analysis(other_args: List[str]):
    """Sentiment analysis from FinBrain for Cryptocurrencies

    Parameters
    ----------
    other_args : List[str]
        Command line arguments to be processed with argparse

    """
    parser = argparse.ArgumentParser(
        prog="finbrain",
        add_help=False,
        description="""FinBrain collects the news headlines from 15+ major financial news
                    sources on a daily basis and analyzes them to generate sentiment scores
                    for more than 4500 US stocks. FinBrain Technologies develops deep learning
                    algorithms for financial analysis and prediction, which currently serves
                    traders from more than 150 countries all around the world.
                    [Source:  https://finbrain.tech]""",
    )

    parser.add_argument(
        "-c",
        "--coin",
        default="BTC",
        type=str,
        dest="coin",
        help="Symbol of coin to load data for. Currently more then 100 symbols are available",
        choices=COINS,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        coin = ns_parser.coin

        df_sentiment = get_sentiment(
            f"{coin}-USD"
        )  # Currently only USD pairs are available

        if not df_sentiment.empty:
            plot_sentiment(df_sentiment, coin)

        df_sentiment.sort_index(ascending=True, inplace=True)

        if gtff.USE_COLOR:
            print(
                df_sentiment["Sentiment Analysis"]
                .apply(sentiment_coloring, last_val=0)
                .to_string()
            )
        else:
            print(df_sentiment.to_string())
        print("")

    except Exception as e:
        print(e)
        print("")
