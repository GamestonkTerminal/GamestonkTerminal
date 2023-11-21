---
title: add
description: This page guides on the usage of the 'add' command to add options to
  the trading diagram. The command has parameters allowing the user to buy a put instead
  of a call, short an option, and specify an option's identifier.
keywords:
- trade options
- options trading
- options diagram
- add command
- buy put
- short option
- option identifier
- options command
- options parameters
- command usage
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="stocks /options/hedge/add - Reference | OpenBB Terminal Docs" />

Add options to the diagram.

### Usage

```python wordwrap
add [-p] [-s] -i {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47}
```

---

## Parameters

| Name | Parameter | Description | Default | Optional | Choices |
| ---- | --------- | ----------- | ------- | -------- | ------- |
| put | -p  --put | Buy a put instead of a call | False | True | None |
| short | -s  --short | Short the option instead of buying it | False | True | None |
| identifier | -i  --identifier | The identifier of the option as found in the list command | None | False | range(0, 48) |


---

## Examples

```python
2022 May 10, 09:17 (🦋) /stocks/options/hedge/ $ add 25
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃                    ┃ Positions ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Delta              │ 1.00      │
├────────────────────┼───────────┤
│ Gamma              │ 7253.89   │
├────────────────────┼───────────┤
│ Vega               │ 0.14      │
├────────────────────┼───────────┤
│ Implied Volatility │ 1.00e-05  │
├────────────────────┼───────────┤
│ Strike Price       │ 147.00    │
└────────────────────┴───────────┘

          Current Option Positions           
┏━━━━━━┳━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┓
┃ Type ┃ Hold ┃ Strike ┃ Implied Volatility ┃
┡━━━━━━╇━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━┩
│ Call │ Long │ 147.00 │ 1.00e-05           │
└──────┴──────┴────────┴────────────────────┘
```
---
