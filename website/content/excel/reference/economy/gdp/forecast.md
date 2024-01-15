---
title: forecast
description: Forecasted GDP Data
keywords: 
- economy
- gdp
- forecast
---

<!-- markdownlint-disable MD041 -->

Forecasted GDP Data.

## Syntax

```jsx<span style={color: 'red'}>=OBB.ECONOMY.GDP.FORECAST([provider];[period];[start_date];[end_date];[type];[country])</span>```

### Example

```excel wordwrap
=OBB.ECONOMY.GDP.FORECAST()
```

---

## Parameters

| Name | Type | Description | Optional |
| ---- | ---- | ----------- | -------- |
| provider | Text | Options: oecd, defaults to oecd. | True |
| period | Text | Time period of the data to return. Units for nominal GDP period. Either quarter or annual. | True |
| start_date | Text | Start date of the data, in YYYY-MM-DD format. | True |
| end_date | Text | End date of the data, in YYYY-MM-DD format. | True |
| type | Text | Type of GDP to get forecast of. Either nominal or real. | True |
| country | Text | Country to get GDP for. (provider: oecd) | True |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| date | The date of the data.  |
| value | Nominal GDP value on the date.  |
