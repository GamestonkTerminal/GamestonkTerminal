""" Business Insider Model """
__docformat__ = "numpy"

import requests
import pandas as pd
from bs4 import BeautifulSoup
from gamestonk_terminal.helper_funcs import get_user_agent


def get_insider_activity(ticker: str) -> pd.DataFrame:
    """Get insider activity. [Source: Business Insider]

    Parameters
    ----------
    ticker : str
        Ticker to get insider activity data from

    Returns
    -------
    df_insider : pd.DataFrame
        Get insider activity data
    """
    url_market_business_insider = (
        f"https://markets.businessinsider.com/stocks/{ticker.lower()}-stock"
    )
    text_soup_market_business_insider = BeautifulSoup(
        requests.get(
            url_market_business_insider, headers={"User-Agent": get_user_agent()}
        ).text,
        "lxml",
    )

    d_insider = dict()
    l_insider_vals = list()
    for idx, insider_val in enumerate(
        text_soup_market_business_insider.findAll(
            "td", {"class": "table__td text-center"}
        )
    ):
        l_insider_vals.append(insider_val.text.strip())

        # Add value to dictionary
        if (idx + 1) % 6 == 0:
            # Check if we are still parsing insider trading activity
            if "/" not in l_insider_vals[0]:
                break
            d_insider[(idx + 1) // 6] = l_insider_vals
            l_insider_vals = list()

    df_insider = pd.DataFrame.from_dict(
        d_insider,
        orient="index",
        columns=["Date", "Shares Traded", "Shares Held", "Price", "Type", "Option"],
    )

    df_insider["Date"] = pd.to_datetime(df_insider["Date"])
    df_insider = df_insider.set_index("Date")
    df_insider = df_insider.sort_index(ascending=True)

    l_names = list()
    for s_name in text_soup_market_business_insider.findAll(
        "a", {"onclick": "silentTrackPI()"}
    ):
        l_names.append(s_name.text.strip())
    df_insider["Insider"] = l_names

    return df_insider
