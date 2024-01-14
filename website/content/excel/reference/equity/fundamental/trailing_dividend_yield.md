---
title: trailing_dividend_yield
description: Trailing 1yr dividend yield
keywords: 
- equity
- fundamental
- trailing_dividend_yield
---

<!-- markdownlint-disable MD041 -->

Trailing 1yr dividend yield.

## Syntax

```jsx<span style={color: 'red'}>=OBB.EQUITY.FUNDAMENTAL.TRAILING_DIVIDEND_YIELD([provider];[symbol])</span>```

### Example

```excel wordwrap
=OBB.EQUITY.FUNDAMENTAL.TRAILING_DIVIDEND_YIELD()
```

---

## Parameters

| Name | Type | Description | Optional |
| ---- | ---- | ----------- | -------- |
| provider | Text | Options: tiingo, defaults to tiingo. | True |
| symbol | Text | Symbol to get data for. | True |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| date | The date of the data.  |
| trailing_dividend_yield | Trailing dividend yield.  |
