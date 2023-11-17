---
title: Basic Syntax
sidebar_position: 2
description: This page provides comprehensive information about standardized command
  syntax for an open-source platform. Topics discussed include the structure of command
  syntax, use of standardized parameters, usage of provider and symbol parameters,
  handling of date and limit parameters, and more. Also explored, are the methods
  for selecting data sources, handling different list and ticker symbol formats, and
  dealing with command responses and warnings.
keywords:
- command syntax
- standardized parameters
- date format
- provider parameter
- data source selection
- symbol parameter
- list formats
- ticker symbols
- date parameter
- time series
- limit parameter
- keyword arguments
- endpoint parameters
- command response
- data models
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="Basic Syntax - Usage | OpenBB Platform Docs" />

The structure of command syntax is standardized across common fields.  This ensures that a `date` is always a `date` and the format remains consistent throughout.  Standardized parameters include, but are not limited to:

- [provider](#provider)
- [symbol](#symbol)
- [start_date](#dates)
- [end_date](#dates)
- [date](#dates)
- [limit](#limit)

When looking at a function's docstring, the standard parameters (shared across multiple providers) are positioned first.  Provider-specific parameters positionally follow the `provider` argument.  The example below is from, `obb.equity.price.quote`:

```console
Parameters
----------
symbol : str
    Symbol to get data for. In this case, the comma separated list of symbols.
provider : Optional[Literal['fmp', 'intrinio']]
    The provider to use for the query, by default None.
    If None, the provider specified in defaults is selected or 'fmp' if there is
    no default.
source : Literal['iex', 'bats', 'bats_delayed', 'utp_delayed', 'cta_a_delayed', 'cta_b_delayed', 'intrinio_mx', 'intrinio_mx_plus', 'delayed_sip']
    Source of the data. (provider: intrinio)
```

:::note
Examples below assume that the Python interface has been imported in the current session, and/or the Fast API has been started.

```python
from openbb import obb
```

```python
uvicorn openbb_core.api.rest_api:app
```

:::

## Provider

The `provider` parameter is the way to select the specific source of the data from the endpoint.  If a [preference for the default provider](/platform/usage#user-settings) has not been defined, the default will be the first, alphabetically, installed provider. Provider values are entered in lower-case, with an underscore for multiple words - for example:

```python
historical_prices = obb.equity.price.historical("aapl", provider="alpha_vantage")
```

Provider coverage can be ascertained with the command below:

```python
obb.coverage.providers
```

Refer to, [Data Providers](/platform/extensions/data_extensions), for instructions on installing data provider extensions.

## Symbol

Symbols are not case-sensitive, and where the function allows, can be entered as a `string`, `List[str]`, or a comma-separated `string`.  The exact format of the symbol may vary between providers - for example, share classes, exchange suffixes, and global composities.  An example of this difference is shown below:

```python
obb.equity.price.historical("brk.b", provider="polygon")
```

```python
obb.equity.price.historical("brk-b", provider="fmp")
```

While some providers handle the different formats on their end, others do not.  This is something to consider when no results are returned from one source.

With providers supporting market data from multiple jurisdictions, the most common method for requesting data outside of US-listings is to append a suffix to the ticker symbol (e.g., `RELIANCE.NS`).  Formats may be unique to a provider, so it is best to review the source's documentation for an overview of their specific conventions.  [This page](https://help.yahoo.com/kb/SLN2310.html) on Yahoo describes how they format symbols, which many others follow to some degree.

### One Symbol

```python
quote = obb.equity.price.quote(symbol="td", provider="fmp")
```

### Multiple Symbols

The OpenBB Provider module enforces REST-compliant lists that can be entered in either format through the Python interface.

#### Comma-Separated String

This is the format required by the Fast API, when creating new data endpoints, it is important that the Python interface is able to accept both formats.

```python
quotes = obb.equity.price.quote("td,schw,jpm,ms", provider="fmp")
```

```python
import requests
r = requests.get("http://127.0.0.1:8000/api/v1/equity/price/quote?provider=fmp&symbol=td,schw,ms,jpm")
r.json()
```

#### Python List

Entering a list will provide the same outcome as above.

```python
quotes = obb.equity.price.quote(["td","schw","jpm","ms"], provider="fmp")
```

Lists of symbols can be generated from the results of other functions, and then passed to the input.

```python
symbol="spgi"
symbols = obb.equity.compare.peers(symbol).results.peers_list+[symbol]
quotes = obb.equity.price.quote(symbols)
```

:::note
To accomplish this same task through the Fast API, convert the list to a comma-separated string.
:::

```python
import requests
symbol="spgi"
r = requests.get(f"http://127.0.0.1:8000/api/v1/equity/compare/peers?provider=fmp&symbol={symbol}")
symbols_list = r.json()["results"]["peers_list"]+[symbol]
symbols = ",".join(symbols_list)
response = requests.get(f"http://127.0.0.1:8000/api/v1/equity/price/quote?provider=fmp&symbol={symbols}")
response.json()
```

## Dates

Dates are entered everywhere as a string, formatted as, "YYYY-MM-DD".  If the function has only the `date` parameter, the data will be a snapshot instead of a time series.

```python
historical_prices = obb.equity.price.historical(symbol="qqq", start_date="2023-01-10", end_date="2023-01-31", provider="fmp")
```

For flexibility and programmatic purposes, a `datetime` object is also accepted.

```python
from datetime import datetime
symbol="qqq"
start = datetime.strptime("100123", "%d%m%y")
end = datetime.strptime("2023-01-31","%Y-%m-%d")
historical_prices = obb.equity.price.historical(symbol, start_date=start, end_date=end, provider="fmp")
```

```python
import requests
response = requests.get(f"http://127.0.0.1:8000/api/v1/equity/price/historical?provider=fmp&symbol={symbol}&start_date={start}&end_date={end}")
response.json()
```

## Limit

Where, optional, `limit` parameters are supplied, they are likely to have sensible default states that return N results starting from the most recent entry or the `start_date`.  Enter these values as an integer.

```python
income = obb.equity.fa.income("AAPL", period="quarter", provider="fmp", limit=4)
```

## **kwargs

All endpoints accept additional keyword arguments, but non-existent parameters will be ignored.  Invalid parameters are communicated via the `warnings` field in the command response.  Parameters can be stored as a dictionary and fed to the command as `**kwargs`.  If a provider, or function, has an undocumented parameter it can still be accessed by supplying the additional kwargs.

```python
kwargs = {"symbol":"msft","start_date":"2023-01-01","provider":"polygon"}
historical_prices = obb.equity.price.historical(**kwargs)
```

```python
data = obb.equity.price.quote("brk-b", provider="fmp", source="bats")
data.warnings
```

```console
[Warning_(category='OpenBBWarning', message="Parameter 'source' is not supported by fmp. Available for: intrinio.")]
```

## REST API POST Requests

Most endpoints are for data retrieval, but some [toolkit extensions](/platform/extensions/toolkit_extensions) require data to pass through the function.  In these instances, it must be a POST request, and JSON.

### Example

This example will use a GET request to fetch daily VIX data from the Cboe data extension, and then make a POST request which passes through the data to a technical analysis function.

First, start a development server.

```bash
uvicorn openbb_core.api.rest_api:app --reload
```

This example will use Python and the Requests library, so the syntax will vary according to the preferred medium for interacting with the API.

#### Fetch Some Data

```python
import requests

get_url = "http://127.0.0.1:8000/api/v1/index/market?provider=cboe&symbol=vix&interval=1d"
get_response = requests.get(get_url)
data_results = get_response.json()["results"]

data_results[-1]
```

```json
{'date': '2023-11-17T00:00:00',
 'open': 14.18,
 'high': 14.19,
 'low': 13.67,
 'close': 13.79,
 'volume': 0,
 'calls_volume': None,
 'puts_volume': None,
 'total_options_volume': None}
```

#### Send a POST Request

Next, pass the `data_results` to a function, using the `json` field in the POST headers.  For this example, Keltner Channels.

The `index` parameter tells the function which field in the posted data to use as the index.

```python
post_url = "http://localhost:8000/api/v1/technical/kc?index=date&length=20&scalar=20&mamode=ema&offset=0"
post_response = requests.post(post_url, json=data_results)
ta_results = post_response.json()["results"]

ta_results[-1]
```

```json
{'high': 14.19,
 'low': 13.67,
 'close': 13.79,
 'KCLe_20_20.0': -8.6829001886,
 'KCBe_20_20.0': 15.778316008,
 'KCUe_20_20.0': 40.2395322047}
```

#### Combine the Results

```python
for i, dictionary in enumerate(ta_results):
    dictionary["date"] = data_results[i]["date"]

ta_results[-1]
```

```json
{'high': 14.19,
 'low': 13.67,
 'close': 13.8,
 'KCLe_20_20.0': -8.6819478077,
 'KCBe_20_20.0': 15.779268389,
 'KCUe_20_20.0': 40.2404845856,
 'date': '2023-11-17T00:00:00'}
```

To confirm, validate that the data was correctly copied:

```python
(
    ta_results[-1]["close"] == data_results[-1]["close"]
    and ta_results[-1]["date"] == data_results[-1]["date"]
    and len(data_results) == len(ta_results)
)
```

```console
True
```

## References

All functions, parameters, and responses are detailed under the [Reference pages](/platform/reference).  The data models for each provider source are described within the [Data Models](/platform/data_models) pages.

These pages are a quick way to cross-reference differences between providers.  The same information is provided in a function's signature and docstring.
