""" Portfolio Optimization Controller Module """
__docformat__ = "numpy"

import argparse
import logging
from typing import List

from prompt_toolkit.completion import NestedCompleter

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.decorators import log_start_end
from gamestonk_terminal.helper_funcs import (
    check_non_negative,
    get_rf,
    parse_known_args_and_warn,
)
from gamestonk_terminal.menu import session
from gamestonk_terminal.parent_classes import BaseController
from gamestonk_terminal.portfolio.portfolio_optimization import (
    optimizer_helper,
    optimizer_view,
)
from gamestonk_terminal.rich_config import console

# pylint: disable=C0302


logger = logging.getLogger(__name__)


class PortfolioOptimization(BaseController):
    """Portfolio Optimization Controller class"""

    CHOICES_COMMANDS = [
        "select",
        "add",
        "rmv",
        "equal",
        "mktcap",
        "dividend",
        "property",
        "maxsharpe",
        "minvol",
        "effret",
        "effrisk",
        "maxquadutil",
        "ef",
        "yolo",
    ]

    period_choices = [
        "1d",
        "5d",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "2y",
        "5y",
        "10y",
        "ytd",
        "max",
    ]

    yf_info_choices = [
        "previousClose",
        "regularMarketOpen",
        "twoHundredDayAverage",
        "trailingAnnualDividendYield",
        "payoutRatio",
        "volume24Hr",
        "regularMarketDayHigh",
        "navPrice",
        "averageDailyVolume10Day",
        "totalAssets",
        "regularMarketPreviousClose",
        "fiftyDayAverage",
        "trailingAnnualDividendRate",
        "open",
        "toCurrency",
        "averageVolume10days",
        "expireDate",
        "yield",
        "algorithm",
        "dividendRate",
        "exDividendDate",
        "beta",
        "circulatingSupply",
        "regularMarketDayLow",
        "priceHint",
        "currency",
        "trailingPE",
        "regularMarketVolume",
        "lastMarket",
        "maxSupply",
        "openInterest",
        "marketCap",
        "volumeAllCurrencies",
        "strikePrice",
        "averageVolume",
        "priceToSalesTrailing12Months",
        "dayLow",
        "ask",
        "ytdReturn",
        "askSize",
        "volume",
        "fiftyTwoWeekHigh",
        "forwardPE",
        "fromCurrency",
        "fiveYearAvgDividendYield",
        "fiftyTwoWeekLow",
        "bid",
        "dividendYield",
        "bidSize",
        "dayHigh",
        "annualHoldingsTurnover",
        "enterpriseToRevenue",
        "beta3Year",
        "profitMargins",
        "enterpriseToEbitda",
        "52WeekChange",
        "morningStarRiskRating",
        "forwardEps",
        "revenueQuarterlyGrowth",
        "sharesOutstanding",
        "fundInceptionDate",
        "annualReportExpenseRatio",
        "bookValue",
        "sharesShort",
        "sharesPercentSharesOut",
        "heldPercentInstitutions",
        "netIncomeToCommon",
        "trailingEps",
        "lastDividendValue",
        "SandP52WeekChange",
        "priceToBook",
        "heldPercentInsiders",
        "shortRatio",
        "sharesShortPreviousMonthDate",
        "floatShares",
        "enterpriseValue",
        "fundFamily",
        "threeYearAverageReturn",
        "lastSplitFactor",
        "legalType",
        "lastDividendDate",
        "morningStarOverallRating",
        "earningsQuarterlyGrowth",
        "pegRatio",
        "lastCapGain",
        "shortPercentOfFloat",
        "sharesShortPriorMonth",
        "impliedSharesOutstanding",
        "fiveYearAverageReturn",
        "regularMarketPrice",
    ]
    PATH = "/portfolio/po/"

    def __init__(self, tickers: List[str] = None, queue: List[str] = None):
        """Constructor"""
        super().__init__(queue)

        if tickers:
            self.tickers = list(set(tickers))
        else:
            self.tickers = list()

        if session and gtff.USE_PROMPT_TOOLKIT:
            choices: dict = {c: {} for c in self.controller_choices}
            choices["property"]["-p"] = {c: None for c in self.yf_info_choices}
            choices["property"]["--property"] = {c: None for c in self.yf_info_choices}
            for fn in ["maxsharpe", "minvol", "maxquadutil", "effret", "effrisk", "ef"]:
                choices[fn]["-p"] = {c: None for c in self.period_choices}
                choices[fn]["--period"] = {c: None for c in self.period_choices}
            self.completer = NestedCompleter.from_nested_dict(choices)

    def print_help(self):
        """Print help"""
        help_text = f"""[cmds]
    select        select list of tickers to be optimized
    add           add tickers to the list of the tickers to be optimized
    rmv           remove tickers from the list of the tickers to be optimized[/cmds]

[param]Tickers: [/param]{('None', ', '.join(self.tickers))[bool(self.tickers)]}

[info]Optimization:[/info][cmds]
    equal         equally weighted
    mktcap        weighted according to market cap (property marketCap)
    dividend      weighted according to dividend yield (property dividendYield)
    property      weight according to selected info property

[info]Mean Variance Optimization:[/info]
    maxsharpe     optimizes for maximal Sharpe ratio (a.k.a the tangency portfolio
    minvol        optimizes for minimum volatility
    maxquadutil   maximises the quadratic utility, given some risk aversion
    effret        maximises return for a given target risk
    effrisk       minimises risk for a given target return

    ef            show the efficient frontier[/cmds]
    """
        console.print(text=help_text, menu="Portfolio - Portfolio Optimization")

    @log_start_end(log=logger)
    def call_select(self, other_args: List[str]):
        """Process select command"""
        self.tickers = []
        self.add_stocks(other_args)

    @log_start_end(log=logger)
    def call_add(self, other_args: List[str]):
        """Process add command"""
        self.add_stocks(other_args)

    @log_start_end(log=logger)
    def call_rmv(self, other_args: List[str]):
        """Process rmv command"""
        self.rmv_stocks(other_args)

    @log_start_end(log=logger)
    def call_equal(self, other_args: List[str]):
        """Process equal command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="equal",
            description="Returns an equally weighted portfolio",
        )
        parser.add_argument(
            "-v",
            "--value",
            default=1,
            type=float,
            dest="value",
            help="Amount to allocate to portfolio",
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights",
        )

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            optimizer_view.display_equal_weight(
                stocks=self.tickers, value=ns_parser.value, pie=ns_parser.pie
            )

    @log_start_end(log=logger)
    def call_mktcap(self, other_args: List[str]):
        """Process mktcap command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="mktcap",
            description="Returns a portfolio that is weighted based on Market Cap.",
        )
        parser.add_argument(
            "-v",
            "--value",
            default=1,
            type=float,
            dest="value",
            help="Amount to allocate to portfolio",
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights",
        )
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 stocks selected to perform calculations."
                )

            optimizer_view.display_property_weighting(
                self.tickers,
                s_property="marketCap",
                value=ns_parser.value,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_dividend(self, other_args: List[str]):
        """Process dividend command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="dividend",
            description="Returns a portfolio that is weighted based dividend yield.",
        )
        parser.add_argument(
            "-v",
            "--value",
            default=1,
            type=float,
            dest="value",
            help="Amount to allocate to portfolio",
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights",
        )
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 stocks selected to perform calculations."
                )

            optimizer_view.display_property_weighting(
                self.tickers,
                s_property="dividendYield",
                value=ns_parser.value,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_property(self, other_args: List[str]):
        """Process property command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="property",
            description="Returns a portfolio that is weighted based on selected property.",
        )
        parser.add_argument(
            "-p",
            "--property",
            required=bool("-h" not in other_args),
            type=optimizer_helper.check_valid_property_type,
            dest="property",
            choices=self.yf_info_choices,
            help="""Property info to weigh. Use one of yfinance info options.""",
        )
        parser.add_argument(
            "-v",
            "--value",
            default=1,
            type=float,
            dest="value",
            help="Amount to allocate to portfolio",
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights",
        )
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 stocks selected to perform calculations."
                )

            optimizer_view.display_property_weighting(
                self.tickers,
                s_property=ns_parser.property,
                value=ns_parser.value,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_maxsharpe(self, other_args: List[str]):
        """Process maxsharpe command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="maxsharpe",
            description="Maximise the Sharpe Ratio",
        )
        parser.add_argument(
            "-p",
            "--period",
            default="1y",
            dest="period",
            help="period to get yfinance data from",
            choices=self.period_choices,
        )
        parser.add_argument(
            "-v",
            "--value",
            dest="value",
            help="Amount to allocate to portfolio",
            type=float,
            default=1.0,
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights",
        )
        parser.add_argument(
            "-r",
            "--risk-free-rate",
            type=float,
            dest="risk_free_rate",
            default=get_rf(),
            help="""Risk-free rate of borrowing/lending. The period of the risk-free rate
                should correspond to the frequency of expected returns.""",
        )

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            optimizer_view.display_max_sharpe(
                stocks=self.tickers,
                period=ns_parser.period,
                value=ns_parser.value,
                rfrate=ns_parser.risk_free_rate,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_minvol(self, other_args: List[str]):
        """Process minvol command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="minvol",
            description="Optimizes for minimum volatility",
        )
        parser.add_argument(
            "-p",
            "--period",
            default="1y",
            dest="period",
            help="period to get yfinance data from",
            choices=self.period_choices,
        )
        parser.add_argument(
            "-v",
            "--value",
            dest="value",
            help="Amount to allocate to portfolio",
            type=float,
            default=1.0,
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights",
        )
        ns_parser = parse_known_args_and_warn(parser, other_args)

        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            optimizer_view.display_min_volatility(
                stocks=self.tickers,
                period=ns_parser.period,
                value=ns_parser.value,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_maxquadutil(self, other_args: List[str]):
        """Process maxquadutil command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="maxquadutil",
            description="Maximises the quadratic utility, given some risk aversion",
        )
        parser.add_argument(
            "-p",
            "--period",
            default="1y",
            dest="period",
            help="period to get yfinance data from",
            choices=self.period_choices,
        )
        parser.add_argument(
            "-v",
            "--value",
            dest="value",
            help="Amount to allocate to portfolio",
            type=float,
            default=1.0,
        )
        parser.add_argument(
            "-n",
            "--market-neutral",
            action="store_true",
            default=False,
            dest="market_neutral",
            help="""whether the portfolio should be market neutral (weights sum to zero), defaults to False.
            Requires negative lower weight bound.""",
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights. Only if neutral flag is left False.",
        )
        parser.add_argument(
            "-r",
            "--risk-aversion",
            type=float,
            dest="risk_aversion",
            default=1.0,
            help="risk aversion parameter",
        )

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            if ns_parser.pie and ns_parser.market_neutral:
                console.print(
                    "Cannot show pie chart for market neutral due to negative weights."
                )

            optimizer_view.display_max_quadratic_utility(
                stocks=self.tickers,
                period=ns_parser.period,
                value=ns_parser.value,
                risk_aversion=ns_parser.risk_aversion,
                market_neutral=ns_parser.market_neutral,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_effrisk(self, other_args: List[str]):
        """Process effrisk command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="effrisk",
            description="""Maximise return for a target risk. The resulting portfolio will have
            a volatility less than the target (but not guaranteed to be equal)""",
        )
        parser.add_argument(
            "-p",
            "--period",
            default="1y",
            dest="period",
            help="period to get yfinance data from",
            choices=self.period_choices,
        )
        parser.add_argument(
            "-v",
            "--value",
            dest="value",
            help="Amount to allocate to portfolio",
            type=float,
            default=1.0,
        )
        parser.add_argument(
            "-n",
            "--market-neutral",
            action="store_true",
            default=False,
            dest="market_neutral",
            help="""whether the portfolio should be market neutral (weights sum to zero), defaults to False.
            Requires negative lower weight bound.""",
        )

        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights. Only if neutral flag is left False.",
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-t")
        parser.add_argument(
            "-t",
            "--target-volatility",
            type=float,
            dest="target_volatility",
            default=0.1,
            help="The desired maximum volatility of the resulting portfolio",
        )

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            if ns_parser.pie and ns_parser.market_neutral:
                console.print(
                    "Cannot show pie chart for market neutral due to negative weights."
                )

            optimizer_view.display_efficient_risk(
                stocks=self.tickers,
                period=ns_parser.period,
                value=ns_parser.value,
                target_volatility=ns_parser.target_volatility,
                market_neutral=ns_parser.market_neutral,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_effret(self, other_args: List[str]):
        """Process effret command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="effret",
            description="Calculate the 'Markowitz portfolio', minimising volatility for a given target return",
        )
        parser.add_argument(
            "-p",
            "--period",
            default="1y",
            dest="period",
            help="period to get yfinance data from",
            choices=self.period_choices,
        )
        parser.add_argument(
            "-v",
            "--value",
            dest="value",
            help="Amount to allocate to portfolio",
            type=float,
            default=1.0,
        )
        parser.add_argument(
            "-n",
            "--market-neutral",
            action="store_true",
            default=False,
            dest="market_neutral",
            help="""whether the portfolio should be market neutral (weights sum to zero), defaults to False.
            Requires negative lower weight bound.""",
        )
        parser.add_argument(
            "--pie",
            action="store_true",
            dest="pie",
            default=False,
            help="Display a pie chart for weights. Only if neutral flag is left False.",
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-t")

        parser.add_argument(
            "-t",
            "--target-return",
            type=float,
            dest="target_return",
            default=0.1,
            help="the desired return of the resulting portfolio",
        )
        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            if ns_parser.pie and ns_parser.market_neutral:
                console.print(
                    "Cannot show pie chart for market neutral due to negative weights."
                )

            optimizer_view.display_efficient_return(
                stocks=self.tickers,
                period=ns_parser.period,
                value=ns_parser.value,
                target_return=ns_parser.target_return,
                market_neutral=ns_parser.market_neutral,
                pie=ns_parser.pie,
            )

    @log_start_end(log=logger)
    def call_ef(self, other_args):
        """Process ef command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="ef",
            description="""This function plots random portfolios based
                        on their risk and returns and shows the efficient frontier.""",
        )
        parser.add_argument(
            "-p",
            "--period",
            default="1y",
            dest="period",
            help="period to get yfinance data from",
            choices=self.period_choices,
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-n")
        parser.add_argument(
            "-n",
            "--number-portfolios",
            default=300,
            type=check_non_negative,
            dest="n_port",
            help="number of portfolios to simulate",
        )
        parser.add_argument(
            "-r",
            "--risk-free",
            action="store_true",
            dest="risk_free",
            default=False,
            help="Adds the optimal line with the risk-free asset",
        )

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            if len(self.tickers) < 2:
                console.print(
                    "Please have at least 2 loaded tickers to calculate weights.\n"
                )

            optimizer_view.display_ef(
                stocks=self.tickers,
                period=ns_parser.period,
                n_portfolios=ns_parser.n_port,
                risk_free=ns_parser.risk_free,
            )

    @log_start_end(log=logger)
    def call_yolo(self, _):
        # Easter egg :)
        console.print("DFV YOLO")
        console.print("GME: ALL", "\n")

    def add_stocks(self, other_args: List[str]):
        """Add ticker or Select tickers for portfolio to be optimized"""
        parser = argparse.ArgumentParser(
            add_help=False,
            prog="add/select",
            description="""Add/Select tickers for portfolio to be optimized.""",
        )
        parser.add_argument(
            "-t",
            "--tickers",
            dest="add_tickers",
            type=lambda s: [str(item).upper() for item in s.split(",")],
            default=[],
            help="tickers to be used in the portfolio to optimize.",
        )
        if other_args:
            if "-" not in other_args[0]:
                other_args.insert(0, "-t")

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            tickers = set(self.tickers)
            for ticker in ns_parser.add_tickers:
                tickers.add(ticker)

            if self.tickers:
                console.print(
                    f"\nCurrent Tickers: {('None', ', '.join(tickers))[bool(tickers)]}"
                )

            self.tickers = list(tickers)
            console.print("")

    def rmv_stocks(self, other_args: List[str]):
        """Remove one of the tickers to be optimized"""
        parser = argparse.ArgumentParser(
            add_help=False,
            prog="rmv",
            description="""Remove one of the tickers to be optimized.""",
        )
        parser.add_argument(
            "-t",
            "--tickers",
            dest="rmv_tickers",
            type=lambda s: [str(item).upper() for item in s.split(",")],
            default=[],
            help="tickers to be removed from the tickers to optimize.",
        )
        if other_args:
            if "-" not in other_args[0]:
                other_args.insert(0, "-t")

        ns_parser = parse_known_args_and_warn(parser, other_args)
        if ns_parser:
            tickers = set(self.tickers)
            for ticker in ns_parser.rmv_tickers:
                tickers.remove(ticker)

            if self.tickers:
                console.print(
                    f"\nCurrent Tickers: {('None', ', '.join(tickers))[bool(tickers)]}"
                )

            self.tickers = list(tickers)
            console.print("")
