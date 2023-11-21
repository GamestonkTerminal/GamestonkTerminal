---
title: dapps
description: A comprehensive guide to understanding and using 'dapps' command for
  listing and sorting the top Decentralized Applications (DApps) from various categories
  and protocols as per users' choice.
keywords:
- DApp
- Decentralized Applications
- Crypto
- Blockchain
- PancakeSwap
- Splinterlands
- Alien Worlds
- Farmers World
- AtomicAssets
- Axie Infinity
- Upland
- OpenSea
- Katana
- Magic Eden
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="crypto /disc/dapps - Reference | OpenBB Terminal Docs" />

Shows available decentralized applications [Source: https://dappradar.com/] Accepts --chain argument to filter by blockchain --page argument to show a specific page. Default: 1 --limit argument to limit the number of records per page. Default: 15

### Usage

```python wordwrap
dapps [-c CHAIN] [-p PAGE] [-l LIMIT]
```

---

## Parameters

| Name | Parameter | Description | Default | Optional | Choices |
| ---- | --------- | ----------- | ------- | -------- | ------- |
| chain | -c  --chain | Filter by blockchain | None | True | None |
| page | -p  --page | Page number | 1 | True | None |
| limit | -l  --limit | Number of records to display per page | 15 | True | None |


---

## Examples

```python
2022 Feb 15, 06:52 (🦋) /crypto/disc/ $ dapps
                              Top Decentralized Applications
┌───────────────┬──────────────┬─────────────────────────┬─────────────┬──────────────────┐
│ Name          │ Category     │ Protocols               │ Daily Users │ Daily Volume [$] │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Splinterlands │ games        │ hive,wax                │ 305.1K      │ 8K               │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ PancakeSwap   │ defi         │ binance-smart-chain     │ 289.3K      │ 223.7M           │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Alien Worlds  │ games        │ wax,binance-smart-chain │ 235.6K      │ 759.2K           │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Farmers World │ games        │ wax                     │ 111.7K      │ 2.3K             │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ AtomicAssets  │ other        │ wax,eos                 │ 108.9K      │ 226.3K           │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Axie Infinity │ games        │ ronin,ethereum          │ 90.9K       │ 11.6M            │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Upland        │ games        │ eos                     │ 63.3K       │ 0                │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ OpenSea       │ marketplaces │ ethereum,polygon        │ 54K         │ 200M             │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Katana        │ defi         │ ronin                   │ 45.9K       │ 92.7M            │
├───────────────┼──────────────┼─────────────────────────┼─────────────┼──────────────────┤
│ Magic Eden    │ marketplaces │ solana                  │ 40.2K       │ 18.5M            │
└───────────────┴──────────────┴─────────────────────────┴─────────────┴──────────────────┘
```
---
