""" Comparison Analysis Marketwatch View """
__docformat__ = "numpy"


import os
from typing import List

from tabulate import tabulate

from gamestonk_terminal import feature_flags as gtff
from gamestonk_terminal.helper_funcs import export_data, financials_colored_values
from gamestonk_terminal.stocks.comparison_analysis import marketwatch_model


def display_income_comparison(
    ticker: str,
    similar: List[str],
    timeframe: str,
    quarter: bool = False,
    export: str = "",
):
    """Display income data from Marketwatch

    Parameters
    ----------
    ticker : str
        Base ticker
    similar : List[str]
        List of tickers to compare
    timeframe : str
        Whether to use quarterly or annual
    quarter : bool, optional
        Whether to use quarterly statements, by default False
    export : str, optional
        Format to export data
    """
    all_stocks = [ticker, *similar]
    df_financials_compared = marketwatch_model.get_financial_comparisons(
        all_stocks, "income", timeframe, quarter
    )
    # Export data before the color
    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "income",
        df_financials_compared,
    )

    if gtff.USE_COLOR:
        df_financials_compared = df_financials_compared.applymap(
            financials_colored_values
        )

    if not quarter:
        df_financials_compared.index.name = timeframe

    if gtff.USE_TABULATE_DF:
        print(
            tabulate(
                df_financials_compared,
                headers=df_financials_compared.columns,
                showindex=True,
                tablefmt="fancy_grid",
            ),
            "\n",
        )
    else:
        print(df_financials_compared.to_string(), "\n")


def display_balance_comparison(
    ticker: str,
    similar: List[str],
    timeframe: str,
    quarter: bool = False,
    export: str = "",
):
    """Compare balance between companies

    Parameters
    ----------
    ticker : str
        Main ticker to compare income
    similar : List[str]
        Similar companies to compare income with
    timeframe : str
        Whether to use quarterly or annual
    quarter : bool, optional
        Whether to use quarterly statements, by default False
    export : str, optional
        Format to export data
    """
    all_stocks = [ticker, *similar]
    df_financials_compared = marketwatch_model.get_financial_comparisons(
        all_stocks, "balance", timeframe, quarter
    )
    # Export data before the color
    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "balance",
        df_financials_compared,
    )

    if gtff.USE_COLOR:
        df_financials_compared = df_financials_compared.applymap(
            financials_colored_values
        )

    if not quarter:
        df_financials_compared.index.name = timeframe

    if gtff.USE_TABULATE_DF:
        print(
            tabulate(
                df_financials_compared,
                headers=df_financials_compared.columns,
                showindex=True,
                tablefmt="fancy_grid",
            ),
            "\n",
        )
    else:
        print(df_financials_compared.to_string(), "\n")


def display_cashflow_comparison(
    ticker: str,
    similar: List[str],
    timeframe: str,
    quarter: bool = False,
    export: str = "",
):
    """Compare cashflow between companies

    Parameters
    ----------
    ticker : str
        Main ticker to compare income
    similar : List[str]
        Similar companies to compare income with
    timeframe : str
        Whether to use quarterly or annual
    quarter : bool, optional
        Whether to use quarterly statements, by default False
    export : str, optional
        Format to export data
    """
    all_stocks = [ticker, *similar]
    df_financials_compared = marketwatch_model.get_financial_comparisons(
        all_stocks, "cashflow", timeframe, quarter
    )

    # Export data before the color
    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "cashflow",
        df_financials_compared,
    )

    if gtff.USE_COLOR:
        df_financials_compared = df_financials_compared.applymap(
            financials_colored_values
        )

    if not quarter:
        df_financials_compared.index.name = timeframe

    if gtff.USE_TABULATE_DF:
        print(
            tabulate(
                df_financials_compared,
                headers=df_financials_compared.columns,
                showindex=True,
                tablefmt="fancy_grid",
            ),
            "\n",
        )
    else:
        print(df_financials_compared.to_string(), "\n")
