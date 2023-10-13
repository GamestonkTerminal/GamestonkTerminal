import pytest
import sys

try:
    import polars as pl
except ImportError:
    pass

try:
    import pandas as pd
except ImportError:
    pass

try:
    import numpy as np
except ImportError:
    pass

try:
    from openbb_charting.core.openbb_figure import OpenBBFigure
except ImportError:
    pass


@pytest.fixture(scope="session")
def obb(pytestconfig):
    """Fixture to setup obb."""

    if pytestconfig.getoption("markexpr") != "not integration":
        import openbb

        return openbb.obb


@pytest.mark.skipif("pandas" not in sys.modules, reason="pandas not installed")
@pytest.mark.integration
def test_to_dataframe(obb):
    """Test obbject to dataframe."""

    stocks_df = obb.stocks.load("AAPL", provider="fmp").to_dataframe()
    assert isinstance(stocks_df, pd.DataFrame)


@pytest.mark.skipif("polars" not in sys.modules, reason="polars not installed")
@pytest.mark.integration
def test_to_polars(obb):
    """Test obbject to polars."""

    crypto_pl = obb.crypto.load("BTC-USD", provider="fmp").to_polars()
    assert isinstance(crypto_pl, pl.DataFrame)


@pytest.mark.skipif("numpy" not in sys.modules, reason="numpy not installed")
@pytest.mark.integration
def test_to_numpy(obb):
    """Test obbject to numpy array."""

    cpi_np = obb.economy.cpi(
        countries=["portugal", "spain", "switzerland"], frequency="annual"
    ).to_numpy()
    assert isinstance(cpi_np, np.ndarray)


@pytest.mark.integration
def test_to_dict(obb):
    """Test obbject to dict."""

    fed_dict = obb.fixedincome.fed(start_date="2010-01-01").to_dict()
    assert isinstance(fed_dict, dict)


@pytest.mark.skipif(
    "openbb_charting" not in sys.modules, reason="openbb_charting not installed"
)
@pytest.mark.integration
def test_to_chart(obb):
    """Test obbject to chart."""

    stocks_chart = obb.stocks.load("AAPL", provider="fmp").to_chart()
    assert isinstance(stocks_chart, OpenBBFigure)


@pytest.mark.skipif(
    "openbb_charting" not in sys.modules, reason="openbb_charting not installed"
)
@pytest.mark.integration
def test_show(obb):
    """Test obbject to chart."""

    stocks_data = obb.stocks.load("AAPL", provider="fmp", chart=True)
    assert isinstance(stocks_data.chart.fig, OpenBBFigure)
    assert stocks_data.chart.fig.show() is None
