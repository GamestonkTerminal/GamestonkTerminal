---
title: filings
description: Get the most-recent filings submitted to the SEC
keywords: 
- equity
- discovery
- filings
---

<!-- markdownlint-disable MD041 -->

Get the most-recent filings submitted to the SEC.

## Syntax

```jsx<span style={color: 'red'}>=OBB.EQUITY.DISCOVERY.FILINGS([provider];[start_date];[end_date];[form_type];[limit];[isDone])</span>```

### Example

```excel wordwrap
=OBB.EQUITY.DISCOVERY.FILINGS()
```

---

## Parameters

| Name | Type | Description | Optional |
| ---- | ---- | ----------- | -------- |
| provider | Text | Options: fmp, defaults to fmp. | True |
| start_date | Text | Start date of the data, in YYYY-MM-DD format. | True |
| end_date | Text | End date of the data, in YYYY-MM-DD format. | True |
| form_type | Text | Filter by form type. Visit https://www.sec.gov/forms for a list of supported form types. | True |
| limit | Number | The number of data entries to return. | True |
| isDone | Boolean | Flag for whether or not the filing is done. (provider: fmp) | True |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| symbol | Symbol representing the entity requested in the data.  |
| cik | Central Index Key (CIK) for the requested entity.  |
| title | Title of the filing.  |
| date | The date of the data.  |
| form_type | The form type of the filing  |
| link | URL to the filing page on the SEC site.  |
