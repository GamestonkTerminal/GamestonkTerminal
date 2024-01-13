---
title: dividends
description: Get historical dividends data for a given company with the OBB.equity.fundamental.dividends
  function. Explore parameters like symbol and provider, and understand the returned
  results, warnings, and metadata. View the data fields, including date, label, adj_dividend,
  dividend, record_date, payment_date, and declaration_date.
keywords: 
- historical dividends
- dividends data
- company dividends
- symbol
- data provider
- default provider
- results
- warnings
- chart
- metadata
- date
- label
- adj_dividend
- dividend
- record_date
- payment_date
- declaration_date
---

<!-- markdownlint-disable MD041 -->

Historical Dividends. Historical dividends data for a given company.

## Syntax

```jsx<span style={color: 'red'}>=OBB.EQUITY.FUNDAMENTAL.DIVIDENDS(symbol;[provider];[page_size])</span>```

### Example

```excel wordwrap
=OBB.EQUITY.FUNDAMENTAL.DIVIDENDS("AAPL")
```

---

## Parameters

| Name | Type | Description | Optional |
| ---- | ---- | ----------- | -------- |
| **symbol** | **Text** | **Symbol to get data for.** | **False** |
| provider | Text | Options: fmp, intrinio, defaults to fmp. | True |
| page_size | Number | The number of data entries to return. (provider: intrinio) | True |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| date | The date of the data.  |
| label | Label of the historical dividends.  |
| adj_dividend | Adjusted dividend of the historical dividends.  |
| dividend | Dividend of the historical dividends.  |
| record_date | Record date of the historical dividends.  |
| payment_date | Payment date of the historical dividends.  |
| declaration_date | Declaration date of the historical dividends.  |
