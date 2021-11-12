"""Finance Database view"""
__docformat__ = "numpy"
# pylint:disable=too-many-arguments

import financedatabase as fd
import pandas as pd
from tabulate import tabulate
from gamestonk_terminal import feature_flags as gtff


def show_equities(
    country: str,
    sector: str,
    industry: str,
    name: str,
    description: str,
    marketcap: str,
    amount: int,
    include_exchanges: bool,
    options: str,
):
    """
    Display a selection of Equities based on country, sector, industry, name and/or description filtered
    by market cap. If no arguments are given, return the equities with the highest market cap.
    [Source: Finance Database]

    Parameters
    ----------
    country: str
        Search by country to find stocks matching the criteria.
    sector : str
        Search by sector to find stocks matching the criteria.
    industry : str
        Search by industry to find stocks matching the criteria.
    name : str
        Search by name to find stocks matching the criteria.
    description : str
        Search by description to find stocks matching the criteria.
    amount : int
        Number of stocks to display, default is 10.
    include_exchanges: bool
        When you wish to include different exchanges use this boolean.
    options : str
        Show the country, sector or industry options.
    """
    if options is not None:
        for option in fd.show_options("equities", options):
            print(option)
        return

    if country is not None:
        country = " ".join(country).title()
    if sector is not None:
        sector = " ".join(sector).title()
    if industry is not None:
        industry = " ".join(industry).title()

    data = fd.select_equities(
        country=country,
        sector=sector,
        industry=industry,
        exclude_exchanges=include_exchanges,
    )

    if name is not None:
        data = fd.search_products(data, query=" ".join(name), search="long_name")
    if description is not None:
        data = fd.search_products(data, query=" ".join(description), search="summary")
    if marketcap is not None:
        marketcap = " ".join(marketcap).title()
        if marketcap not in ["Small Cap", "Mid Cap", "Large Cap"]:
            raise ValueError(
                f"Invalid choice ({marketcap}) for -mc/--marketcap. Choose from 'Small Cap', "
                f"'Mid Cap' or 'Large Cap'."
            )
        data = fd.search_products(data, query=marketcap, search="market_cap")

    tabulate_data = pd.DataFrame(data).T[
        [
            "long_name",
            "sector",
            "industry",
            "country",
            "city",
            "website",
            "market_cap",
        ]
    ]

    if gtff.USE_TABULATE_DF:
        print(
            tabulate(
                tabulate_data.iloc[:amount],
                showindex=True,
                headers=[
                    "Name",
                    "Sector",
                    "Industry",
                    "Country",
                    "City",
                    "Website",
                    "Market Cap",
                ],
                floatfmt=".2f",
                tablefmt="fancy_grid",
            ),
            "\n",
        )
    else:
        print(tabulate_data.iloc[:amount].to_string(), "\n")
