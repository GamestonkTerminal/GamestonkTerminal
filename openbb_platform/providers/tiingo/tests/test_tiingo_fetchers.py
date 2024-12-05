"""Test Tiingo fetchers."""

from datetime import date

import pytest
from openbb_core.app.service.user_service import UserService
from openbb_tiingo.models.company_news import TiingoCompanyNewsFetcher
from openbb_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from openbb_tiingo.models.currency_historical import TiingoCurrencyHistoricalFetcher
from openbb_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from openbb_tiingo.models.trailing_dividend_yield import TiingoTrailingDivYieldFetcher
from openbb_tiingo.models.websocket_connection import TiingoWebSocketFetcher
from openbb_tiingo.models.world_news import TiingoWorldNewsFetcher

test_credentials = UserService().default_user_settings.credentials.model_dump(
    mode="json"
)


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration."""
    return {
        "filter_headers": [("User-Agent", None)],
        "filter_query_parameters": [
            ("token", "MOCK_TOKEN"),
        ],
    }


@pytest.mark.record_http
def test_tiingo_equity_historical_fetcher(credentials=test_credentials):
    """Test Tiingo equity historical fetcher."""
    params = {
        "symbol": "AAPL",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TiingoEquityHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_company_news_fetcher(credentials=test_credentials):
    """Test Tiingo company news fetcher."""
    params = {"symbol": "AAPL,MSFT"}

    fetcher = TiingoCompanyNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_world_news_fetcher(credentials=test_credentials):
    """Test Tiingo world news fetcher."""
    params = {"limit": 20}

    fetcher = TiingoWorldNewsFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_crypto_historical_fetcher(credentials=test_credentials):
    """Test Tiingo crypto historical fetcher."""
    params = {
        "symbol": "BTCUSD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TiingoCryptoHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_currency_historical_fetcher(credentials=test_credentials):
    """Test Tiingo currency historical fetcher."""
    params = {
        "symbol": "EURUSD",
        "start_date": date(2023, 1, 1),
        "end_date": date(2023, 6, 6),
    }

    fetcher = TiingoCurrencyHistoricalFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_http
def test_tiingo_trailing_div_yield_fetcher(credentials=test_credentials):
    """Test Tiingo trailing dividend yield fetcher."""
    params = {"symbol": "SCHD"}

    fetcher = TiingoTrailingDivYieldFetcher()
    result = fetcher.test(params, credentials)
    assert result is None


@pytest.mark.record_verify_screen(hash=True)
@pytest.mark.record_verify_object(hash=False)
def test_tiingo_websocket_fetcher(record, credentials=test_credentials):
    """Test Tiingo Websocket fetcher."""
    import asyncio
    import time

    params = {
        "symbol": "btcusd",
        "name": "tiingo_test",
        "limit": 10,
        "asset_type": "crypto",
    }

    try:
        fetcher = TiingoWebSocketFetcher()
        response = asyncio.run(fetcher.fetch_data(params, credentials))
        time.sleep(1)
        record.add_verify(response.client.is_running)
        assert response.client.is_running
        time.sleep(1)
        assert len(response.client.results) > 0
        record.add_verify(list(response.client.results[0].model_dump().keys()))
    finally:
        response.client.disconnect()
        assert not response.client.is_running
        record.add_verify(response.client.is_running)
