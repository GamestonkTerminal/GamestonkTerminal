"""Papermill Controller Module"""
__docformat__ = "numpy"

import argparse
import os
from typing import List
import subprocess
from prompt_toolkit.completion import NestedCompleter
from gamestonk_terminal.cryptocurrency.report import crypto_market_view

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.menu import session
from gamestonk_terminal.helper_funcs import get_flair
from gamestonk_terminal import config_terminal
from gamestonk_terminal.helper_funcs import parse_known_args_and_warn

# pylint: disable=R1732


class ReportController:
    """Report Controller class"""

    CHOICES = [
        "cls",
        "?",
        "help",
        "q",
        "quit",
    ]

    CHOICES_COMMANDS = [
        "ov",
    ]

    CHOICES += CHOICES_COMMANDS

    def __init__(self):
        """Constructor"""
        self.report_parser = argparse.ArgumentParser(add_help=False, prog="report")
        self.report_parser.add_argument(
            "cmd",
            choices=self.CHOICES,
        )

    def switch(self, an_input: str, proc: subprocess.Popen):
        """Process and dispatch input

        Parameters
        -------
        an_input : str
            string with input arguments
        proc : subprocess.Popen
            subprocess that calls jupyter notebook for report generation

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

        (known_args, other_args) = self.report_parser.parse_known_args(an_input.split())

        # Help menu again
        if known_args.cmd == "?":
            print_help()
            return None

        # Clear screen
        if known_args.cmd == "cls":
            os.system("cls||clear")
            return None

        return getattr(
            self, "call_" + known_args.cmd, lambda: "Command not recognized!"
        )(other_args, proc)

    def call_help(self, *_):
        """Process Help command"""
        print_help()

    def call_q(self, _, proc):
        """Process Q command - quit the menu"""
        proc.kill()
        return False

    def call_quit(self, _, proc):
        """Process Quit command - quit the program"""
        proc.kill()
        return True

    def call_ov(self, other_args: List[str], _):
        """Process ov command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="co",
            description="""
                    Run crypto market report
                """,
        )

        parser.add_argument(
            "-m",
            "--mode",
            action="store",
            dest="mode",
            default="html",
            choices=["ipynb", "html"],
            help="Output mode to show report. ipynb will allow to add information to the report.",
        )

        try:
            ns_parser = parse_known_args_and_warn(parser, other_args)
            if not ns_parser:
                return

            crypto_market_view.crypto_market_report(mode=ns_parser.mode)

        except Exception as e:
            print(e, "\n")
        except SystemExit:
            print("")


def print_help():
    """Print help"""
    print(
        "https://github.com/GamestonkTerminal/GamestonkTerminal/tree/main/gamestonk_terminal/cryptocurrency/report"
    )
    print("\nReports:")
    print("   cls           clear screen")
    print("   ?/help        show this menu again")
    print("   q             quit this menu, and shows back to main menu")
    print("   quit          quit to abandon program")
    print("")
    print("   ov            generate crypto overview report")
    print("")


def menu():
    """Report Menu"""
    report_controller = ReportController()
    report_controller.call_help(None)

    # Initialize jupyter notebook
    cmd = f"jupyter notebook --port={config_terminal.PAPERMILL_NOTEBOOK_REPORT_PORT}"
    proc = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    while True:
        # Get input command from user
        if session and gtff.USE_PROMPT_TOOLKIT:
            completer = NestedCompleter.from_nested_dict(
                {c: None for c in report_controller.CHOICES}
            )
            an_input = session.prompt(
                f"{get_flair()} (crypto)>(report)> ",
                completer=completer,
            )
        else:
            an_input = input(f"{get_flair()} (crypto)>(report)> ")

        try:
            process_input = report_controller.switch(an_input, proc)
        except SystemExit:
            print("The command selected doesn't exist\n")
            continue

        if process_input is False:
            return False

        if process_input is True:
            return True
