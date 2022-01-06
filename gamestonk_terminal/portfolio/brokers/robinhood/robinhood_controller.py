"""Robinhood Controller"""
__docformat__ = "numpy"

import argparse
from typing import List

from prompt_toolkit.completion import NestedCompleter
from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.menu import session
from gamestonk_terminal.portfolio.brokers.robinhood import (
    robinhood_view,
    robinhood_model,
)
from gamestonk_terminal.parent_classes import BaseController
from gamestonk_terminal.decorators import try_except
from gamestonk_terminal.helper_funcs import (
    parse_known_args_and_warn,
    EXPORT_ONLY_RAW_DATA_ALLOWED,
)


class RobinhoodController(BaseController):

    CHOICES_COMMANDS = ["holdings", "history", "login"]

    valid_span = ["day", "week", "month", "3month", "year", "5year", "all"]
    valid_interval = ["5minute", "10minute", "hour", "day", "week"]

    def __init__(self, queue: List[str] = None):
        """CONSTRUCTOR"""
        super().__init__("/portfolio/bro/rh/", queue)
        self.choices += self.CHOICES_COMMANDS

        if session and gtff.USE_PROMPT_TOOLKIT:
            choices: dict = {c: {} for c in self.CHOICES}
            choices["history"]["-i"] = {c: None for c in self.valid_interval}
            choices["history"]["--interval"] = {c: None for c in self.valid_interval}
            choices["history"]["-s"] = {c: None for c in self.valid_span}
            choices["history"]["--span"] = {c: None for c in self.valid_span}
            self.completer = NestedCompleter.from_nested_dict(choices)

    def print_help(self):
        """Print help"""
        help_text = """
Robinhood:
    login       login to robinhood

    holdings    show account holdings in stocks
    history     show equity history of your account
"""

        print(help_text)

    @try_except
    def call_login(self, _):
        """Process login"""
        robinhood_model.login()

    @try_except
    def call_holdings(self, other_args: List[str]):
        """Process holdings command"""
        parser = argparse.ArgumentParser(
            prog="holdings",
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description="Display info about your trading accounts on Robinhood",
        )
        ns_parser = parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_RAW_DATA_ALLOWED
        )
        if ns_parser:
            robinhood_view.display_holdings(export=ns_parser.export)

    @try_except
    def call_history(self, other_args: List[str]):
        """Process history command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="history",
            description="""Historical Portfolio Info""",
        )
        parser.add_argument(
            "-s",
            "--span",
            dest="span",
            type=str,
            choices=self.valid_span,
            default="3month",
            help="Span of historical data",
        )
        parser.add_argument(
            "-i",
            "--interval",
            dest="interval",
            default="day",
            choices=self.valid_interval,
            type=str,
            help="Interval to look at portfolio",
        )
        ns_parser = parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_RAW_DATA_ALLOWED
        )
        if ns_parser:
            robinhood_view.display_historical(
                interval=ns_parser.interval,
                span=ns_parser.span,
                export=ns_parser.export,
            )
