""" pycoingecko_api """
__docformat__ = "numpy"

import argparse
from typing import List
from pandas.plotting import register_matplotlib_converters
import matplotlib.pyplot as plt
from tabulate import tabulate
from pycoingecko import CoinGeckoAPI
from gamestonk_terminal.helper_funcs import parse_known_args_and_warn, plot_autoscale
from gamestonk_terminal.config_plot import PLOT_DPI
import gamestonk_terminal.cryptocurrency.coingecko.pycoingecko_overview_model as gecko
import gamestonk_terminal.cryptocurrency.coingecko.pycoingecko_coin_model as gecko_coin
from gamestonk_terminal.cryptocurrency.cryptocurrency_helpers import wrap_text_in_df

register_matplotlib_converters()

# Generate a list of valid coins to be checked against later
cg_api = CoinGeckoAPI()
coins = cg_api.get_coins()

# pylint: disable=inconsistent-return-statements
# pylint: disable=R0904, C0302


def load(other_args: List[str]):
    """Load selected Cryptocurrency. You can pass either symbol of id of the coin

    Parameters
    ----------
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="load",
        description="""
                        Load Coin [CoinGecko]
                        """,
    )

    parser.add_argument(
        "-c",
        "--coin",
        required=True,
        type=str,
        dest="coin",
        help="Coin to load data for (symbol or coin id)",
    )

    try:
        if other_args:
            if "-" not in other_args[0]:
                other_args.insert(0, "-c")

        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        try:
            coin = gecko_coin.Coin(ns_parser.coin)
        except KeyError:
            print(f"Could not find coin with the id: {ns_parser.coin}")
            print("")
            return None

        print("")
        return coin

    except SystemExit:
        print("")
        return None

    except Exception as e:
        print(e)
        print("")
        return None


def chart(coin: gecko_coin.Coin, other_args: List[str]):
    """Plots chart for loaded cryptocurrency

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="chart",
        description="""
                        Display chart for loaded coin
                        """,
    )

    parser.add_argument(
        "--vs", default="usd", dest="vs", help="Currency to display vs coin"
    )

    parser.add_argument(
        "-d", "--days", default=30, dest="days", help="Number of days to get data for"
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.get_coin_market_chart(ns_parser.vs, ns_parser.days)
        plt.figure(figsize=plot_autoscale(), dpi=PLOT_DPI)

        plt.plot(df.index, df.price, "-ok", ms=2)
        plt.xlabel("Time")
        plt.xlim(df.index[0], df.index[-1])
        plt.ylabel("Price")
        plt.grid(b=True, which="major", color="#666666", linestyle="-")
        plt.minorticks_on()
        plt.grid(b=True, which="minor", color="#999999", linestyle="-", alpha=0.2)
        plt.title(f"{coin.coin_symbol}/{df['currency'][0]}")
        plt.show()
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def ta(coin: gecko_coin.Coin, other_args: List[str]):
    """Load data for Technical Analysis

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="ta",
        description="""
                        Loads data for technical analysis
                        """,
    )

    parser.add_argument(
        "--vs", default="usd", dest="vs", help="Currency to display vs coin"
    )

    parser.add_argument(
        "-d", "--days", default=30, dest="days", help="Number of days to get data for"
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.get_coin_market_chart(ns_parser.vs, ns_parser.days)
        return df

    except SystemExit:
        print("")
        return None

    except Exception as e:
        print(e)
        print("")
        return None


def info(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows basic information about loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="info",
        description="""
                        Shows basic information about loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = wrap_text_in_df(coin.base_info, w=80)
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def web(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows found websites corresponding to loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="web",
        description="""
                        Websites found for given Coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.websites
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def social(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows social media corresponding to loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="social",
        description="""
                        Shows social media corresponding to loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.social_media
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def dev(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows developers data for loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="dev",
        description="""
                       Developers data for loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.developers_data
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def ath(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows all time high data for loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="ath",
        description="""
                        All time high data for loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.all_time_high
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def atl(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows all time low data for loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="atl",
        description="""
                        All time low data for loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.all_time_low
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def score(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows different kind of scores for loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="score",
        description="""
                        Different kind of scores for loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.scores
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def bc(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows urls to blockchain explorers

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="bc",
        description="""
                        Blockchain explorers URLs for loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.blockchain_explorers
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def market(coin: gecko_coin.Coin, other_args: List[str]):
    """Shows market data for loaded coin

    Parameters
    ----------
    coin : gecko_coin.Coin
        Cryptocurrency
    other_args : List[str]
        argparse arguments

    """
    parser = argparse.ArgumentParser(
        add_help=False,
        prog="market",
        description="""
                        Market data for loaded coin
                        """,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if not ns_parser:
            return

        df = coin.market_data
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except SystemExit:
        print("")

    except Exception as e:
        print(e)
        print("")


def holdings_overview(other_args: List[str]):
    """
    Shows overview of public companies that holds ethereum or bitcoin from www.coingecko.com
    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="hold",
        add_help=False,
        description="Shows overview of public companies that holds ethereum or bitcoin",
    )

    parser.add_argument(
        "-c",
        "--coin",
        dest="coin",
        type=str,
        help="companies with ethereum or bitcoin",
        default="bitcoin",
        choices=["ethereum", "bitcoin"],
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_holdings_overview(endpoint=ns_parser.coin)
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def holdings_companies_list(other_args: List[str]):
    """Shows Ethereum/Bitcoin Holdings by Public Companies from www.coingecko.com
    Track publicly traded companies around the world that are buying ethereum as part of corporate treasury

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="hold_comp",
        add_help=False,
        description="Track publicly traded companies around the world that "
        "are buying ethereum as part of corporate treasury",
    )

    parser.add_argument(
        "-c",
        "--coin",
        dest="coin",
        type=str,
        help="companies with ethereum or bitcoin",
        default="bitcoin",
        choices=["ethereum", "bitcoin"],
    )

    parser.add_argument(
        "-l",
        "--links",
        dest="links",
        action="store_true",
        help="Flag to show urls",
        default=False,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_companies_assets(endpoint=ns_parser.coin)

        if ns_parser.links is True:
            df = df[["rank", "company", "url"]]
        else:
            df.drop("url", axis=1, inplace=True)

        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def gainers(other_args: List[str]):
    """Shows Largest Gainers - coins which gain the most in given period from www.coingecko.com

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="gainers",
        add_help=False,
        description="Shows Largest Gainers - coins which gain the most in given period",
    )

    parser.add_argument(
        "-p",
        "--period",
        dest="period",
        type=str,
        help="time period, one from [1h, 24h, 7d, 14d, 30d, 60d, 1y]",
        default="1h",
        choices=["1h", "24h", "7d", "14d", "30d", "60d", "1y"],
    )

    parser.add_argument(
        "-t",
        "--top",
        dest="top",
        type=int,
        help="top N number records",
        default=20,
    )

    parser.add_argument(
        "-s",
        "--sort",
        dest="sortby",
        type=str,
        help="Sort by given column. Default: rank",
        default="rank",
        choices=["rank", "symbol", "name", "volume", "price", "change"],
    )

    parser.add_argument(
        "--descend",
        action="store_false",
        help="Flag to sort in descending order (lowest first)",
        dest="descend",
        default=True,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        if ns_parser.sortby == "change":
            sortby = f"%change_{ns_parser.period}"
        else:
            sortby = ns_parser.sortby

        df = gecko.get_gainers_or_losers(
            period=ns_parser.period, typ="gainers"
        ).sort_values(by=sortby, ascending=ns_parser.descend)
        print(
            tabulate(
                df.head(ns_parser.top),
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def losers(other_args: List[str]):
    """Shows Largest Losers - coins which lost the most in given period of time from www.coingecko.com

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="losers",
        add_help=False,
        description="Shows Largest Losers - coins which price dropped the most in given period",
    )

    parser.add_argument(
        "-p",
        "--period",
        dest="period",
        type=str,
        help="time period, one from [1h, 24h, 7d, 14d, 30d, 60d, 1y]",
        default="1h",
        choices=["1h", "24h", "7d", "14d", "30d", "60d", "1y"],
    )

    parser.add_argument(
        "-t",
        "--top",
        dest="top",
        type=int,
        help="top N number records",
        default=20,
    )

    parser.add_argument(
        "-s",
        "--sort",
        dest="sortby",
        type=str,
        help="Sort by given column. Default: change",
        default="rank",
        choices=["rank", "symbol", "name", "volume", "price", "change"],
    )

    parser.add_argument(
        "--descend",
        action="store_false",
        help="Flag to sort in descending order (lowest first)",
        dest="descend",
        default=True,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        if ns_parser.sortby == "change":
            sortby = f"%change_{ns_parser.period}"
        else:
            sortby = ns_parser.sortby

        df = gecko.get_gainers_or_losers(
            period=ns_parser.period, typ="losers"
        ).sort_values(by=sortby, ascending=ns_parser.descend)
        print(
            tabulate(
                df.head(ns_parser.top),
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def discover(category: str, other_args: List[str]):
    """Discover coins by different categories
        - Most voted coins
        - Most popular coins
        - Recently added coins
        - Most positive sentiment coins

    Parameters
    ----------
    category: str
        one from list: [trending, most_voted, positive_sentiment, most_visited]
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="discover",
        add_help=False,
        description=f"Discover {category} coins by one of category\n"
        "Available categories: [trending, most_voted, positive_sentiment, most_visited]",
    )

    parser.add_argument(
        "-t",
        "--top",
        dest="top",
        type=int,
        help="top N number records",
        default=20,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.discover_coins(category=category)
        df.index = df.index + 1
        df.reset_index(inplace=True)
        df.rename(columns={"index": "rank"}, inplace=True)
        df = df.head(ns_parser.top)
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".5f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def news(other_args: List[str]):
    """Shows latest crypto news from www.coingecko.com

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="news",
        add_help=False,
        description="Shows latest crypto news from CoinGecko",
    )

    parser.add_argument(
        "-t",
        "--top",
        dest="top",
        type=int,
        help="top N number of news >=10",
        default=100,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_news(n=ns_parser.top)
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".0f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def categories(other_args: List[str]):
    """Shows top cryptocurrency categories by market capitalization from https://www.coingecko.com/en/categories
    The cryptocurrency category ranking is based on market capitalization.

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="categories",
        add_help=False,
        description="Shows top cryptocurrency categories by market capitalization",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_top_crypto_categories()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".0f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def recently_added(other_args: List[str]):
    """Shows recently added coins from "https://www.coingecko.com/en/coins/recently_added"

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="recently",
        add_help=False,
        description="Shows top cryptocurrency categories by market capitalization",
    )

    parser.add_argument(
        "-t",
        "--top",
        dest="top",
        type=int,
        help="top N number records",
        default=20,
    )

    parser.add_argument(
        "-s",
        "--sort",
        dest="sortby",
        type=str,
        help="Sort by given column. Default: change",
        default="rank",
        choices=["rank", "name", "symbol", "price", "change_24h", "change_1h", "added"],
    )

    parser.add_argument(
        "--descend",
        action="store_false",
        help="Flag to sort in descending order (lowest first)",
        dest="descend",
        default=True,
    )

    parser.add_argument(
        "-l",
        "--links",
        dest="links",
        action="store_true",
        help="Flag to show urls",
        default=False,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_recently_added_coins().sort_values(
            by=ns_parser.sortby, ascending=ns_parser.descend
        )

        if ns_parser.links is True:
            df = df[["rank", "symbol", "added", "url"]]
        else:
            df.drop("url", axis=1, inplace=True)

        print(
            tabulate(
                df.head(ns_parser.top),
                headers=df.columns,
                floatfmt=".0f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def stablecoins(other_args: List[str]):
    """Shows stablecoins data from "https://www.coingecko.com/en/stablecoins"

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="stables",
        add_help=False,
        description="Shows stablecoins by market capitalization",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_stable_coins()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".0f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def yfarms(other_args: List[str]):
    """Shows Top Yield Farming Pools by Value Locked from "https://www.coingecko.com/en/yield-farming"

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="yfarms",
        add_help=False,
        description="Shows Top Yield Farming Pools by Value Locked",
    )

    parser.add_argument(
        "-t",
        "--top",
        dest="top",
        type=int,
        help="Top N of records. Default 20",
        default=20,
    )

    parser.add_argument(
        "-s",
        "--sort",
        dest="sortby",
        type=str,
        help="Sort by given column. Default: rank",
        default="rank",
        choices=["rank", "name", "value_locked", "return_year"],
    )

    parser.add_argument(
        "--descend",
        action="store_false",
        help="Flag to sort in descending order (lowest first)",
        dest="descend",
        default=True,
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_yield_farms()
        df = df.sort_values(by=ns_parser.sortby, ascending=ns_parser.descend)

        print(
            tabulate(
                df.head(ns_parser.top),
                headers=df.columns,
                floatfmt=".0f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def top_volume_coins(other_args: List[str]):
    """Shows Top 100 Coins by Trading Volume from "https://www.coingecko.com/en/yield-farming"

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="top_volume",
        add_help=False,
        description="Shows Top 100 Coins by Trading Volume",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_top_volume_coins()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")

    except Exception as e:
        print(e)
        print("")


def top_defi_coins(other_args: List[str]):
    """Shows Top 100 DeFi Coins by Market Capitalization from "https://www.coingecko.com/en/defi"
    DeFi or Decentralized Finance refers to financial services that are built
    on top of distributed networks with no central intermediaries.

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="top_defi",
        add_help=False,
        description="Shows Top 100 DeFi Coins by Market Capitalization",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_top_defi_coins()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def top_dex(other_args: List[str]):
    """Shows Top Decentralized Exchanges on CoinGecko by Trading Volume from "https://www.coingecko.com/en/dex"

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="top_dex",
        add_help=False,
        description="Shows Top Decentralized Exchanges on CoinGecko by Trading Volume",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_top_dexes()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def top_nft(other_args: List[str]):
    """Shows Top 100 NFT Coins by Market Capitalization from "https://www.coingecko.com/en/nft"
    Top 100 NFT Coins by Market Capitalization
    NFT (Non-fungible Token) refers to digital assets with unique characteristics.
    Examples of NFT include crypto artwork, collectibles, game items, financial products, and more.

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="top_nft",
        add_help=False,
        description="Shows Top 100 NFT Coins by Market Capitalization",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_top_nfts()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".4f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def nft_of_the_day(other_args: List[str]):
    """Shows NFT of the day "https://www.coingecko.com/en/nft"

    NFT (Non-fungible Token) refers to digital assets with unique characteristics.
    Examples of NFT include crypto artwork, collectibles, game items, financial products, and more.

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="nft_today",
        add_help=False,
        description="Shows NFT of the day",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_nft_of_the_day()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def nft_market_status(other_args: List[str]):
    """Shows overview data of nft markets "https://www.coingecko.com/en/nft"

    NFT (Non-fungible Token) refers to digital assets with unique characteristics.
    Examples of NFT include crypto artwork, collectibles, game items, financial products, and more.

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="nft_market",
        add_help=False,
        description="Shows NFT market status",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_nft_market_status()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def exchanges(other_args: List[str]):
    """Shows list of top exchanges from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="exchanges",
        add_help=False,
        description="Shows Top Crypto Exchanges",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_exchanges()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".1f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def platforms(other_args: List[str]):
    """Shows list of financial platforms from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="platforms",
        add_help=False,
        description="Shows Top Crypto Financial Platforms",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_financial_platforms()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def products(other_args: List[str]):
    """Shows list of financial products from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="products",
        add_help=False,
        description="Shows Top Crypto Financial Products",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_finance_products()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def indexes(other_args: List[str]):
    """Shows list of crypto indexes from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="indexes",
        add_help=False,
        description="Shows list of crypto indexes from CoinGecko",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_indexes()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def derivatives(other_args: List[str]):
    """Shows  list of crypto derivatives from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="derivatives",
        add_help=False,
        description="Shows list of crypto derivatives from CoinGecko",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_derivatives()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def exchange_rates(other_args: List[str]):
    """Shows  list of crypto, fiats, commodity exchange rates from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="ex_rates",
        add_help=False,
        description="Shows list of crypto, fiats, commodity exchange rates from CoinGecko",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_exchange_rates()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def global_market_info(other_args: List[str]):
    """Shows global statistics about crypto from CoinGecko
        - market cap change
        - number of markets
        - icos
        - number of active crypto
        - market_cap_pct

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="global",
        add_help=False,
        description="Shows global statistics about Crypto Market",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_global_info()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".2f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def global_defi_info(other_args: List[str]):
    """Shows global statistics about Decentralized Finances from CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="defi",
        add_help=False,
        description="Shows global DeFi statistics",
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return

        df = gecko.get_global_defi_info()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".1f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")


def coin_list(other_args: List[str]):
    """Shows list of coins available on CoinGecko

    Parameters
    ----------
    other_args: List[str]
        Arguments to pass to argparse

    """
    parser = argparse.ArgumentParser(
        prog="coins",
        add_help=False,
        description="Shows list of coins available on CoinGecko",
    )
    parser.add_argument(
        "-s", "--skip", default=0, dest="skip", help="Skip n of records", type=int
    )
    parser.add_argument(
        "-l", "--limit", default=300, dest="limit", help="Limit of records", type=int
    )

    try:
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if not ns_parser:
            return
        try:
            df = gecko.get_coin_list()[
                ns_parser.skip : ns_parser.skip + ns_parser.limit
            ]
        except Exception:
            df = gecko.get_coin_list()
        print(
            tabulate(
                df,
                headers=df.columns,
                floatfmt=".1f",
                showindex=False,
                tablefmt="fancy_grid",
            )
        )
        print("")
    except Exception as e:
        print(e)
        print("")
