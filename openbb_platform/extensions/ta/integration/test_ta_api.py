import json
import random
from typing import List

import pytest
import requests
from openbb_provider.utils.helpers import get_querystring


def get_token():
    return requests.post(
        "http://0.0.0.0:8000/api/v1/account/token",
        data={"username": "openbb", "password": "openbb"},
        timeout=5,
    )


def auth_header():
    access_token = get_token().json()["access_token"]
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture(scope="session")
def headers():
    h = {}
    auth = auth_header()
    h.update(auth)
    return h


def get_random_data(menu: str, symbols: List[str], providers: List[str]):
    symbol = random.choice(symbols)  # noqa: S311
    provider = random.choice(providers)  # noqa: S311

    url = f"http://0.0.0.0:8000/api/v1/{menu}/load?symbol={symbol}&provider={provider}"
    result = requests.get(url, headers=auth_header(), timeout=5)
    return result.json()["results"]


symbols = ["AAPL", "NVDA", "MSFT", "TSLA", "AMZN", "GOOG", "FB", "BABA", "TSM", "V"]
providers = ["fmp", "intrinio", "polygon", "yfinance"]
stocks_data = get_random_data("stocks", symbols=symbols, providers=providers)

# TODO : add more crypto providers and symbols
symbols_crypto = ["BTC"]
providers_crypto = ["fmp"]
crypto_data = get_random_data(
    menu="crypto", symbols=symbols_crypto, providers=providers_crypto
)


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "length": "",
                "mamode": "",
                "drift": "",
                "offset": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "length": "15",
                "mamode": "rma",
                "drift": "2",
                "offset": "1",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_atr(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/atr?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "close_column": "",
                "period": "",
                "start_date": "",
                "end_date": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "close_column": "adj_close",
                "period": "125",
                "start_date": "",
                "end_date": "",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_fib(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/fib?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "offset": ""}),
        ({"data": crypto_data, "index": "date", "offset": "1"}),
    ],
)
@pytest.mark.integration
def test_ta_obv(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/obv?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "length": "", "signal": ""}),
        ({"data": crypto_data, "index": "date", "length": "15", "signal": "2"}),
    ],
)
@pytest.mark.integration
def test_ta_fisher(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/fisher?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "fast": "", "slow": "", "offset": ""}),
        (
            {
                "data": crypto_data,
                "index": "date",
                "fast": "5",
                "slow": "15",
                "offset": "2",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_adosc(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/adosc?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "target": "",
                "index": "",
                "length": "",
                "std": "",
                "mamode": "",
                "offset": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "length": "55",
                "std": "3",
                "mamode": "wma",
                "offset": "1",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_bbands(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/bbands?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "target": "", "index": "", "length": "", "offset": ""}),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "length": "55",
                "offset": "5",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_zlma(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/zlma?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "length": "", "scalar": ""}),
        (
            {
                "data": crypto_data,
                "index": "date",
                "length": "30",
                "scalar": "110",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_aroon(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/aroon?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "target": "", "index": "", "length": "", "offset": ""}),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "length": "55",
                "offset": "2",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_sma(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/sma?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "target": "",
                "show_all": "",
                "asint": "",
                "offset": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "target": "high",
                "show_all": "true",
                "asint": "true",
                "offset": "5",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_demark(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/demark?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "anchor": "", "offset": ""}),
        ({"data": crypto_data, "index": "date", "anchor": "W", "offset": "5"}),
    ],
)
@pytest.mark.integration
def test_ta_vwap(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/vwap?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "target": "",
                "index": "",
                "fast": "",
                "slow": "",
                "signal": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "fast": "10",
                "slow": "30",
                "signal": "10",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_macd(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/macd?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "target": "", "index": "", "length": "", "offset": ""}),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "length": "55",
                "offset": "2",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_hma(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/hma?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "lower_length": "",
                "upper_length": "",
                "offset": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "lower_length": "30",
                "upper_length": "40",
                "offset": "5",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_donchian(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/donchian?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "conversion": "",
                "base": "",
                "lagging": "",
                "offset": "",
                "lookahead": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "conversion": "10",
                "base": "30",
                "lagging": "50",
                "offset": "30",
                "lookahead": "true",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_ichimoku(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/ichimoku?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "target": "", "period": ""}),
        ({"data": crypto_data, "index": "date", "target": "close", "period": "95"}),
    ],
)
@pytest.mark.integration
def test_ta_clenow(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/clenow?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "offset": ""}),
        ({"data": crypto_data, "index": "date", "offset": "5"}),
    ],
)
@pytest.mark.integration
def test_ta_ad(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/ad?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "length": "", "scalar": "", "drift": ""}),
        (
            {
                "data": crypto_data,
                "index": "date",
                "length": "60",
                "scalar": "90.0",
                "drift": "2",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_adx(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/adx?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "target": "", "index": "", "length": "", "offset": ""}),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "length": "60",
                "offset": "10",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_wma(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/wma?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "length": "", "scalar": ""}),
        ({"data": crypto_data, "index": "date", "length": "16", "scalar": "0.02"}),
    ],
)
@pytest.mark.integration
def test_ta_cci(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/cci?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "target": "",
                "index": "",
                "length": "",
                "scalar": "",
                "drift": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "date",
                "length": "16",
                "scalar": "90.0",
                "drift": "2",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_rsi(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/rsi?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "fast_k_period": "",
                "slow_d_period": "",
                "slow_k_period": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "fast_k_period": "12",
                "slow_d_period": "2",
                "slow_k_period": "2",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_stoch(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/stoch?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "length": "",
                "scalar": "",
                "mamode": "",
                "offset": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "length": "22",
                "scalar": "24",
                "mamode": "sma",
                "offset": "5",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_kc(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/kc?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        ({"data": stocks_data, "index": "", "length": ""}),
        ({"data": crypto_data, "index": "date", "length": "20"}),
    ],
)
@pytest.mark.integration
def test_ta_cg(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/cg?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "index": "",
                "lower_q": "",
                "upper_q": "",
                "model": "",
                "is_crypto": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "index": "date",
                "lower_q": "0.3",
                "upper_q": "0.7",
                "model": "Parkinson",
                "is_crypto": "true",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_cones(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/cones?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200


@pytest.mark.parametrize(
    "params",
    [
        (
            {
                "data": stocks_data,
                "target": "close",
                "index": "date",
                "length": "",
                "offset": "",
            }
        ),
        (
            {
                "data": crypto_data,
                "target": "high",
                "index": "",
                "length": "60",
                "offset": "10",
            }
        ),
    ],
)
@pytest.mark.integration
def test_ta_ema(params, headers):
    params = {p: v for p, v in params.items() if v}
    data = json.dumps(params.pop("data"))

    query_str = get_querystring(params, [])
    url = f"http://0.0.0.0:8000/api/v1/ta/ema?{query_str}"
    result = requests.post(url, headers=headers, timeout=5, data=data)
    assert isinstance(result, requests.Response)
    assert result.status_code == 200
