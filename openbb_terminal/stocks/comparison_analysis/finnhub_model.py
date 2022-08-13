"""Finnhub model"""
__docformat__ = "numpy"

import logging
from typing import List, Tuple

import requests

from openbb_terminal import config_terminal as cfg
from openbb_terminal.decorators import log_start_end
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


@log_start_end(log=logger)
def get_similar_companies(symbol: str) -> Tuple[List[str], str]:
    """Get similar companies from Finhub

    Parameters
    ----------
    symbol : str
        Ticker to find comparisons for

    Returns
    -------
    List[str]
        List of similar companies
    str
        String containing data source
    """

    response = requests.get(
        f"https://finnhub.io/api/v1/stock/peers?symbol={symbol}&token={cfg.API_FINNHUB_KEY}"
    )

    similar = []
    user = "Error"

    if response.status_code == 200:
        similar = response.json()
        user = "Finnhub"

        if not similar:
            console.print("Similar companies not found.")
    elif response.status_code == 401:
        console.print("[red]Invalid API Key[/red]\n")
    elif response.status_code == 403:
        console.print("[red]API Key not authorized for Premium Feature[/red]\n")
    else:
        console.print(f"Error in request: {response.json()['error']}", "\n")

    return similar, user
