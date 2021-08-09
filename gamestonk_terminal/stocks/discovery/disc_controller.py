""" Disc Controller """
__docformat__ = "numpy"

import argparse
import os
from typing import List
from matplotlib import pyplot as plt
from prompt_toolkit.completion import NestedCompleter
from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.helper_funcs import get_flair
from gamestonk_terminal.menu import session
from gamestonk_terminal.helper_funcs import (
    parse_known_args_and_warn,
    check_non_negative,
)
from gamestonk_terminal.stocks.discovery import (
    ark_view,
    fidelity_view,
    seeking_alpha_view,
    short_interest_view,
    yahoofinance_view,
    finra_ats_view,
    finnhub_view,
    stockgrid_view,
)


class DiscoveryController:
    """Discovery Controller"""

    # Command choices
    CHOICES = [
        "?",
        "cls",
        "help",
        "q",
        "quit",
    ]

    CHOICES_COMMANDS = [
        "pipo",
        "fipo",
        "gainers",
        "losers",
        "orders",
        "ark_orders",
        "up_earnings",
        "high_short",
        "low_float",
        "latest",
        "trending",
        "darkpool",
        "darkshort",
        "shortvol",
    ]

    CHOICES += CHOICES_COMMANDS

    def __init__(self):
        """Constructor"""
        self.disc_parser = argparse.ArgumentParser(add_help=False, prog="disc")
        self.disc_parser.add_argument(
            "cmd",
            choices=self.CHOICES,
        )

    @staticmethod
    def print_help():
        """Print help"""
        help_text = """https://github.com/GamestonkTerminal/GamestonkTerminal/tree/main/gamestonk_terminal/stocks/discovery

Discovery:
    cls            clear screen")
    ?/help         show this menu again")
    q              quit this menu, and shows back to main menu")
    quit           quit to abandon program")

Finnhub:
    pipo           past IPOs dates
    fipo           future IPOs dates
Yahoo Finance:
    gainers        show latest top gainers
    losers         show latest top losers
Fidelity:
    orders         orders by Fidelity Customers
cathiesark.com:
    ark_orders     orders by ARK Investment Management LLC
Seeking Alpha:
    latest         latest news
    trending       trending news
    up_earnings    upcoming earnings release dates
highshortinterest.com:
    high_short     show top high short interest stocks of over 20% ratio
lowfloat.com:
    low_float      show low float stocks under 10M shares float
FINRA:
    darkpool       promising tickers based on dark pool shares regression
Stockgrid:
    darkshort      dark pool short position
    shortvol       short interest and days to cover
"""
        print(help_text)

    def switch(self, an_input: str):
        """Process and dispatch input

        Returns
        -------
        True, False or None
            False - quit the menu
            True - quit the program
            None - continue in the menu
        """
        # Empty command
        if not an_input:
            print("")
            return None

        (known_args, other_args) = self.disc_parser.parse_known_args(an_input.split())

        # Help menu again
        if known_args.cmd == "?":
            self.print_help()
            return None

        # Clear screen
        if known_args.cmd == "cls":
            os.system("cls||clear")
            return None

        return getattr(
            self, "call_" + known_args.cmd, lambda: "Command not recognized!"
        )(other_args)

    def call_help(self, _):
        """Process Help command"""
        self.print_help()

    def call_q(self, _):
        """Process Q command - quit the menu"""
        return False

    def call_quit(self, _):
        """Process Quit command - quit the program"""
        return True

    def call_pipo(self, other_args: List[str]):
        """Process pipo command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="pipo",
            description="""
                Past IPOs dates. [Source: https://finnhub.io]
            """,
        )
        parser.add_argument(
            "-n",
            "--num",
            action="store",
            dest="num",
            type=check_non_negative,
            default=5,
            help="Number of past days to look for IPOs.",
        )
        parser.add_argument(
            "--export",
            choices=["csv", "json", "xlsx"],
            default="",
            type=str,
            dest="export",
            help="Export dataframe data to csv,json,xlsx file",
        )
        try:
            if other_args:
                if "-" not in other_args[0]:
                    other_args.insert(0, "-n")

            ns_parser = parse_known_args_and_warn(parser, other_args)
            if not ns_parser:
                return

            finnhub_view.past_ipo(
                num_days_behind=ns_parser.num,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e, "\n")

    def call_fipo(self, other_args: List[str]):
        """Process fipo command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="fipo",
            description="""
                Future IPOs dates. [Source: https://finnhub.io]
            """,
        )
        parser.add_argument(
            "-n",
            "--num",
            action="store",
            dest="num",
            type=check_non_negative,
            default=5,
            help="Number of future days to look for IPOs.",
        )
        parser.add_argument(
            "--export",
            choices=["csv", "json", "xlsx"],
            default="",
            type=str,
            dest="export",
            help="Export dataframe data to csv,json,xlsx file",
        )
        try:
            if other_args:
                if "-" not in other_args[0]:
                    other_args.insert(0, "-n")

            ns_parser = parse_known_args_and_warn(parser, other_args)
            if not ns_parser:
                return

            finnhub_view.future_ipo(
                num_days_ahead=ns_parser.num,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e, "\n")

    def call_gainers(self, other_args: List[str]):
        """Process gainers command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="gainers",
            description="Print up to 25 top ticker gainers. [Source: Yahoo Finance]",
        )
        parser.add_argument(
            "-n",
            "--num",
            action="store",
            dest="num",
            type=int,
            default=5,
            choices=range(1, 25),
            help="Number of the top gainers stocks to retrieve.",
        )
        parser.add_argument(
            "--export",
            choices=["csv", "json", "xlsx"],
            default="",
            type=str,
            dest="export",
            help="Export dataframe data to csv,json,xlsx file",
        )
        try:
            ns_parser = parse_known_args_and_warn(parser, other_args)
            if not ns_parser:
                return

            yahoofinance_view.display_gainers(
                num_stocks=ns_parser.num,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e, "\n")

    def call_losers(self, other_args: List[str]):
        """Process losers command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="losers",
            description="Print up to 25 top ticker losers. [Source: Yahoo Finance]",
        )
        parser.add_argument(
            "-n",
            "--num",
            action="store",
            dest="num",
            type=int,
            default=5,
            choices=range(1, 25),
            help="Number of the top losers stocks to retrieve.",
        )
        parser.add_argument(
            "--export",
            choices=["csv", "json", "xlsx"],
            default="",
            type=str,
            dest="export",
            help="Export dataframe data to csv,json,xlsx file",
        )
        try:
            ns_parser = parse_known_args_and_warn(parser, other_args)
            if not ns_parser:
                return

            yahoofinance_view.display_losers(
                num_stocks=ns_parser.num,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e, "\n")

    def call_orders(self, other_args: List[str]):
        """Process orders command"""
        fidelity_view.orders_view(other_args)

    def call_ark_orders(self, other_args: List[str]):
        """Process ark_orders command"""
        ark_view.ark_orders_view(other_args)

    def call_up_earnings(self, other_args: List[str]):
        """Process up_earnings command"""
        seeking_alpha_view.earnings_release_dates_view(other_args)

    def call_high_short(self, other_args: List[str]):
        """Process high_short command"""
        short_interest_view.high_short_interest_view(other_args)

    def call_low_float(self, other_args: List[str]):
        """Process low_float command"""
        short_interest_view.low_float_view(other_args)

    def call_latest(self, other_args: List[str]):
        """Process latest command"""
        seeking_alpha_view.latest_news_view(other_args)

    def call_trending(self, other_args: List[str]):
        """Process trending command"""
        seeking_alpha_view.trending_news_view(other_args)

    def call_darkpool(self, other_args: List[str]):
        """Process darkpool command"""
        finra_ats_view.dark_pool(other_args)

    def call_darkshort(self, other_args: List[str]):
        """Process darkshort command"""
        stockgrid_view.darkshort(other_args)

    def call_shortvol(self, other_args: List[str]):
        """Process shortvol command"""
        stockgrid_view.shortvol(other_args)


def menu():
    """Discovery Menu"""

    disc_controller = DiscoveryController()
    disc_controller.call_help(None)

    # Loop forever and ever
    while True:
        # Get input command from user
        if session and gtff.USE_PROMPT_TOOLKIT:
            completer = NestedCompleter.from_nested_dict(
                {c: None for c in disc_controller.CHOICES}
            )

            an_input = session.prompt(
                f"{get_flair()} (stocks)>(disc)> ",
                completer=completer,
            )
        else:
            an_input = input(f"{get_flair()} (stocks)>(disc)> ")

        try:
            plt.close("all")

            process_input = disc_controller.switch(an_input)

            if process_input is not None:
                return process_input

        except SystemExit:
            print("The command selected doesn't exist\n")
            continue
