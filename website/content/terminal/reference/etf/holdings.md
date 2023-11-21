---
title: holdings
description: Look at ETF company holdings
keywords:
- etf
- holdings
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="etf /holdings - Reference | OpenBB Terminal Docs" />

Look at ETF company holdings

### Usage

```python wordwrap
holdings [-l LIMIT]
```

---

## Parameters

| Name | Parameter | Description | Default | Optional | Choices |
| ---- | --------- | ----------- | ------- | -------- | ------- |
| limit | -l  --limit | Number of holdings to get | 10 | True | None |


---

## Examples

```python
2022 Oct 27, 08:21 (🦋) /etf/ $ holdings

                           ETF Holdings                           
┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃       ┃ Name                            ┃ % Of Etf ┃ Shares    ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━┩
│ AAPL  │ Apple Inc.                      │ 7.06%    │ 169672324 │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ MSFT  │ Microsoft Corporation           │ 5.74%    │ 83765412  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ AMZN  │ Amazon.com, Inc.                │ 3.28%    │ 99548898  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ GOOGL │ Alphabet, Inc.                  │ 1.92%    │ 67345732  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ TSLA  │ Tesla, Inc.                     │ 1.82%    │ 29915424  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ GOOG  │ Alphabet, Inc.                  │ 1.73%    │ 60222505  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ BRK.B │ Berkshire Hathaway Inc.         │ 1.60%    │ 20277701  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ UNH   │ UnitedHealth Group Incorporated │ 1.55%    │ 10505922  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ JNJ   │ Johnson & Johnson               │ 1.38%    │ 29530061  │
├───────┼─────────────────────────────────┼──────────┼───────────┤
│ XOM   │ Exxon Mobil Corporation         │ 1.35%    │ 46810082  │
└───────┴─────────────────────────────────┴──────────┴───────────┘
```
---
