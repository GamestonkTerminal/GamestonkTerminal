---
title: ch
description: This documentation outlines the usage of the 'ch' command to display
  a list of major crypto-related hacks. It details the different parameters available
  to sort and display the data. Included are specific examples, and the expected output.
keywords:
- crypto-related hacks
- crypto hack
- hack display
- sort by parameters
- crypto platform
- hack amount
- hack date
- hack audit
- hack slug
- hack URL
- reverse display order
- individual crypto hack
---

import HeadTitle from '@site/src/components/General/HeadTitle.tsx';

<HeadTitle title="crypto /ov/ch - Reference | OpenBB Terminal Docs" />

Display list of major crypto-related hacks [Source: https://rekt.news] Can be sorted by {Platform,Date,Amount [$],Audit,Slug,URL} with --sortby and reverse the display order with --reverse Show only N elements with --limit Accepts --slug or -s to check individual crypto hack (e.g., -s polynetwork-rekt)

### Usage

```python wordwrap
ch [-l LIMIT] [--sortby {Platform,Date,Amount [$],Audit,Slug,URL} [{Platform,Date,Amount [$],Audit,Slug,URL} ...]] [-r] [-s SORTBY]
```

---

## Parameters

| Name | Parameter | Description | Default | Optional | Choices |
| ---- | --------- | ----------- | ------- | -------- | ------- |
| limit | -l  --limit | Display N items | 15 | True | None |
| sortby | --sortby | Sort by given column. Default: Amount [$] | Amount [$] | True | Platform, Date, Amount [$], Audit, Slug, URL |
| reverse | -r  --reverse | Data is sorted in descending order by default. Reverse flag will sort it in an ascending way. Only works when raw data is displayed. | False | True | None |
| slug | -s  --slug | Slug to check crypto hack (e.g., polynetwork-rekt) |  | True | ronin-rekt, polynetwork-rekt, bnb-bridge-rekt, sbf-mask-off, wormhole-rekt, mixin-rekt, euler-rekt, bitmart-rekt, nomad-rekt, beanstalk-rekt, wintermute-rekt-2, compound-rekt, vulcan-forged-rekt, cream-rekt-2, multichain-rekt2, poloniex-rekt, bonq-rekt, badger-rekt, mango-markets-rekt, atomic-wallet-rekt, harmony-rekt, mirror-rekt, fei-rari-rekt, qubit-rekt, ascendex-rekt, curve-vyper-rekt, alphapo-rekt, easyfi-rekt, uranium-rekt, bzx-rekt, coinex-rekt, cashio-rekt, pancakebunny-rekt, epic-hack-homie, stake-rekt, alpha-finance-rekt, lastpass-users-rekt, veefinance-rekt, cryptocom-rekt, meerkat-finance-bsc-rekt, monox-rekt, spartan-rekt, grim-finance-rekt, deribit-rekt, wintermute-rekt, stablemagnet-rekt, paid-rekt, harvest-finance-rekt, ankr-helio-rekt, xtoken-rekt, bald-rekt, elephant-money-rekt, venus-blizz-rekt, transit-swap-rekt, popsicle-rekt, pickle-finance-rekt, cream-rekt, snowdog-rekt, bearn-rekt, indexed-finance-rekt, teamfinance-rekt, inverse-finance-rekt, eminence-rekt-in-prod, furucombo-rekt, deus-dao-rekt-2, deathbed-confessions-c3pr, agave-hundred-rekt, yearn2-rekt, saddle-finance-rekt2, value-rekt3, yearn-rekt, dego-finance-rekt, arbix-rekt, rari-capital-rekt, value-rekt2, cover-rekt, dydx-rekt, punkprotocol-rekt, safemoon-rekt, crema-finance-rekt, superfluid-rekt, platypus-finance-rekt, moola-markets-rekt, visor-finance-rekt, thorchain-rekt2, hack-epidemic, lcx-rekt, htx-huobi-rekt, anyswap-rekt, warp-finance-rekt, meter-rekt, nightmare-ftm, jimbo-rekt, hundred-rekt2, exactly-protocol-rekt, burgerswap-rekt, value-defi-rekt, deus-dao-r3kt, lodestar-rekt, alchemix-rekt, belt-rekt, audius-rekt, bondly-rekt, inverse-rekt2, roll-rekt, unsolved-mystery, thorchain-rekt, xtoken-rekt-x2, 11-rekt, poly-network-rekt2, raydium-rekt, chainswap-rekt, conic-finance-rekt, kokomo-finance-rekt, voltage-finance-rekt, daomaker-rekt, dforce-network-rekt, nirvana-rekt, eralend-rekt, raft-rekt, sushi-yoink-rekt, skyward-rekt, jaypegs-automart-rekt, swaprum-rekt, orion-protocol-rekt, fortress-rekt, deus-dao-rekt, stars-arena-rekt, LSC-FSL-rekt, remitano-rekt, shibarium-bridge-rekt, atlantis-loans-rekt, pancakebunny2-rekt, templedao-rekt, platypus-rekt2, onyx-protocol-rekt, balancer-rekt, zunami-protocol-rekt, kannagi-finance-rekt, gymnet-rekt, revest-finance-rekt, ripmevbot2, dexible-rekt, madmeerkat-finance-rekt, au-dodo-rekt, akropolis-rekt, hope-finance-rekt, merlin-dex-rekt, bent-finance, 8ight-finance-rekt, defilabs-rekt, acala-network-rekt, ripmevbot, levyathan-rekt, treasure-dao-rekt, the-big-combo, steadefi-rekt, sovryn-rekt, level-finance-rekt, rocketswap-rekt, sturdy-rekt, tornado-gov-rekt, autoshark-rekt, merlinlabs-rekt, midas-capital-rekt, unibot-rekt, midas-rekt2, curve-finance-rekt, merlin2-rekt, hedera-rekt, merlin3-rekt, saddle-finance-rekt, safedollar-rekt |


---

## Examples

```python
2022 Feb 15, 08:16 (🦋) /crypto/ov/ $ ch
                                                            Major Crypto Hacks
┌────────────────────────┬────────────┬────────────┬────────────────────────┬────────────────────┬───────────────────────────────────────┐
│ Platform               │ Date       │ Amount [$] │ Audit                  │ Slug               │ URL                                   │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Poly Network - REKT    │ 2021-08-10 │ 611 M      │ Unaudited              │ polynetwork-rekt   │ https://rekt.news/polynetwork-rekt/   │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Wormhole - REKT        │ 2022-02-02 │ 326 M      │ Neodyme                │ wormhole-rekt      │ https://rekt.news/wormhole-rekt/      │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ BitMart - REKT         │ 2021-12-04 │ 196 M      │ N/A                    │ bitmart-rekt       │ https://rekt.news/bitmart-rekt/       │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Compound - REKT        │ 2021-09-29 │ 147 M      │ Unaudited              │ compound-rekt      │ https://rekt.news/compound-rekt/      │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Vulcan Forged - REKT   │ 2021-12-13 │ 140 M      │ Unaudited              │ vulcan-forged-rekt │ https://rekt.news/vulcan-forged-rekt/ │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Cream Finance - REKT 2 │ 2021-10-27 │ 130 M      │ Unaudited              │ cream-rekt-2       │ https://rekt.news/cream-rekt-2/       │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Badger - REKT          │ 2021-12-02 │ 120 M      │ Unaudited              │ badger-rekt        │ https://rekt.news/badger-rekt/        │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Qubit Finance - REKT   │ 2022-01-28 │ 80 M       │ Unaudited              │ qubit-rekt         │ https://rekt.news/qubit-rekt/         │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Ascendex - REKT        │ 2021-12-12 │ 77.700 M   │ Unaudited              │ ascendex-rekt      │ https://rekt.news/ascendex-rekt/      │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ EasyFi - REKT          │ 2021-04-19 │ 59 M       │ Unaudited              │ easyfi-rekt        │ https://rekt.news/easyfi-rekt/        │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Uranium Finance - REKT │ 2021-04-28 │ 57.200 M   │ Unaudited              │ uranium-rekt       │ https://rekt.news/uranium-rekt/       │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ bZx - REKT             │ 2021-11-05 │ 55 M       │ Unaudited              │ bzx-rekt           │ https://rekt.news/bzx-rekt/           │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ PancakeBunny - REKT    │ 2021-05-19 │ 45 M       │ Unaudited              │ pancakebunny-rekt  │ https://rekt.news/pancakebunny-rekt/  │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Kucoin - REKT          │ 2020-09-29 │ 45 M       │ Internal audit         │ epic-hack-homie    │ https://rekt.news/epic-hack-homie/    │
├────────────────────────┼────────────┼────────────┼────────────────────────┼────────────────────┼───────────────────────────────────────┤
│ Alpha Finance - REKT   │ 2021-02-13 │ 37.500 M   │ Quantstamp, Peckshield │ alpha-finance-rekt │ https://rekt.news/alpha-finance-rekt/ │
└────────────────────────┴────────────┴────────────┴────────────────────────┴────────────────────┴───────────────────────────────────────┘
```
---
