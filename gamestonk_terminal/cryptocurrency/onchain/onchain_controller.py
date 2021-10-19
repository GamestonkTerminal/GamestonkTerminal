"""Onchain Controller Module"""
__docformat__ = "numpy"

import os
import argparse
from typing import List

from prompt_toolkit.completion import NestedCompleter

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.menu import session
from gamestonk_terminal.helper_funcs import (
    get_flair,
    parse_known_args_and_warn,
    check_positive,
    check_int_range,
)

from gamestonk_terminal.cryptocurrency.onchain import (
    gasnow_view,
    whale_alert_view,
    ethplorer_view,
)

# pylint: disable=R1732


class OnchainController:
    """Onchain Controller class"""

    CHOICES = [
        "cls",
        "?",
        "help",
        "q",
        "quit",
    ]

    CHOICES_COMMANDS = [
        "gwei",
        "whales",
        "balance",
        "top",
        "holders",
        "tx",
        "hist",
        "info",
        "th",
        "prices",
    ]

    CHOICES += CHOICES_COMMANDS

    def __init__(self):
        """Constructor"""
        self.onchain_parser = argparse.ArgumentParser(add_help=False, prog="onchain")
        self.onchain_parser.add_argument(
            "cmd",
            choices=self.CHOICES,
        )

    def switch(self, an_input: str):
        """Process and dispatch input

        Parameters
        -------
        an_input : str
            string with input arguments

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

        (known_args, other_args) = self.onchain_parser.parse_known_args(
            an_input.split()
        )

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

    def call_help(self, *_):
        """Process Help command"""
        self.print_help()

    def call_q(self, _):
        """Process Q command - quit the menu"""
        return False

    def call_quit(self, _):
        """Process Quit command - quit the program"""
        return True

    def call_gwei(self, other_args: List[str]):
        """Process gwei command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="onchain",
            description="""
                Display ETH gas fees
                [Source: https://www.gasnow.org]
            """,
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

            gasnow_view.display_gwei_fees(export=ns_parser.export)

        except Exception as e:
            print(e, "\n")

    def call_whales(self, other_args: List[str]):
        """Process whales command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="wales",
            description="""
                Display crypto whales transactions.
                [Source: https://docs.whale-alert.io/]
            """,
        )

        parser.add_argument(
            "-m",
            "--min",
            dest="min",
            type=check_int_range(500000, 100 ** 7),
            help="Minimum value of transactions.",
            default=1000000,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: date",
            default="date",
            choices=[
                "date",
                "symbol",
                "blockchain",
                "amount",
                "amount_usd",
                "from",
                "to",
            ],
        )
        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=True,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            action="store_true",
            help="Flag to show addresses of transaction",
            default=False,
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

            whale_alert_view.display_whales_transactions(
                min_value=ns_parser.min,
                top=ns_parser.top,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                show_address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_balance(self, other_args: List[str]):
        """Process balance command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="balance",
            description="""
                Display info about tokens on given ethereum blockchain address.
                [Source: Ethplorer]
            """,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: index",
            default="index",
            choices=[
                "index",
                "balance",
                "tokenName",
                "tokenSymbol",
            ],
        )
        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=True,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            help="Ethereum blockchain address",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-a")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_address_info(
                top=ns_parser.top,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_hist(self, other_args: List[str]):
        """Process hist command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="hist",
            description="""
                   Display history for given ethereum blockchain address.
                    e.g. 0x3cD751E6b0078Be393132286c442345e5DC49699
                   [Source: Ethplorer]
               """,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: timestamp",
            default="timestamp",
            choices=["timestamp", "transactionHash", "token", "value"],
        )
        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=True,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            help="Ethereum blockchain addresses",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-a")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_address_history(
                top=ns_parser.top,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_holders(self, other_args: List[str]):
        """Process holders command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="holders",
            description="""
                Display top ERC20 token holders: e.g. 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
                [Source: Ethplorer]
            """,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: share",
            default="share",
            choices=[
                "address",
                "balance",
                "share",
            ],
        )
        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=False,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            help="ERC20 token address",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-a")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_top_token_holders(
                top=ns_parser.top,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_top(self, other_args: List[str]):
        """Process top command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="top",
            description="""
                Display top ERC20 tokens.
                [Source: Ethplorer]
            """,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: rank",
            default="rank",
            choices=[
                "rank",
                "name",
                "symbol",
                "price",
                "txsCount",
                "transfersCount",
                "holdersCount",
                "address",
            ],
        )

        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=True,
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

            ethplorer_view.display_top_tokens(
                top=ns_parser.top,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_info(self, other_args: List[str]):
        """Process info command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="info",
            description="""
                Display info about ERC20 token. e.g. 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
                [Source: Ethplorer]
            """,
        )

        parser.add_argument(
            "--social",
            action="store_false",
            help="Flag to show social media links",
            dest="social",
            default=False,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            help="ERC20 token address",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-a")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_token_info(
                social=ns_parser.social,
                address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_th(self, other_args: List[str]):
        """Process th command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="th",
            description="""
                     Displays info about token history.
                     e.g. 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
                     [Source: Ethplorer]
                 """,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: value",
            default="value",
            choices=[
                "value",
            ],
        )
        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=True,
        )

        parser.add_argument(
            "--hash",
            action="store_false",
            help="Flag to show transaction hash",
            dest="hash",
            default=True,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            help="ERC20 token address",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-a")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_token_history(
                top=ns_parser.top,
                hash_=ns_parser.hash,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_tx(self, other_args: List[str]):
        """Process tx command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="tx",
            description="""
                  Display info ERC20 token transaction on ethereum blockchain.
                  e.g. 0x9dc7b43ad4288c624fdd236b2ecb9f2b81c93e706b2ffd1d19b112c1df7849e6
                  [Source: Ethplorer]
              """,
        )

        parser.add_argument(
            "-tx",
            "--tx",
            dest="tx",
            help="Ethereum transaction hash",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-tx")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_tx_info(
                tx_hash=ns_parser.tx,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def call_prices(self, other_args: List[str]):
        """Process prices command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="prices",
            description="""
                  "Display token historical prices. e.g. 0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984
                  [Source: Ethplorer]
              """,
        )

        parser.add_argument(
            "-t",
            "--top",
            dest="top",
            type=check_positive,
            help="top N number records",
            default=10,
        )

        parser.add_argument(
            "-s",
            "--sort",
            dest="sortby",
            type=str,
            help="Sort by given column. Default: date",
            default="date",
            choices=[
                "date",
                "cap",
                "volumeConverted",
                "open",
                "high",
                "close",
                "low",
            ],
        )
        parser.add_argument(
            "--descend",
            action="store_false",
            help="Flag to sort in descending order (lowest first)",
            dest="descend",
            default=False,
        )

        parser.add_argument(
            "-a",
            "--address",
            dest="address",
            help="ERC20 token addresses",
            default=False,
            type=str,
            required="-h" not in other_args,
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
                if not other_args[0][0] == "-":
                    other_args.insert(0, "-a")

            ns_parser = parse_known_args_and_warn(parser, other_args)

            if not ns_parser:
                return

            ethplorer_view.display_token_historical_prices(
                top=ns_parser.top,
                sortby=ns_parser.sortby,
                descend=ns_parser.descend,
                address=ns_parser.address,
                export=ns_parser.export,
            )

        except Exception as e:
            print(e)

    def print_help(self):
        """Print help"""
        help_text = """
Onchain:
    cls         clear screen
    ?/help      show this menu again
    q           quit this menu, and shows back to main menu
    quit        quit to abandon the program

    gwei              check current eth gas fees
    whales            check crypto wales transactions

Ethereum:
    balance           check ethereum address balance
    top               top ERC20 tokens
    holders           top ERC20 token holders
    hist              ethereum address history (transactions)
    info              ERC20 token info
    th                ERC20 token history
    tx                ethereum blockchain transaction info
    prices            ERC20 token historical prices
"""

        print(help_text)


def menu():
    """Onchain Menu"""
    onchain_controller = OnchainController()
    onchain_controller.call_help(None)

    while True:
        # Get input command from user
        if session and gtff.USE_PROMPT_TOOLKIT:
            completer = NestedCompleter.from_nested_dict(
                {c: None for c in onchain_controller.CHOICES}
            )
            an_input = session.prompt(
                f"{get_flair()} (crypto)>(onchain)> ",
                completer=completer,
            )
        else:
            an_input = input(f"{get_flair()} (crypto)>(onchain)> ")

        try:
            process_input = onchain_controller.switch(an_input)
        except SystemExit:
            print("The command selected doesn't exist\n")
            continue

        if process_input is False:
            return False

        if process_input is True:
            return True
