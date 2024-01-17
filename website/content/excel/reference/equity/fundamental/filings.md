---
title: FILINGS
description: Learn how to retrieve company filings data such as date, type of document,
  and link. Understand the available parameters to filter the data, including symbol,
  limit, provider, type, and page. Explore the different fields in the data, such
  as ticker symbol, accepted date, and final link.
keywords: 
- company filings
- data entries
- symbol
- limit
- provider
- type
- page
- cik
- date
- link
- ticker symbol
- accepted date
- final link
- report date
- act
- items
- primary doc description
- primary doc
- accession number
- file number
- film number
- is inline xbrl
- is xbrl
- size
- complete submission url
- filing detail url
- xml
---

<!-- markdownlint-disable MD033 -->
import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="EQUITY.FUNDAMENTAL.FILINGS | OpenBB Add-in for Excel Docs" />

Company Filings. Company filings data.

## Syntax

```excel wordwrap
=OBB.EQUITY.FUNDAMENTAL.FILINGS([symbol];[provider];[form_type];[limit];[start_date];[end_date];[thea_enabled];[cik];[use_cache])
```

### Example

```excel wordwrap
=OBB.EQUITY.FUNDAMENTAL.FILINGS()
```

---

## Parameters

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| symbol | Text | Symbol to get data for. | False |
| provider | Text | Options: fmp, intrinio, sec, defaults to fmp. | False |
| form_type | Text | Type of the SEC filing form. (provider: sec) | False |
| limit | Number | The number of data entries to return. | False |
| start_date | Text | Start date of the data, in YYYY-MM-DD format. (provider: intrinio) | False |
| end_date | Text | End date of the data, in YYYY-MM-DD format. (provider: intrinio) | False |
| thea_enabled | Boolean | Return filings that have been read by Intrinio's Thea NLP. (provider: intrinio) | False |
| cik | Any | Lookup filings by Central Index Key (CIK) instead of by symbol. (provider: sec) | False |
| use_cache | Boolean | Whether or not to use cache.  If True, cache will store for one day. (provider: sec) | False |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| symbol | Symbol representing the entity requested in the data.  |
| cik | Central Index Key (CIK) for the requested entity.  |
| filing_date | Filing date of the SEC report.  |
| accepted_date | Accepted date of the SEC report.  |
| report_type | Type of the SEC report.  |
| filing_url | URL to the filing page on the SEC site.  |
| report_url | URL to the actual report on the SEC site.  |
| id | Intrinio ID of the filing. (provider: intrinio) |
| period_end_date | Ending date of the fiscal period for the filing. (provider: intrinio) |
| sec_unique_id | SEC unique ID of the filing. (provider: intrinio) |
| instance_url | URL for the XBRL filing for the report. (provider: intrinio) |
| industry_group | Industry group of the company. (provider: intrinio) |
| industry_category | Industry category of the company. (provider: intrinio) |
| report_date | The date of the filing. (provider: sec) |
| act | The SEC Act number. (provider: sec) |
| items | The SEC Item numbers. (provider: sec) |
| primary_doc_description | The description of the primary document. (provider: sec) |
| primary_doc | The filename of the primary document. (provider: sec) |
| accession_number | The accession number. (provider: sec) |
| file_number | The file number. (provider: sec) |
| film_number | The film number. (provider: sec) |
| is_inline_xbrl | Whether the filing is an inline XBRL filing. (provider: sec) |
| is_xbrl | Whether the filing is an XBRL filing. (provider: sec) |
| size | The size of the filing. (provider: sec) |
| complete_submission_url | The URL to the complete filing submission. (provider: sec) |
| filing_detail_url | The URL to the filing details. (provider: sec) |
