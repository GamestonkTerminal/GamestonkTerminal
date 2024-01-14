---
title: symbol_map
description: Retrieve the ticker symbol corresponding to a company CIK using the
  OBB API endpoint. This function allows you to perform a search query and get the
  results along with additional metadata, warnings, and optional chart data.
keywords: 
- ticker symbol
- CIK
- company
- ticker mapping
- search query
- provider
- results
- warnings
- chart
- metadata
- data
- symbol
- entity
---

<!-- markdownlint-disable MD041 -->

Get the ticker symbol corresponding to a company's CIK.

## Syntax

```jsx<span style={color: 'red'}>=OBB.REGULATORS.SEC.SYMBOL_MAP([provider];[query])</span>```

### Example

```excel wordwrap
=OBB.REGULATORS.SEC.SYMBOL_MAP()
```

---

## Parameters

| Name | Type | Description | Optional |
| ---- | ---- | ----------- | -------- |
| provider | Text | Options: sec, defaults to sec. | True |
| query | Text | Search query. | True |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| symbol | Symbol representing the entity requested in the data. (provider: sec) |
