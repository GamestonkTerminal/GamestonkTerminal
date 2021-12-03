"""BitQuery model"""
__docformat__ = "numpy"

import datetime
import json
from typing import Optional

from requests.exceptions import HTTPError
from requests.adapters import HTTPAdapter

import requests
import pandas as pd
from gamestonk_terminal import config_terminal as cfg


class BitQueryApiKeyException(Exception):
    """Bit Query Api Key Exception object"""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"BitQueryApiKeyException: {self.message}"


BQ_URL = "https://graphql.bitquery.io"
CURRENCIES = ["ETH", "USD", "BTC", "USDT"]
DECENTRALIZED_EXCHANGES = [
    "1inch",
    "1inch Liquidity Protocol",
    "AfroDex",
    "Air Swap",
    "AirSwap",
    "Amplbitcratic",
    "Balancer",
    "Bamboo Relay",
    "Bancor Network",
    "BestSwap",
    "Bitox",
    "CRO DeFi Swap",
    "CellSwap",
    "Cellswap",
    "Cofix",
    "Coinchangex",
    "Cream Pool Token",
    "Curve",
    "DDEX",
    "DUBIex",
    "DecentrEx",
    "DeversiFi",
    "Dodo",
    "ERC dEX",
    "ETHERCExchange",
    "EtherBlockchain",
    "EtherDelta",
    "Ethernext",
    "Ethfinex",
    "FEGex",
    "FFFSwap",
    "Fordex",
    "GUDecks",
    "GUDeks",
    "HiSwap",
    "Hydro Hybrid Exchange",
    "IDEX",
    "Kyber Network",
    "LedgerDex",
    "Matcha",
    "Miniswap",
    "Mooniswap",
    "Oasis",
    "OpenRelay",
    "Radar Relay",
    "S.Finance",
    "SakeSwap",
    "SeedDex",
    "Shark Relay",
    "SingularX",
    "StarBitEx",
    "SushiSwap",
    "SwapX",
    "SwitchDex",
    "TacoSwap",
    "The Ocean",
    "TokenJar",
    "TokenStore",
    "TokenTrove",
    "Tokenlon",
    "TradexOne",
    "Uniswap",
    "Zerox Exchange",
    "ZeusSwap",
    "dYdX",
    "dex.blue",
]
NETWORKS = ["bsc", "ethereum", "matic"]
ERC20_TOKENS = None


def query_graph(url: str, query: str) -> dict:
    """Helper methods for querying graphql api. [Source: https://bitquery.io/]

    Parameters
    ----------
    url: str
        Endpoint url
    query: str
        Graphql query

    Returns
    -------
    dict:
        Dictionary with response data
    """

    session = requests.Session()
    session.mount("http://", HTTPAdapter(max_retries=5))
    headers = {"x-api-key": cfg.API_BITQUERY_KEY}

    response = session.post(url, json={"query": query}, headers=headers)

    if response.status_code == 500:
        raise HTTPError(f"Internal sever error {response.reason}")

    if not 200 <= response.status_code < 300:
        raise BitQueryApiKeyException(
            f"Invalid Authentication: {response.status_code}. "
            f"Please visit https://bitquery.io/pricing and generate you free api key"
        )
    try:
        data = response.json()
        if "error" in data:
            raise ValueError(f"Invalid Response: {data['error']}")
    except Exception as e:
        raise ValueError(f"Invalid Response: {response.text}") from e
    return data["data"]


def get_erc20_tokens() -> pd.DataFrame:
    """Helper method that loads ~1500 most traded erc20 token.
    [Source: json file]

    Returns
    -------
    pd.DataFrame
        ERC20 tokens with address, symbol and name
    """

    with open("../data/erc20_coins.json") as f:
        data = json.load(f)
    df = pd.json_normalize(data)
    df.columns = ["count", "address", "symbol", "name"]
    return df[["name", "symbol", "address", "count"]]


def find_token_address(token: str) -> Optional[str]:
    """Helper methods that search for ERC20 coin base on provided symbol or token address.
    If erc20 token address is provided, then function checks if it's proper address and returns it back.
    In other case mapping data is loaded from file (or cache), and function lookup for belonging token address.

    Parameters
    ----------
    token: str
        ERC20 token symbol e.g. UNI, SUSHI, ETH, WBTC or token address e.g. 0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48

    Returns
    -------
    str or None
        ERC20 token address, or None if nothing found.
    """

    if token.startswith("0x") and len(token) >= 38:
        return token
    token = token.upper()

    if token == "ETH":
        return token

    token = "WBTC" if token == "BTC" else token

    tokens_map: pd.DataFrame = ERC20_TOKENS or get_erc20_tokens()

    found_token = tokens_map.loc[tokens_map["symbol"] == token]
    if found_token.empty:
        return None
    if len(found_token) > 1:
        return found_token.sort_values(by="count", ascending=False).iloc[0]["address"]
    return found_token.iloc[0]["address"]


def get_dex_trades_by_exchange(
    trade_amount_currency: str = "USD", limit: int = 90
) -> pd.DataFrame:
    """Get trades on Decentralized Exchanges aggregated by DEX [Source: https://graphql.bitquery.io/]

    Parameters
    ----------
    trade_amount_currency: str
        Currency of displayed trade amount. Default: USD
    limit:  int
        Last n days to query data. Maximum 365 (bigger numbers can cause timeouts
        on server side)

    Returns
    -------
    pd.DataFrame
        Trades on Decentralized Exchanges aggregated by DEX
    """

    dt = (datetime.date.today() - datetime.timedelta(min(limit, 365))).strftime(
        "%Y-%m-%d"
    )

    if trade_amount_currency not in CURRENCIES:
        trade_amount_currency = "USD"

    query = f"""
            {{
          ethereum {{
            dexTrades(options: {{limit: 40, desc: ["count"]}}
             date: {{since: "{dt}"}}
            ) {{
              exchange {{
              name
            }}
              count
              tradeAmount(in: {trade_amount_currency})
            }}
          }}
        }}
        """

    data = query_graph(BQ_URL, query)

    dex_trades = data["ethereum"]["dexTrades"]
    if not dex_trades:
        raise ValueError(f"List of dex trades is empty {data['ethereum']}")
    df = pd.json_normalize(dex_trades)
    df.columns = ["trades", "tradeAmount", "exchange"]
    return df[["exchange", "trades", "tradeAmount"]].sort_values(
        by="tradeAmount", ascending=True
    )


def get_dex_trades_monthly(
    trade_amount_currency: str = "USD", limit: int = 90
) -> pd.DataFrame:
    """Get list of trades on Decentralized Exchanges monthly aggregated. [Source: https://graphql.bitquery.io/]

    Parameters
    ----------
    trade_amount_currency: str
        Currency of displayed trade amount. Default: USD
    limit:  int
        Last n days to query data. Maximum 365 (bigger numbers can cause timeouts
        on server side)

    Returns
    -------
    pd.DataFrame
        Trades on Decentralized Exchanges monthly aggregated
    """

    if trade_amount_currency not in CURRENCIES:
        trade_amount_currency = "USD"

    dt = (datetime.date.today() - datetime.timedelta(min(limit, 365))).strftime(
        "%Y-%m-%d"
    )

    query = f"""
        {{
          ethereum {{
            dexTrades(
              options: {{desc: ["date.year", "date.month", "count"]}}
              date: {{since: "{dt}"}}
            ) {{
              count
              date {{
                month
                year
              }}
              tradeAmount(in: {trade_amount_currency})
            }}
          }}
        }}
        """

    data = query_graph(BQ_URL, query)
    if not data:
        return pd.DataFrame()

    dex_trades = data["ethereum"]["dexTrades"]
    if not dex_trades:
        raise ValueError(f"List of dex trades is empty {data['ethereum']}")
    df = pd.json_normalize(dex_trades)
    df["date"] = df.apply(
        lambda x: datetime.date(int(x["date.year"]), int(x["date.month"]), 1), axis=1
    )
    return df[["date", "count", "tradeAmount"]]


def get_daily_dex_volume_for_given_pair(
    limit: int = 100,
    token: str = "UNI",
    vs: str = "USDT",
) -> pd.DataFrame:
    """Get daily volume for given pair [Source: https://graphql.bitquery.io/]

    Parameters
    -------
    limit:  int
        Last n days to query data
    token: str
        ERC20 token symbol
    vs: str
        Quoted currency.

    Returns
    -------
    pd.DataFrame
         Daily volume for given pair
    """

    dt = (datetime.date.today() - datetime.timedelta(min(limit, 365))).strftime(
        "%Y-%m-%d"
    )

    base, quote = find_token_address(token), find_token_address(vs)
    if not base or not quote:
        return pd.DataFrame()

    query = f"""
         {{
          ethereum(network: ethereum) {{
            dexTrades(
              options: {{desc: ["timeInterval.day", "trades"]}}
              baseCurrency: {{is: "{base}"}}
              quoteCurrency: {{is: "{quote}"}}
              date: {{since: "{dt}" }}
            ) {{
              timeInterval {{
                day(count: 1)
              }}
              baseCurrency {{
                symbol
              }}
              quoteCurrency {{
                symbol
              }}
              exchange {{
                fullName
              }}
              trades: count
              tradeAmount(in: USD)
              quotePrice
              maximum_price: quotePrice(calculate: maximum)
              minimum_price: quotePrice(calculate: minimum)
              open_price: minimum(of: block, get: quote_price)
              close_price: maximum(of: block, get: quote_price)
            }}
          }}
        }}
        """

    data = query_graph(BQ_URL, query)
    if not data:
        return pd.DataFrame()

    df = pd.json_normalize(data["ethereum"]["dexTrades"])
    df.columns = [
        "trades",
        "tradeAmountUSD",
        "price",
        "high",
        "low",
        "open",
        "close",
        "date",
        "base",
        "quote",
        "exchange",
    ]
    return df[
        [
            "date",
            "exchange",
            "base",
            "quote",
            "open",
            "high",
            "low",
            "close",
            "tradeAmountUSD",
            "trades",
        ]
    ].sort_values(by="date", ascending=False)


def get_token_volume_on_dexes(
    token: str = "UNI",
    trade_amount_currency: str = "USD",
) -> pd.DataFrame:
    """Get token volume on different Decentralized Exchanges. [Source: https://graphql.bitquery.io/]

    Parameters
    ----------
    token: str
        ERC20 token symbol.
    trade_amount_currency: str
        Currency to display trade amount in.

    Returns
    -------
    pd.DataFrame
        Token volume on Decentralized Exchanges
    """

    if trade_amount_currency not in CURRENCIES:
        trade_amount_currency = "USD"

    token_address = find_token_address(token)
    query = f"""
        {{
           ethereum {{
            dexTrades(
              baseCurrency: {{is:"{token_address}"}}
            ) {{
                  baseCurrency{{
        symbol
      }}
              exchange {{
              name
              fullName
              }}
              count
              tradeAmount(in: {trade_amount_currency})

            }}
            }}
            }}

        """

    data = query_graph(BQ_URL, query)
    if not data:
        return pd.DataFrame()

    df = pd.json_normalize(data["ethereum"]["dexTrades"])[
        ["exchange.fullName", "baseCurrency.symbol", "tradeAmount", "count"]
    ]
    df.columns = ["exchange", "coin", "tradeAmount", "trades"]
    return df[~df["exchange"].str.startswith("<")].sort_values(
        by="tradeAmount", ascending=False
    )


def get_ethereum_unique_senders(interval: str = "day", limit: int = 90) -> pd.DataFrame:
    """Get number of unique ethereum addresses which made a transaction in given time interval.

    Parameters
    ----------
    interval: str
        Time interval in which count unique ethereum addresses which made transaction. day, month or week.
    limit: int
        Number of records for data query.

    Returns
    -------
    pd.DataFrame
        Unique ethereum addresses which made a transaction
    """

    intervals = {
        "day": 1,
        "month": 30,
        "week": 7,
    }

    if interval not in intervals.keys():
        interval = "day"

    days = min(limit * intervals[interval], 90)

    dt = (datetime.date.today() - datetime.timedelta(days)).strftime("%Y-%m-%d")

    query = f"""
     {{
          ethereum(network: ethereum) {{
            transactions(options: {{desc: "date.date"}}, date: {{since: "{dt}"}}) {{
              uniqueSenders: count(uniq: senders)
              date {{
                date:startOfInterval(unit: {interval})
              }}
                avgGasPrice: gasPrice(calculate: average)
                  medGasPrice: gasPrice(calculate: median)
                  maxGasPrice: gasPrice(calculate: maximum)
                  transactions: count
            }}
          }}
        }}
        """

    data = query_graph(BQ_URL, query)
    if not data:
        return pd.DataFrame()

    df = pd.DataFrame(data["ethereum"]["transactions"])
    df["date"] = df["date"].apply(lambda x: x["date"])
    return df[
        [
            "date",
            "uniqueSenders",
            "transactions",
            "avgGasPrice",
            "medGasPrice",
            "maxGasPrice",
        ]
    ]


def get_most_traded_pairs(
    network: str = "ethereum", exchange: str = "Uniswap", limit: int = 90
) -> pd.DataFrame:
    """Get most traded crypto pairs on given decentralized exchange in chosen time period.
    [Source: https://graphql.bitquery.io/]

    Parameters
    ----------
    network: str
        EVM network. One from list: bsc (binance smart chain), ethereum or matic
    exchange:
        Decentralized exchange name
    limit:
        Number of days taken into calculation account.

    Returns
    -------

    """

    dt = (datetime.date.today() - datetime.timedelta(limit)).strftime("%Y-%m-%d")
    query = f"""
    {{
    ethereum(network: {network}){{
    dexTrades(options: {{limit: 100, desc: "tradeAmount"}},
      exchangeName: {{is: "{exchange}"}}
      date: {{since: "{dt}"}}) {{
      buyCurrency {{
        symbol
      }}
      sellCurrency{{
        symbol
      }}
      trades: count
      tradeAmount(in: USD)
    }}
    }}
    }}
    """
    data = query_graph(BQ_URL, query)
    if not data:
        return pd.DataFrame()

    df = pd.json_normalize(data["ethereum"]["dexTrades"])
    df.columns = ["trades", "tradeAmount", "base", "quoted"]
    return df[["base", "quoted", "trades", "tradeAmount"]]


def get_spread_for_crypto_pair(
    token: str = "WETH", vs: str = "USDT", limit: int = 30
) -> pd.DataFrame:
    """Get an average bid and ask prices, average spread for given crypto pair for chosen time period.
       [Source: https://graphql.bitquery.io/]

    Parameters
    ----------
    limit:  int
        Last n days to query data
    token: str
        ERC20 token symbol
    vs: str
        Quoted currency.

    Returns
    -------
    pd.DataFrame
       Average bid and ask prices, spread for given crypto pair for chosen time period
    """

    dt = (datetime.date.today() - datetime.timedelta(limit)).strftime("%Y-%m-%d")
    base, quote = find_token_address(token), find_token_address(vs)

    if not base or not quote:
        return pd.DataFrame()

    query = f"""
        {{
      ethereum(network: ethereum){{
      dexTrades(
          date: {{since:"{dt}"}}
          baseCurrency: {{is: "{base}"}},
          quoteCurrency: {{is: "{quote}"}}) {{
          date {{date}}
          baseCurrency {{symbol}}
          baseAmount
          quoteCurrency {{
            symbol
          }}
          quoteAmount
          trades: count
          quotePrice
          side
        }}
      }}
    }}
    """
    data = query_graph(BQ_URL, query)
    if not data:
        return pd.DataFrame()

    df = pd.json_normalize(data["ethereum"]["dexTrades"])

    columns = ["quotePrice", "date.date", "baseCurrency.symbol", "quoteCurrency.symbol"]
    bids = df.query("side == 'SELL'")[columns]
    asks = df.query("side == 'BUY'")[columns]

    bids.columns = ["averageBidPrice", "date", "baseCurrency", "quoteCurrency"]
    asks.columns = ["averageAskPrice", "date", "baseCurrency", "quoteCurrency"]

    daily_spread = pd.merge(asks, bids, on=["date", "baseCurrency", "quoteCurrency"])
    daily_spread["dailySpread"] = abs(
        daily_spread["averageBidPrice"] - daily_spread["averageAskPrice"]
    )
    return daily_spread[
        [
            "date",
            "baseCurrency",
            "quoteCurrency",
            "dailySpread",
            "averageBidPrice",
            "averageAskPrice",
        ]
    ].sort_values(by="date", ascending=True)
