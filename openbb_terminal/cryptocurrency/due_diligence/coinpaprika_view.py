"""CoinPaprika view"""
__docformat__ = "numpy"

import logging
import os

from pandas.plotting import register_matplotlib_converters

from openbb_terminal.cryptocurrency.dataframe_helpers import (
    lambda_long_number_format_with_type_check,
)
from openbb_terminal.cryptocurrency.due_diligence import coinpaprika_model
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import export_data, print_rich_table
from openbb_terminal.rich_config import console
from openbb_terminal.cryptocurrency import cryptocurrency_helpers

logger = logging.getLogger(__name__)

register_matplotlib_converters()

# pylint: disable=inconsistent-return-statements
# pylint: disable=C0302, too-many-lines

TWEETS_FILTERS = ["date", "user_name", "status", "retweet_count", "like_count"]

EVENTS_FILTERS = ["date", "date_to", "name", "description", "is_conference"]

EX_FILTERS = ["id", "name", "adjusted_volume_24h_share", "fiats"]

MARKET_FILTERS = [
    "pct_volume_share",
    "exchange",
    "pair",
    "trust_score",
    "volume",
    "price",
]

CURRENCIES = [
    "BTC",
    "ETH",
    "USD",
    "EUR",
    "PLN",
    "KRW",
    "GBP",
    "CAD",
    "JPY",
    "RUB",
    "TRY",
    "NZD",
    "AUD",
    "CHF",
    "UAH",
    "HKD",
    "SGD",
    "NGN",
    "PHP",
    "MXN",
    "BRL",
    "THB",
    "CLP",
    "CNY",
    "CZK",
    "DKK",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "MYR",
    "NOK",
    "PKR",
    "SEK",
    "TWD",
    "ZAR",
    "VND",
    "BOB",
    "COP",
    "PEN",
    "ARS",
    "ISK",
]


@log_start_end(log=logger)
def display_twitter(
    symbol: str = "BTC",
    limit: int = 10,
    sortby: str = "date",
    ascending: bool = True,
    export: str = "",
) -> None:
    """Get twitter timeline for given coin id. Not more than last 50 tweets [Source: CoinPaprika]

    Parameters
    ----------
    symbol: str
        Cryptocurrency symbol (e.g. BTC)
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data. Every column name is valid
        (see for possible values:
        https://api.coinpaprika.com/docs#tag/Coins/paths/~1coins~1%7Bcoin_id%7D~1twitter/get).
    ascending: bool
        Flag to sort data ascending
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    # get coinpaprika id using crypto symbol
    cp_id = cryptocurrency_helpers.get_coinpaprika_id(symbol)

    df = coinpaprika_model.get_coin_twitter_timeline(cp_id, sortby, ascending)

    if df.empty:
        console.print(f"Couldn't find any tweets for coin {symbol}", "\n")
        return

    print_rich_table(
        df.head(limit),
        headers=list(df.columns),
        show_index=False,
        title="Twitter Timeline",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "twitter",
        df,
    )


@log_start_end(log=logger)
def display_events(
    symbol: str = "BTC",
    limit: int = 10,
    sortby: str = "date",
    ascending: bool = False,
    links: bool = False,
    export: str = "",
) -> None:
    """Get all events for given coin id. [Source: CoinPaprika]

    Parameters
    ----------
    symbol: str
        Cryptocurrency symbol (e.g. BTC)
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data. Every column name is valid
        (see for possible values:
        https://api.coinpaprika.com/docs#tag/Coins/paths/~1coins~1%7Bcoin_id%7D~1events/get).
    ascending: bool
        Flag to sort data ascending
    links: bool
        Flag to display urls
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    # get coinpaprika id using crypto symbol
    cp_id = cryptocurrency_helpers.get_coinpaprika_id(symbol)

    df = coinpaprika_model.get_coin_events_by_id(cp_id, sortby, ascending)

    if df.empty:
        console.print(f"Couldn't find any events for coin {symbol}\n")
        return

    df_data = df.copy()

    if links is True:
        df = df[["date", "name", "link"]]
    else:
        df.drop("link", axis=1, inplace=True)

    print_rich_table(
        df.head(limit), headers=list(df.columns), show_index=False, title="All Events"
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "events",
        df_data,
    )


@log_start_end(log=logger)
def display_exchanges(
    symbol: str = "btc",
    limit: int = 10,
    sortby: str = "adjusted_volume_24h_share",
    ascending: bool = True,
    export: str = "",
) -> None:
    """Get all exchanges for given coin id. [Source: CoinPaprika]

    Parameters
    ----------
    symbol: str
        Cryptocurrency symbol (e.g. BTC)
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data. Every column name is valid (see for possible values:
        https://api.coinpaprika.com/v1).
    ascending: bool
        Flag to sort data ascending
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    # get coinpaprika id using crypto symbol
    cp_id = cryptocurrency_helpers.get_coinpaprika_id(symbol)

    df = coinpaprika_model.get_coin_exchanges_by_id(cp_id, sortby, ascending)

    if df.empty:
        console.print("No data found", "\n")
        return

    print_rich_table(
        df.head(limit),
        headers=list(df.columns),
        show_index=False,
        title="All Exchanges",
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ex",
        df,
    )


@log_start_end(log=logger)
def display_markets(
    from_symbol: str = "BTC",
    to_symbol: str = "USD",
    limit: int = 20,
    sortby: str = "pct_volume_share",
    ascending: bool = True,
    links: bool = False,
    export: str = "",
) -> None:
    """Get all markets for given coin id. [Source: CoinPaprika]

    Parameters
    ----------
    from_symbol: str
        Cryptocurrency symbol (e.g. BTC)
    to_symbol: str
        Quoted currency
    limit: int
        Number of records to display
    sortby: str
        Key by which to sort data. Every column name is valid (see for possible values:
        https://api.coinpaprika.com/v1).
    ascending: bool
        Flag to sort data ascending
    links: bool
        Flag to display urls
    export : str
        Export dataframe data to csv,json,xlsx file
    """

    if sortby in ["volume", "price"]:
        sortby = f"{str(to_symbol).lower()}_{sortby}"

    # get coinpaprika id using crypto symbol
    cp_id = cryptocurrency_helpers.get_coinpaprika_id(from_symbol)

    df = coinpaprika_model.get_coin_markets_by_id(cp_id, to_symbol, sortby, ascending)

    if df.empty:
        console.print("There is no data \n")
        return

    df_data = df.copy()

    if links is True:
        df = df[["exchange", "pair", "trust_score", "market_url"]]
    else:
        df.drop("market_url", axis=1, inplace=True)

    print_rich_table(
        df.head(limit), headers=list(df.columns), show_index=False, title="All Markets"
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "mkt",
        df_data,
    )


@log_start_end(log=logger)
def display_price_supply(
    from_symbol: str = "BTC",
    to_symbol: str = "USD",
    export: str = "",
) -> None:
    """Get ticker information for single coin [Source: CoinPaprika]

    Parameters
    ----------
    from_symbol: str
        Cryptocurrency symbol (e.g. BTC)
    to_symbol: str
        Quoted currency
    export: str
        Export dataframe data to csv,json,xlsx

    """
    # get coinpaprika id using crypto symbol
    cp_id = cryptocurrency_helpers.get_coinpaprika_id(from_symbol)

    df = coinpaprika_model.get_tickers_info_for_coin(cp_id, to_symbol)

    if df.empty:
        console.print("No data found", "\n")
        return

    df = df.applymap(lambda x: lambda_long_number_format_with_type_check(x))

    print_rich_table(
        df, headers=list(df.columns), show_index=False, title="Coin Information"
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "ps",
        df,
    )


@log_start_end(log=logger)
def display_basic(
    symbol: str = "BTC",
    export: str = "",
) -> None:
    """Get basic information for coin. Like:
        name, symbol, rank, type, description, platform, proof_type, contract, tags, parent.
        [Source: CoinPaprika]

    Parameters
    ----------
    symbol: str
        Cryptocurrency symbol (e.g. BTC)
    export: str
        Export dataframe data to csv,json,xlsx
    """
    # get coinpaprika id using crypto symbol
    cp_id = cryptocurrency_helpers.get_coinpaprika_id(symbol)

    df = coinpaprika_model.basic_coin_info(cp_id)

    if df.empty:
        console.print("No data available\n")
        return

    print_rich_table(
        df, headers=list(df.columns), show_index=False, title="Basic Coin Information"
    )

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "basic",
        df,
    )
