# pylint: disable=C0302, R0911
""" Options Chains Module """
__docformat__ = "numpy"

# IMPORTATION STANDARD
import logging
from copy import deepcopy

# IMPORTATION THIRDPARTY
from typing import Any, Callable, Optional

import numpy as np
import pandas as pd

# IMPORTATION INTERNAL
from openbb_terminal.decorators import log_start_end
from openbb_terminal.stocks.options.cboe_model import load_options as load_cboe
from openbb_terminal.stocks.options.intrinio_model import load_options as load_intrinio
from openbb_terminal.stocks.options.nasdaq_model import load_options as load_nasdaq
from openbb_terminal.stocks.options.tmx_model import load_options as load_tmx
from openbb_terminal.stocks.options.tradier_model import load_options as load_tradier
from openbb_terminal.stocks.options.yfinance_model import load_options as load_yfinance

logger = logging.getLogger(__name__)

SOURCES = ["CBOE", "YahooFinance", "Tradier", "Intrinio", "Nasdaq", "TMX"]

# mypy: disable-error-code="attr-defined, index"


@log_start_end(log=logger)
def load_options_chains(
    symbol: str,
    source: str = "CBOE",
    date: str = "",
    pydantic: bool = False,
) -> object:
    """Loads all options chains from a specific source, fields returned to each attribute will vary.

    Parameters
    ----------
    symbol : str
        The underlying asset's symbol.
    source: str
        The source of the data. Choices are "CBOE", "YahooFinance", "Tradier", "Intrinio", "Nasdaq", or "TMX".
    date: Optional[str]
        The date for the EOD option chain.  Format: YYYY-MM-DD.
        This parameter is only available for "TMX" or "Intrinio".
    pydantic: bool
        Whether to return the object as a Pydantic Model or a subscriptable Pandas object.  Default is False.

    Returns
    -------
    object: OptionsChains data object

        chains: dict
            All options chains data from a specific source.  Returns as a Pandas DataFrame if pydantic is False.
        expirations: list[str]
            List of all unique expiration dates.
        hasGreeks: bool
            True if the source returns greeks with the chains data.
        hasIV: bool
            True if the source returns implied volatility with the chains data.
        last_price: float
            The last price (or the price at the EOD for the date.of the EOD option chain).
        source: str
            The source that was entered in the input.
        strikes: list[float]
            List of all unique strike prices.
        symbol: str
            The symbol that was entered in the input.
        SYMBOLS: pd.DataFrame
            The symbol directory to the selected source, when available.  Only returned when pydantic is False.
        underlying_name: str
            The name of the underlying asset.
        underlying_price: dict
            The underlying asset's price and performance.  Returns as a Pandas Series if pydantic is False.

    Examples
    --------
    Loads SPY data from CBOE, returns as a Pydantic Model, and displays the longest-dated expiration chain.

    >>> from openbb_terminal.sdk import openbb
    >>> import pandas as pd
    >>> data = openbb.stocks.options.load_options_chains("SPY", pydantic = True)
    >>> chains = pd.DataFrame(data.chains)
    >>> chains[chains["expiration"] == data.expirations[-1]]

    Loads QQQ data from Tradier as a Pydantic Model.

    >>> from openbb_terminal.sdk import openbb
    >>> data = openbb.stocks.options.load_options_chains("QQQ", source = "Tradier", pydantic = True)

    Loads VIX data from YahooFinance as a Pandas object.

    >>> from openbb_terminal.sdk import openbb
    >>> data = openbb.stocks.options.load_options_chains("^VIX", source = "YahooFinance")

    Loads XIU data from TMX and displays the 25 highest open interest options.

    >>> from openbb_terminal.sdk  import openbb
    >>> data = openbb.stocks.options.load_options_chains("XIU", "TMX")
    >>> data.chains.sort_values("openInterest", ascending=False).head(25)

    Loads the EOD chains data for XIU.TO from March 15, 2020, sorted by number of transactions.

    >>> from openbb_terminal.sdk  import openbb
    >>> data = openbb.stocks.options.load_options_chains("XIU.TO", "TMX", "2020-03-15")
    >>> data.chains.sort_values("transactions", ascending=False).head(25)
    """

    if source not in SOURCES:
        print("Invalid choice. Choose from: ", list(SOURCES), sep=None)
        return None

    if source == "Nasdaq":
        return load_nasdaq(symbol, pydantic)
    if source == "YahooFinance":
        return load_yfinance(symbol, pydantic)
    if source == "Tradier":
        return load_tradier(symbol, pydantic)
    if source == "TMX":
        if date != "":
            return load_tmx(symbol, date, pydantic)
        return load_tmx(symbol, pydantic=pydantic)
    if source == "Intrinio":
        if date != "":
            return load_intrinio(symbol, date, pydantic)
        return load_intrinio(symbol, pydantic=pydantic)

    return load_cboe(symbol, pydantic)


def validate_object(
    options: object, scope: Optional[str] = "object", days: Optional[int] = None
) -> Any:
    """This is an internal helper function for validating the OptionsChains data object passed
    through the input of functions defined in the OptionsChains class.  The purpose is to handle
    multi-type inputs with backwards compatibility and provide robust error handling.  The return
    is the portion of the object, or a true/false validation, required to perform the operation.

    Parameters
    ----------
    options : object
        The OptionsChains data object.
        Accepts both Pydantic and Pandas object types, as defined by `load_options_chains()`.
        A Pandas DataFrame, or dictionary, with the options chains data is also accepted.
    scope: str
        The scope of the data needing to be validated.  Choices are: ["chains", "object", "strategies", "nonZeroPrices"]
    days: int
        The number of target number of days until the expiration.

    Returns
    -------
    Any:
        if scope == "chains":
            pd.DataFrame
                Pandas DataFrame with the validated data.
        if scope == "object" or scope == "strategies":
            bool
                True if the object is a valid OptionsChains data object.

    Examples
    --------
    Load some data first:
    >>> from openbb_terminal.stocks.options import options_chains_model
    >>> data = options_chains_model.OptionsChains().load_options_chains("SPY")
    To extract just the chains data, use:
    >>> chains = options_chains_model.validate_object(data, scope="chains")
    To pass as a true/false validation, use:
    >>> if options_chains_model.validate_object(data, scope="object") is False:
    >>>     return
    To pass and return the entire object for non-zero prices:
    >>> from copy import deepcopy
    >>> options = deepcopy(data)
    >>> if options_chains_model.validate_object(options, scope="object") is True:
    >>>     options = options_chains_model.validate_object(options, scope="nonZeroPrices")
    """

    scopes = ["chains", "object", "strategies", "nonZeroPrices"]

    valid: bool = True

    if scope == "":
        scope = "chains"

    if scope not in scopes:
        print("Invalid choice.  The supported methods are:", scopes)
        return pd.DataFrame()

    if scope == "object":
        try:
            if isinstance(options.strikes, list) and isinstance(
                options.expirations, list
            ):
                return valid

        except AttributeError:
            print(
                "Error: Invalid data type supplied.  The OptionsChains data object is required.  "
                "Use load_options_chains() first."
            )
            return not valid

    if scope == "strategies":
        try:
            if isinstance(options.last_price, float):
                return valid
        except AttributeError:
            print(
                "`last_price` was not found in the OptionsChainsData object and is required for this operation."
            )
            return not valid

    if scope == "chains":
        try:
            if isinstance(options, pd.DataFrame):
                chains = options.copy()

            if isinstance(options, dict):
                chains = pd.DataFrame(options)

            elif isinstance(options, object) and not isinstance(options, pd.DataFrame):
                chains = (
                    pd.DataFrame(options.chains)  # type: ignore[attr-defined]
                    if isinstance(options.chains, dict)  # type: ignore[attr-defined]
                    else options.chains.copy()  # type: ignore[attr-defined]
                )

                if options is None or chains.empty:
                    print(
                        "No options chains data found in the supplied object.  Use load_options_chains()."
                    )
                    return pd.DataFrame()

            if "openInterest" not in chains.columns:
                print("Expected column, openInterest, not found.")
                return pd.DataFrame()

            if "volume" not in chains.columns:
                print("Expected column, volume, not found.")
                return pd.DataFrame()
        except AttributeError:
            print("Error: Invalid data type supplied.")
            return pd.DataFrame()

        return chains

    if scope == "nonZeroPrices":
        dte_estimate = get_nearest_dte(  # noqa:F841 pylint: disable=unused-variable
            options, days
        )
        # When Intrinio data is not EOD, there is no "ask" column, renaming "close".
        if options.source == "Intrinio" and options.date == "":
            options.chains["ask"] = options.chains["close"]
            options.chains["bid"] = options.chains["close"]

        # Error handling for TMX EOD data when the date is an expiration date.  EOD, 0-day options are excluded.
        if options.source == "TMX" and options.date != "":
            options.chains = options.chains[options.chains["dte"] > 0]

        if (
            options.source == "TMX"
            or options.source == "YahooFinance"
            and options.chains.query("`dte` == @dte_estimate")["ask"].sum() == 0
        ):
            options.chains["ask"] = options.chains["lastPrice"]
        if (
            options.source == "TMX"
            or options.source == "YahooFinance"
            and options.chains.query("`dte` == @dte_estimate")["bid"].sum() == 0
        ):
            options.chains["bid"] = options.chains["lastPrice"]

        return options

    print(
        "Error: No valid data supplied. Check the input to ensure it is not empty or None."
    )

    return not valid


def get_nearest_dte(options: object, days: Optional[int] = 30) -> int:
    """Gets the closest expiration date to the target number of days until expiry.

    Parameters
    ----------
    options : object
        The OptionsChains data object.  Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry.  Default is 30 days.

    Returns
    -------
    int
        The closest expiration date to the target number of days until expiry, expressed as DTE.

    Example
    -------
    >>> from openbb_terminal.stocks.options import options_chains_model
    >>> options = options_chains_model.OptionsChains().load_options_chains("QQQ")
    >>> options_chains_model.get_nearest_dte(options)
    >>> options_chains_model.get_nearest_dte(options, 90)
    """

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    nearest = (options.chains["dte"] - days).abs().idxmin()

    return options.chains.loc[nearest]["dte"]


def get_nearest_call_strike(
    options: object, days: Optional[int] = 30, strike_price: Optional[float] = 0
) -> float:
    """Gets the closest call strike to the target price and number of days until expiry.

    Parameters
    ----------
    options : object
        The OptionsChains data object.  Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry.  Default is 30 days.
    strike_price: float
        The target strike price.  Default is the last price of the underlying stock.

    Returns
    -------
    float
        The closest strike price to the target price and number of days until expiry.

    Example
    -------
    >>> data = OptionsChains().load_options_chains('SPY')
    >>> get_nearest_call_strike(data)
    >>> get_nearest_call_strike(data, 90)
    >>> days = data.chains.dte.unique().tolist()
    >>> for day in days:
    >>>     print(get_nearest_call_strike(data, day))
    """

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    if strike_price == 0:
        strike_price = options.last_price

    dte_estimate = get_nearest_dte(options, days)

    nearest = (
        (
            options.chains[options.chains["dte"] == dte_estimate]
            .query("`optionType` == 'call' and `ask` > 0")
            .convert_dtypes()["strike"]
            - strike_price
        )
        .abs()
        .idxmin()
    )

    return options.chains.loc[nearest]["strike"]


def get_nearest_put_strike(
    options: object, days: Optional[int] = 30, strike_price: Optional[float] = 0
) -> float:
    """Gets the closest put strike to the target price and number of days until expiry.

    Parameters
    ----------
    options : object
        The OptionsChains data object.  Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry.  Default is 30 days.
    strike_price: float
        The target strike price.  Default is the last price of the underlying stock.

    Returns
    -------
    float
        The closest strike price to the target price and number of days until expiry.

    Example
    -------
    >>> data = OptionsChains().load_options_chains('SPY')
    >>> get_nearest_put_strike(data)
    >>> get_nearest_put_strike(data, 90)
    >>> days = data.chains.dte.unique().tolist()
    >>> for day in days:
    >>>     print(get_nearest_put_strike(data, day))
    """

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    if strike_price == 0:
        strike_price = options.last_price

    dte_estimate = get_nearest_dte(options, days)

    nearest = (
        (
            options.chains[options.chains["dte"] == dte_estimate]
            .query("`optionType` == 'put' and `ask` > 0")
            .convert_dtypes()["strike"]
            - strike_price
        )
        .abs()
        .idxmin()
    )

    return options.chains.loc[nearest]["strike"]


def get_nearest_otm_strike(
    options: object, moneyness: Optional[float] = 5
) -> dict[str, float]:
    """Gets the nearest put and call strikes at a given percent OTM from the underlying price.

    Parameters
    ----------
    options : OptionsChains
        The OptionsChains data object.  Use load_options_chains() to load the data.
    moneyness: float
        The target percent OTM, expressed as a percent between 0 and 100.  Default is 5.

    Returns
    -------
    dict[str, float]
        Dictionary of the upper (call) and lower (put) strike prices.

    Example
    -------
    >>> from openbb_terminal.stocks.options import options_chains_model
    >>> data = options_chains_model.OptionsChains().load_options_chains('SPY')
    >>> strikes = options_chains_model.get_nearest_otm_strike(data)
    """

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    if not moneyness:
        moneyness = 5

    if 0 < moneyness < 100:
        moneyness = moneyness / 100

    if moneyness > 100 or moneyness < 0:
        print("Error: Moneyness must be expressed as a percentage between 0 and 100")
        return {}

    upper = options.last_price * (1 + moneyness)
    lower = options.last_price * (1 - moneyness)
    strikes = pd.Series(options.strikes)
    nearest_call = (upper - strikes).abs().idxmin()
    call = strikes[nearest_call]
    nearest_putt = (lower - strikes).abs().idxmin()
    put = strikes[nearest_putt]

    otmStrikes = {"call": call, "put": put}

    return otmStrikes


def calculate_straddle(
    options: object,
    days: Optional[int] = 30,
    strike: float = 0,
) -> pd.DataFrame:
    """Calculates the cost of a straddle and its payoff profile. Use a negative strike price for short options.
    Requires the OptionsChains data object.

    Parameters
    ----------
    options : object
        The OptionsChains data object. Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry. Default is 30 days.
    strike: float
        The target strike price. Enter a negative value for short options.
        Default is the last price of the underlying stock.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with the results. Strike1 is the nearest call strike, strike2 is the nearest put strike.

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> data = openbb.stocks.options.load_options_chains('SPY')
    >>> openbb.stocks.options.calculate_straddle(data)
    """
    options = deepcopy(options)
    if not days:
        days = 30

    short: bool = False
    if strike is not None and strike < 0:
        short = True
    strike_price = abs(strike)

    bidAsk = "bid" if short else "ask"  # noqa:F841

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    dte_estimate = get_nearest_dte(options, days)  # noqa:F841

    options = validate_object(options, "nonZeroPrices", dte_estimate)

    if not strike_price:
        strike_price = options.last_price

    call_strike_estimate = get_nearest_call_strike(
        options, dte_estimate, strike_price
    )  # noqa:F841
    put_strike_estimate = get_nearest_put_strike(
        options, dte_estimate, strike_price
    )  # noqa:F841

    call_premium = options.chains.query(
        "`strike` == @call_strike_estimate and `dte` == @dte_estimate and `optionType` == 'call'"
    )[bidAsk].values

    put_premium = options.chains.query(
        "`strike` == @put_strike_estimate and `dte` == @dte_estimate and `optionType` == 'put'"
    )[bidAsk].values

    straddle_cost = call_premium + put_premium

    straddle = {}

    # Include the as-of date if the data is historical EOD.
    if (
        options.source == "Intrinio"
        and options.date != ""
        or options.source == "TMX"
        and options.date != ""
    ):
        straddle.update({"Date": options.date})

    straddle.update(
        {
            "Symbol": options.symbol,
            "Underlying Price": options.last_price,
            "Expiration": options.chains.query("`dte` == @dte_estimate")[
                "expiration"
            ].unique()[0],
            "DTE": dte_estimate,
            "Strike 1": call_strike_estimate,
            "Strike 2": put_strike_estimate,
            "Strike 1 Premium": call_premium[0],
            "Strike 2 Premium": put_premium[0],
            "Cost": straddle_cost[0] * -1 if short else straddle_cost[0],
            "Cost Percent": round(
                straddle_cost[0] / options.last_price * 100, ndigits=4
            ),
            "Breakeven Upper": call_strike_estimate + straddle_cost[0],
            "Breakeven Upper Percent": round(
                (call_strike_estimate + straddle_cost[0]) / options.last_price * 100,
                ndigits=4,
            )
            - 100,
            "Breakeven Lower": put_strike_estimate - straddle_cost[0],
            "Breakeven Lower Percent": -100
            + round(
                (put_strike_estimate - straddle_cost[0]) / options.last_price * 100,
                ndigits=4,
            ),
            "Max Profit": abs(straddle_cost[0]) if short else np.inf,
            "Max Loss": np.inf if short else straddle_cost[0] * -1,
        }
    )

    straddle = pd.DataFrame(data=straddle.values(), index=straddle.keys()).rename(
        columns={0: "Short Straddle" if short else "Long Straddle"}
    )

    straddle.loc["Payoff Ratio"] = round(
        abs(straddle.loc["Max Profit"][0] / straddle.loc["Max Loss"][0]), ndigits=4
    )

    return straddle


def calculate_strangle(
    options: object,
    days: Optional[int] = 30,
    moneyness: Optional[float] = 5,
) -> pd.DataFrame:
    """Calculates the cost of a straddle and its payoff profile.  Use a negative value for moneyness for short options.

    Requires the OptionsChains data object.

    Parameters
    ----------
    options : object
        The OptionsChains data object.  Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry.  Default is 30 days.
    moneyness: float
        The percentage of OTM moneyness, expressed as a percent between -100 < 0 < 100.
        Enter a negative number for short options.
        Default is 5.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with the results. Strike 1 is the nearest call strike, and strike 2 is the nearest put strike.

    Examples
    --------
    >>> from openbb_terminal.sdk import openbb
    >>> data = openbb.stocks.options.load_options_chains('SPY')
    >>> openbb.stocks.options.calculate_strangle(data)
    """
    options = deepcopy(options)

    if not days:
        days = 30

    if not moneyness:
        moneyness = 5

    short: bool = False

    if moneyness < 0:
        short = True
    moneyness = abs(moneyness)
    bidAsk = "bid" if short else "ask"  # noqa:F841

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    dte_estimate = get_nearest_dte(options, days)  # noqa:F841

    options = validate_object(options, "nonZeroPrices", dte_estimate)

    if moneyness > 100 or moneyness < 0:
        print("Error: Moneyness must be between 0 and 100.")
        return pd.DataFrame()

    strikes = get_nearest_otm_strike(options, moneyness)

    call_strike_estimate = get_nearest_call_strike(
        options, dte_estimate, strikes["call"]
    )  # noqa:F841
    put_strike_estimate = get_nearest_put_strike(
        options, dte_estimate, strikes["put"]
    )  # noqa:F841

    call_premium = options.chains.query(
        "`strike` == @call_strike_estimate and `dte` == @dte_estimate and `optionType` == 'call'"
    )[bidAsk].values

    put_premium = options.chains.query(
        "`strike` == @put_strike_estimate and `dte` == @dte_estimate and `optionType` == 'put'"
    )[bidAsk].values

    strangle_cost = call_premium + put_premium

    strangle = {}

    # Includees the as-of date if it is historical EOD data.
    if (
        options.source == "Intrinio"
        and options.date != ""
        or options.source == "TMX"
        and options.date != ""
    ):
        strangle.update({"Date": options.date})

    strangle.update(
        {
            "Symbol": options.symbol,
            "Underlying Price": options.last_price,
            "Expiration": options.chains.query("`dte` == @dte_estimate")[
                "expiration"
            ].unique()[0],
            "DTE": dte_estimate,
            "Strike 1": call_strike_estimate,
            "Strike 2": put_strike_estimate,
            "Strike 1 Premium": call_premium[0],
            "Strike 2 Premium": put_premium[0],
            "Cost": strangle_cost[0] * -1 if short else strangle_cost[0],
            "Cost Percent": round(
                strangle_cost[0] / options.last_price * 100, ndigits=4
            ),
            "Breakeven Upper": call_strike_estimate + strangle_cost[0],
            "Breakeven Upper Percent": round(
                (call_strike_estimate + strangle_cost[0]) / options.last_price * 100,
                ndigits=4,
            )
            - 100,
            "Breakeven Lower": put_strike_estimate - strangle_cost[0],
            "Breakeven Lower Percent": -100
            + round(
                (put_strike_estimate - strangle_cost[0]) / options.last_price * 100,
                ndigits=4,
            ),
            "Max Profit": abs(strangle_cost[0]) if short else np.inf,
            "Max Loss": np.inf if short else strangle_cost[0] * -1,
        }
    )

    strangle = pd.DataFrame(data=strangle.values(), index=strangle.keys()).rename(
        columns={0: "Short Strangle" if short else "Long Strangle"}
    )

    strangle.loc["Payoff Ratio"] = round(
        abs(strangle.loc["Max Profit"][0] / strangle.loc["Max Loss"][0]), ndigits=4
    )

    return strangle


def calculate_vertical_call_spread(
    options: object,
    days: Optional[int] = 30,
    sold_strike: Optional[float] = 0,
    bought_strike: Optional[float] = 0,
) -> pd.DataFrame:
    """Calculates the vertical call spread for the target DTE.
    A bull call spread is when the sold strike is above the bought strike.

    Parameters
    ----------
    options : object
        The OptionsChains data object. Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry. This value will be used to get the nearest valid DTE.
        Default is 30 days.
    sold_strike: float
        The target strike price for the short leg of the vertical call spread.
        Default is the 5% OTM above the last price of the underlying.
    bought_strike: float
        The target strike price for the long leg of the vertical call spread. Default is the last price of the underlying.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with the results. Strike 1 is the sold strike, and strike 2 is the bought strike.

    Examples
    --------
    Load the data:
    >>> from openbb_terminal.stocks.options.options_chains_model import OptionsChains()
    >>> op = OptionsChains()
    >>> data = op.load_options_chains("QQQ")

    For a bull call spread:
    >>> op.calculate_vertical_call_spread(data, days=10, sold_strike=355, bought_strike=350)

    For a bear call spread:
    >>> op.calculate_vertical_call_spread(data, days=10, sold_strike=350, bought_strike=355)
    """
    options = deepcopy(options)

    if not days:
        days = 30

    if not bought_strike:
        bought_strike = options.last_price * 1.0250

    if not sold_strike:
        sold_strike = options.last_price * 1.0750

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    dte_estimate = get_nearest_dte(options, days)  # noqa:F841

    options = validate_object(options, "nonZeroPrices", dte_estimate)

    sold = get_nearest_call_strike(options, days, sold_strike)
    bought = get_nearest_call_strike(options, days, bought_strike)

    sold_premium = options.chains.query(
        "`strike` == @sold and `dte` == @dte_estimate and `optionType` == 'call'"
    )["bid"].values
    bought_premium = options.chains.query(
        "`strike` == @bought and `dte` == @dte_estimate and `optionType` == 'call'"
    )["ask"].values

    spread_cost = bought_premium - sold_premium
    breakeven_price = bought + spread_cost[0]
    max_profit = sold - bought - spread_cost[0]
    call_spread_ = {}
    if sold != bought and spread_cost != 0:
        # Includees the as-of date if it is historical EOD data.
        if (
            options.source == "Intrinio"
            and options.date != ""
            or options.source == "TMX"
            and options.date != ""
        ):
            call_spread_.update({"Date": options.date})

        call_spread_.update(
            {
                "Symbol": options.symbol,
                "Underlying Price": options.last_price,
                "Expiration": options.chains.query("`dte` == @dte_estimate")[
                    "expiration"
                ].unique()[0],
                "DTE": dte_estimate,
                "Strike 1": sold,
                "Strike 2": bought,
                "Strike 1 Premium": sold_premium[0],
                "Strike 2 Premium": bought_premium[0],
                "Cost": spread_cost[0],
                "Cost Percent": round(
                    spread_cost[0] / options.last_price * 100, ndigits=4
                ),
                "Breakeven Lower": breakeven_price,
                "Breakeven Lower Percent": round(
                    (breakeven_price / options.last_price * 100) - 100, ndigits=4
                ),
                "Breakeven Upper": np.nan,
                "Breakeven Upper Percent": np.nan,
                "Max Profit": max_profit,
                "Max Loss": spread_cost[0] * -1,
            }
        )

        call_spread = pd.DataFrame(
            data=call_spread_.values(), index=call_spread_.keys()
        ).rename(columns={0: "Bull Call Spread"})
        if call_spread.loc["Cost"][0] < 0:
            call_spread.loc["Max Profit"][0] = call_spread.loc["Cost"][0] * -1
            call_spread.loc["Max Loss"][0] = -1 * (
                bought - sold + call_spread.loc["Cost"][0]
            )
            lower = bought if sold > bought else sold
            call_spread.loc["Breakeven Upper"][0] = (
                lower + call_spread.loc["Max Profit"][0]
            )
            call_spread.loc["Breakeven Upper Percent"][0] = round(
                (breakeven_price / options.last_price * 100) - 100, ndigits=4
            )
            call_spread.loc["Breakeven Lower"][0] = np.nan
            call_spread.loc["Breakeven Lower Percent"][0] = np.nan
            call_spread.rename(
                columns={"Bull Call Spread": "Bear Call Spread"}, inplace=True
            )

        call_spread.loc["Payoff Ratio"] = round(
            abs(call_spread.loc["Max Profit"][0] / call_spread.loc["Max Loss"][0]),
            ndigits=4,
        )

        return call_spread
    return pd.DataFrame()


def calculate_vertical_put_spread(
    options: object,
    days: Optional[int] = 30,
    sold_strike: Optional[float] = 0,
    bought_strike: Optional[float] = 0,
) -> pd.DataFrame:
    """Calculates the vertical put spread for the target DTE.
    A bear put spread is when the bought strike is above the sold strike.

    Parameters
    ----------
    options : object
        The OptionsChains data object. Use load_options_chains() to load the data.
    days: int
        The target number of days until expiry. This value will be used to get the nearest valid DTE.
        Default is 30 days.
    sold_strike: float
        The target strike price for the short leg of the vertical put spread. Default is the last price of the underlying.
    bought_strike: float
        The target strike price for the long leg of the vertical put spread.
        Default is the 5% OTM above the last price of the underlying.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with the results. Strike 1 is the sold strike, strike 2 is the bought strike.

    Examples
    --------
    Load the data:
    >>> from openbb_terminal.stocks.options.options_chains_model import OptionsChains()
    >>> op = OptionsChains()
    >>> data = op.load_options_chains("QQQ")

    For a bull put spread:
    >>> op.calculate_vertical_put_spread(data, days=10, sold_strike=355, bought_strike=350)

    For a bear put spread:
    >>> op.calculate_vertical_put_spread(data, days=10, sold_strike=355, bought_strike=350)
    """
    options = deepcopy(options)

    if not days:
        days = 30

    if not bought_strike:
        bought_strike = options.last_price * 0.9750

    if not sold_strike:
        sold_strike = options.last_price * 0.9250

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    dte_estimate = get_nearest_dte(options, days)  # noqa:F841
    options = validate_object(options, "nonZeroPrices", dte_estimate)
    sold = get_nearest_put_strike(options, days, sold_strike)
    bought = get_nearest_put_strike(options, days, bought_strike)

    sold_premium = options.chains.query(
        "`strike` == @sold and `dte` == @dte_estimate and `optionType` == 'put'"
    )["bid"].values
    bought_premium = options.chains.query(
        "`strike` == @bought and `dte` == @dte_estimate and `optionType` == 'put'"
    )["ask"].values

    spread_cost = bought_premium - sold_premium
    max_profit = abs(spread_cost[0])
    breakeven_price = sold - max_profit
    max_loss = (sold - bought - max_profit) * -1
    put_spread_ = {}
    if sold != bought and max_loss != 0:
        # Includees the as-of date if it is historical EOD data.
        if (
            options.source == "Intrinio"
            and options.date != ""
            or options.source == "TMX"
            and options.date != ""
        ):
            put_spread_.update({"Date": options.date})

        put_spread_.update(
            {
                "Symbol": options.symbol,
                "Underlying Price": options.last_price,
                "Expiration": options.chains.query("`dte` == @dte_estimate")[
                    "expiration"
                ].unique()[0],
                "DTE": dte_estimate,
                "Strike 1": sold,
                "Strike 2": bought,
                "Strike 1 Premium": sold_premium[0],
                "Strike 2 Premium": bought_premium[0],
                "Cost": spread_cost[0],
                "Cost Percent": round(max_profit / options.last_price * 100, ndigits=4),
                "Breakeven Lower": np.nan,
                "Breakeven Lower Percent": np.nan,
                "Breakeven Upper": breakeven_price,
                "Breakeven Upper Percent": (
                    100 - round((breakeven_price / options.last_price) * 100, ndigits=4)
                ),
                "Max Profit": max_profit,
                "Max Loss": max_loss,
            }
        )

        put_spread = pd.DataFrame(
            data=put_spread_.values(), index=put_spread_.keys()
        ).rename(columns={0: "Bull Put Spread"})
        if put_spread.loc["Cost"][0] > 0:
            put_spread.loc["Max Profit"][0] = bought - sold - spread_cost[0]
            put_spread.loc["Max Loss"][0] = spread_cost[0] * (-1)
            put_spread.loc["Breakeven Lower"][0] = bought - spread_cost[0]
            put_spread.loc["Breakeven Lower Percent"][0] = 100 - round(
                (breakeven_price / options.last_price) * 100, ndigits=4
            )
            put_spread.loc["Breakeven Upper"][0] = np.nan
            put_spread.loc["Breakeven Upper Percent"][0] = np.nan
            put_spread.rename(
                columns={"Bull Put Spread": "Bear Put Spread"}, inplace=True
            )

        put_spread.loc["Payoff Ratio"] = round(
            abs(put_spread.loc["Max Profit"][0] / put_spread.loc["Max Loss"][0]),
            ndigits=4,
        )

        return put_spread
    return pd.DataFrame()


@log_start_end(log=logger)
def calculate_stats(options: object, by: Optional[str] = "expiration") -> pd.DataFrame:
    """Calculates basic statistics for the options chains, like OI and Vol/OI ratios.

    Parameters
    ----------
    options : object
        The OptionsChains data object.
        Accepts both Pydantic and Pandas object types, as defined by `load_options_chains()`.
        A Pandas DataFrame, or dictionary, with the options chains data is also accepted.
    by: str
        Whether to calculate by strike or expiration.  Default is expiration.

    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with the calculated statistics.

    Examples
    --------
    >>> from openbb_terminal.stocks.options.options_chains_model import OptionsChains
    >>> data = OptionsChains().load_options_chains("SPY")
    >>> OptionsChains().calculate_stats(data)
    >>> OptionsChains().calculate_stats(data, "strike")
    >>> OptionsChains().calculate_stats(data.chains, "expiration")
    """

    if by not in ["expiration", "strike"]:
        print("Invalid choice.  The supported methods are: [expiration, strike]")
        return pd.DataFrame()

    chains = deepcopy(options)
    last_price = chains.last_price if hasattr(chains, "last_price") else None
    chains = validate_object(chains, scope="chains")

    if chains.empty or chains is None:
        return chains == pd.DataFrame()

    stats = pd.DataFrame()

    stats["Puts OI"] = (
        chains[chains["optionType"] == "put"]
        .groupby(f"{by}")[["openInterest"]]
        .sum(numeric_only=True)
        .astype(int)
    )
    stats["Calls OI"] = (
        chains[chains["optionType"] == "call"]
        .groupby(f"{by}")[["openInterest"]]
        .sum(numeric_only=True)
        .astype(int)
    )
    stats["Total OI"] = stats["Calls OI"] + stats["Puts OI"]
    stats["OI Ratio"] = round(stats["Puts OI"] / stats["Calls OI"], 2)

    if by == "expiration" and last_price:
        stats["Puts OTM"] = (
            chains.query("`optionType` == 'put' & `strike` < @last_price")
            .groupby("expiration")[["openInterest"]]
            .sum(numeric_only=True)
        )
        stats["Calls OTM"] = (
            chains.query("`optionType` == 'call' & `strike` > @last_price")
            .groupby("expiration")[["openInterest"]]
            .sum(numeric_only=True)
        )
        stats["Puts ITM"] = (
            chains.query("`optionType` == 'put' & `strike` > @last_price")
            .groupby("expiration")[["openInterest"]]
            .sum(numeric_only=True)
        )
        stats["Calls ITM"] = (
            chains.query("`optionType` == 'call' & `strike` < @last_price")
            .groupby("expiration")[["openInterest"]]
            .sum(numeric_only=True)
        )
        stats["OTM Ratio"] = round(stats["Puts OTM"] / stats["Calls OTM"], 2)
        stats["ITM Percent"] = round(
            (stats["Puts ITM"] + stats["Calls ITM"]) / stats["Total OI"] * 100, 2
        )
        if last_price:
            straddle_cost = (
                get_strategies(options, straddle_strike=last_price)
                .rename(columns={"expiration": "Expiration"})
                .set_index("Expiration")[["Cost"]]
            )
            stats["Straddle Cost"] = straddle_cost

    stats["Puts Volume"] = (
        chains[chains["optionType"] == "put"]
        .groupby(f"{by}")[["volume"]]
        .sum(numeric_only=True)
        .astype(int)
    )
    stats["Calls Volume"] = (
        chains[chains["optionType"] == "call"]
        .groupby(f"{by}")
        .sum(numeric_only=True)[["volume"]]
        .astype(int)
    )
    stats["Total Volume"] = stats["Calls Volume"] + stats["Puts Volume"]
    stats["Volume Ratio"] = round(stats["Puts Volume"] / stats["Calls Volume"], 2)
    stats["Vol-OI Ratio"] = round(stats["Total Volume"] / stats["Total OI"], 2)

    if by == "strike":
        stats.rename_axis("Strike", inplace=True)
    stats.rename_axis("Expiration", inplace=True)

    return stats.replace([np.nan, np.inf], "")


@log_start_end(log=logger)
def get_strategies(
    options: object,
    days: Optional[list[int]] = None,
    straddle_strike: Optional[float] = 0,
    strangle_moneyness: Optional[list[float]] = None,
    vertical_calls: Optional[list[float]] = None,
    vertical_puts: Optional[list[float]] = None,
) -> pd.DataFrame:
    """Gets options strategies for all, or a list of, DTE(s).
    Currently supports straddles, strangles, and vertical spreads.
    Multiple strategies, expirations, and % moneyness can be returned.
    To get short options, use a negative value for the `straddle_strike` price or `strangle_moneyness`.
    A sold call strike that is lower than the bought strike, or a sold put strike that is higher than the bought strike,
    is a bearish vertical spread.

    Parameters
    ----------
    options: object
        The OptionsChains data object. Use `load_options_chains()` to load the data.
    days: list[int]
        List of DTE(s) to get strategies for. Enter a single value, or multiple as a list. Defaults to all.
    strike_price: float
        The target strike price. Defaults to the last price of the underlying stock.
    strangle_moneyness: list[float]
        List of OTM moneyness to target, expressed as a percent value between 0 and 100.
        Enter a single value, or multiple as a list. Defaults to 5.
    vertical_calls: list[float]
        Call strikes for vertical spreads, listed as [sold strike, bought strike].
    vertical_puts: list[float]
        Put strikes for vertical spreads, listed as [sold strike, bought strike].
    Returns
    -------
    pd.DataFrame
        Pandas DataFrame with the results.

    Examples
    --------
    Load data
    >>> from openbb_terminal.stocks.options.options_chains_model import OptionsChains
    >>> op = OptionsChains()
    >>> data = op.load_options_chains("SPY")

    Return just straddles
    >>> op.get_strategies(data)

    Return strangles
    >>> op.get_strategies(data)

    Return multiple values for both moneness and days:
    >>> op.get_strategies(data, days = [10,30,60,90], moneyness = [2.5,-5,10,-20])

    Return vertical spreads for all expirations.
    >>> op.get_strategies(data, vertical_calls=[430,427], vertical_puts=[420,426])
    """
    if strangle_moneyness is None:
        strangle_moneyness = [0.0]
    if days is None:
        days = options.chains["dte"].unique().tolist()

    options = deepcopy(options)

    # Allows a single input to be passed instead of a list.
    days = [days] if isinstance(days, int) else days  # type: ignore[list-item]

    if not isinstance(vertical_calls, (list, float)) and vertical_calls is not None:
        print(
            "Two strike prices are required. Enter the sold price first, then the bought price."
        )
        return pd.DataFrame()
    if not isinstance(vertical_puts, (list, float)) and vertical_puts is not None:
        print(
            "Two strike prices are required. Enter the sold price first, then the bought price."
        )
        return pd.DataFrame()

    if strangle_moneyness:
        strangle_moneyness = (
            [strangle_moneyness]  # type: ignore[list-item]
            if not isinstance(strangle_moneyness, list)
            else strangle_moneyness
        )

    if validate_object(options, scope="object") is False:
        return pd.DataFrame()

    if validate_object(options, scope="strategies") is False:
        print("`last_price` was not found in the OptionsChain data object.")
        return pd.DataFrame()

    if isinstance(options.chains, dict):
        options.chains = pd.DataFrame(options.chains)

    days_list = []

    strategies = pd.DataFrame()
    straddles = pd.DataFrame()
    strangles = pd.DataFrame()
    strangles_ = pd.DataFrame()
    call_spreads = pd.DataFrame()
    put_spreads = pd.DataFrame()

    for day in days:
        days_list.append(get_nearest_dte(options, day))
    days = list(set(days_list))

    if vertical_calls:
        cStrike1 = vertical_calls[0]
        cStrike2 = vertical_calls[1]
        for day in days:
            call_spread = calculate_vertical_call_spread(
                options, day, cStrike1, cStrike2
            ).transpose()
            call_spreads = pd.concat([call_spreads, call_spread])

    if vertical_puts:
        pStrike1 = vertical_puts[0]
        pStrike2 = vertical_puts[1]
        for day in days:
            put_spread = calculate_vertical_put_spread(
                options, day, pStrike1, pStrike2
            ).transpose()
            put_spreads = pd.concat([put_spreads, put_spread])

    if straddle_strike:
        straddle_strike = (
            options.last_price if straddle_strike == 0 else straddle_strike
        )
        for day in days:
            straddles = pd.concat(
                [
                    straddles,
                    calculate_straddle(options, day, straddle_strike).transpose(),
                ]
            )

    if strangle_moneyness and strangle_moneyness[0] != 0:
        for day in days:
            for moneyness in strangle_moneyness:
                strangles_ = pd.concat(
                    [
                        strangles_,
                        calculate_strangle(options, day, moneyness).transpose(),
                    ]
                )
        strangles = pd.concat([strangles, strangles_])
        strangles = strangles.query("`Strike 1` != `Strike 2`").drop_duplicates()

    strategies = pd.concat([straddles, strangles, call_spreads, put_spreads])

    if strategies.empty:
        print("No strategy was selected, returning all ATM straddles.")
        return get_strategies(options, straddle_strike=options.last_price)

    strategies = strategies.reset_index().rename(columns={"index": "Strategy"})
    strategies = (
        strategies.set_index(["Expiration", "DTE"])
        .sort_index()
        .drop(columns=["Symbol"])
    )
    return strategies.reset_index()


class OptionsChains:  # pylint: disable=too-few-public-methods
    """OptionsChains class for loading and interacting with the OptionsChains data object.
    Use `load_options_chains()` to load the data to a variable and then feed the object to
    the input of the other functions.

    Attributes
    ----------
    load_options_chains: Callable
        Function for loading the OptionsChains data object for all data sources.
    calculate_stats: Callable
        Function to return a table of summary statistics, by strike or by expiration.
    calculate_straddle: Callable
        Function to calculate straddles and generate an optional table with the payoff profile.
    calculate_strangle: Callable
        Function to calculate strangles and generate an optional table with the payoff profile.
    get_strategies: Callable
        Function for calculating multiple straddles and strangles at different expirations and moneyness.
    """

    def __init__(self) -> None:
        self.load_options_chains: Callable = load_options_chains
        self.calculate_stats: Callable = calculate_stats
        self.calculate_vertical_call_spread: Callable = calculate_vertical_call_spread
        self.calculate_vertical_put_spread: Callable = calculate_vertical_put_spread
        self.calculate_straddle: Callable = calculate_straddle
        self.calculate_strangle: Callable = calculate_strangle
        self.get_strategies: Callable = get_strategies
