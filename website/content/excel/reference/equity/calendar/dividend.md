---
title: dividend
description: Get upcoming and historical dividend data with the OBB.equity.calendar.dividend
  method. This method allows you to retrieve dividend information such as dates, amounts,
  and provider details. It also provides warnings, charts, and metadata for further
  analysis.
keywords: 
- dividend calendar
- upcoming dividends
- historical dividends
- dividend data
- dividend schedule
- dividend information
- dividend dates
- dividend amounts
- dividend provider
- dividend warnings
- dividend chart
- dividend metadata
- ex-dividend date
- record date
- payment date
- declaration date
- dividend symbol
- dividend name
- dividend adjusted amount
- dividend label
- annualized dividend amount
---

<!-- markdownlint-disable MD041 -->

Upcoming and Historical Dividend Calendar.

## Syntax

```jsx<span style={color: 'red'}>=OBB.EQUITY.CALENDAR.DIVIDEND([provider];[start_date];[end_date])</span>```

### Example

```excel wordwrap
=OBB.EQUITY.CALENDAR.DIVIDEND()
```

---

## Parameters

| Name | Type | Description | Optional |
| ---- | ---- | ----------- | -------- |
| provider | Text | Options: fmp, defaults to fmp. | True |
| start_date | Text | Start date of the data, in YYYY-MM-DD format. | True |
| end_date | Text | End date of the data, in YYYY-MM-DD format. | True |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| date | The date of the data. (Ex-Dividend)  |
| symbol | Symbol representing the entity requested in the data.  |
| amount | Dividend amount, per-share.  |
| name | Name of the entity.  |
| record_date | The record date of ownership for eligibility.  |
| payment_date | The payment date of the dividend.  |
| declaration_date | Declaration date of the dividend.  |
| adjusted_amount | The adjusted-dividend amount. (provider: fmp) |
| label | Ex-dividend date formatted for display. (provider: fmp) |
| factor | factor by which to multiply stock prices before this date, in order to calculate historically-adjusted stock prices. (provider: intrinio) |
| dividend_currency | The currency of the dividend. (provider: intrinio) |
| split_ratio | The ratio of the stock split, if a stock split occurred. (provider: intrinio) |
| annualized_amount | The indicated annualized dividend amount. (provider: nasdaq) |
