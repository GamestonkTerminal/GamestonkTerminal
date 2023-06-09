# IMPORTATION STANDARD

# IMPORTATION THIRDPARTY
import pandas as pd
import pytest

# IMPORTATION INTERNAL
from openbb_terminal.stocks.options import tmx_model

# pylint: disable=no-member


@pytest.mark.vcr
def test_underlying_price():
    result_df = tmx_model.get_underlying_price("XIU")
    assert isinstance(result_df, pd.Series)
    assert "price" in result_df.index
    result_df2 = tmx_model.load_options("XIU", pydantic=True)
    assert result_df["price"] == result_df2.last_price
    assert hasattr(result_df2, "underlying_price")
    assert isinstance(result_df2.underlying_price, dict)
    assert result_df2.underlying_price["price"] == result_df["price"]


@pytest.mark.record_stdout
def test_underlying_price_bad_symbol():
    result_df = tmx_model.get_underlying_price("BAD_SYMBOL")
    assert result_df.empty


@pytest.mark.vcr
def test_underlying_name():
    ticker = tmx_model.Chains().get_chains("BAM")
    assert hasattr(ticker, "underlying_name")
    assert isinstance(ticker.underlying_name, str)
    assert ticker.underlying_name != "BAM"


@pytest.mark.vcr
def test_check_symbol():
    ticker = tmx_model.Chains()
    result_df = ticker.check_symbol("BAD_SYMBOL")
    assert isinstance(result_df, bool)
    result_df2 = ticker.check_symbol("CM")
    assert result_df2 is True


@pytest.mark.vcr
def test_last_price():
    ticker = tmx_model.load_options("AC")
    assert hasattr(ticker, "last_price")
    assert isinstance(ticker.last_price, float)
    ticker2 = tmx_model.load_options("AC", "2021-12-28")
    assert hasattr(ticker2, "last_price")
    assert isinstance(ticker2.last_price, float)
    assert ticker.last_price != ticker2.last_price


@pytest.mark.vcr
def test_chains():
    ticker = tmx_model.Chains().get_chains("BMO")
    assert hasattr(ticker, "chains")
    assert isinstance(ticker.chains, pd.DataFrame)
    ticker = tmx_model.load_options("BMO", pydantic=True)
    assert hasattr(ticker, "chains")
    assert isinstance(ticker.chains, dict)
    assert ticker.hasGreeks is False


@pytest.mark.vcr
def test_strikes():
    ticker = tmx_model.Chains().get_chains("RY")
    assert hasattr(ticker, "strikes")
    assert isinstance(ticker.strikes, list)
    assert isinstance(ticker.strikes[0], float)
    assert ticker.strikes[-1] == max(ticker.chains["strike"])


@pytest.mark.vcr
def test_eodchains_holiday():
    ticker = tmx_model.Chains().get_eodchains("SU", "2018-12-25")
    assert not ticker.chains.empty
    ticker1 = tmx_model.Chains().get_eodchains("SU", "2020-07-01")
    assert hasattr(ticker1, "date")
    assert ticker1.date != "2020-07-01"


@pytest.mark.vcr
def test_expirations():
    ticker = tmx_model.Chains().get_chains("VFV")
    assert hasattr(ticker, "expirations")
    results1 = ticker.expirations
    assert isinstance(results1, list)
    ticker.get_eodchains("VFV", "2021-12-28")
    results_df2 = ticker.expirations
    assert isinstance(results_df2, list)
    assert results1 != results_df2


@pytest.mark.vcr
def test_SYMBOLS():
    ticker = tmx_model.Chains()
    results_df = ticker.SYMBOLS
    assert not results_df.empty
    assert "RY" in results_df.index


@pytest.mark.vcr
def test_hasGreeks_hasIV():
    ticker = tmx_model.Chains()
    assert ticker.chains.empty
    ac = tmx_model.load_options("AC")
    assert ac.hasGreeks is False
    assert ac.hasIV is False
    ac2 = tmx_model.load_options("AC", "2022-01-03")
    assert ac2.hasIV
    assert ac2.hasGreeks is False
