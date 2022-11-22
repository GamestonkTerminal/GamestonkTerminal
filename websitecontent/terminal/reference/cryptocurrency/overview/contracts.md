---
title: contracts
description: OpenBB Terminal Function
---

# contracts

Gets all contract addresses for given platform. Provide platform id with -p/--platform parameter You can display only N number of smart contracts with --limit parameter. You can sort data by id, type, active, balance --sortby parameter and also with --reverse flag to sort descending. Displays: id, type, active, balance

### Usage

```python
usage: contracts
                 [-p {btc-bitcoin,eos-eos,eth-ethereum,xrp-xrp,bch-bitcoin-cash,xem-nem,neo-neo,xlm-stellar,etc-ethereum-classic,qtum-qtum,zec-zcash,vet-vechain,bts-bitshares,waves-waves,nxt-nxt,act-achain,ubq-ubiq,xcp-counterparty,ppc-peercoin,etp-metaverse-etp,signa-signa,omni-omni,trx-tron,bnb-binance-coin,ardr-ardor,ht-huobi-token,wan-wanchain,ftm-fantom,matic-polygon,afcash-africunia-bank,avax-avalanche,sol-solana,blvr-believer,cake-pancakeswap,bcna-bitcanna831,fsxu-flashx-ultra,chik-chickenkebab-finance,jgn-juggernaut7492,crx-cryptex,whirl-whirl-finance,etl-etherlite,eubi-eubi-token,swam-swapmatic-token,shells-shells,levelg-levelg,lyr-lyra,ants-fireants,berry-berry,drc-deracoin,sxcc-southxchange-coin,vega-vega-coin,xgk-goldkash,ptd-peseta-digital,mmt-moments-market,gems-algogems,kilt-kilt-protocol,harl-harmonylauncher,alph-alephium,ride-holoride,fcon-spacefalcon,love-diamond-love,kint-kintsugi,astr-astar,chum-chum-coin,polyx-polymesh,kfl-kaafila,evmos-evmos,wtip-worktips9618,xeta-xana,arn-arenum,fayre-fayre,mart-artmeta,azit-azit,fcd-freshcut-diamond,pbt-property-blockchain-trade,fww-farmers-world-wood,cand-canary-dollar,srs-sirius-finance,xden-xiden,arz-arize,hash-provenance-blockchain,joy-drawshop-kingdom-reverse-joystick,orbc-orbis,b3x-bnext-b3x,xmp-maptcoin,gomt-gomeat,pro-proton-coin,slrr-solarr,xgbl-xungible,utg-ultronglow,oxp-onxrp,algx-algodex,bridge-octus-bridge,cvshot-cvshots,xspectar-xspectar,blkz-blocksworkz,sva-solvia,bdlt-bdlt,ogy-origyn-foundation,digau-dignity-gold,trx3l-trx3l,eth3s-eth3s,intr-interlay,crom-crome,tutl-tutela,cc-cloudcoin,ztg-zeitgeist,film-filmcredits,znt-zenith-finance,bnd-bened,mddn-modden234234234,wei-wei,dcrn-decred-next,omc-omchain,turn-big-turn,cmp-caduceus,pmg-pmg-coin,xx-xx-network,neer-metaversenetwork-pioneer,tao-fusotao,cic-crazy-internet-coin,bsx-basilisk,cuc-cuprum-coin,ulx-ultron,fury-fanfury,vxxl-vxxl,spex-stepex,log-logos,metal-metal-blockchain,nai-natiol,ling-lingose}]
                 [-l LIMIT] [-s {id,type,active}] [-r]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| platform | Blockchain platform like eth-ethereum | eth-ethereum | True | btc-bitcoin, eos-eos, eth-ethereum, xrp-xrp, bch-bitcoin-cash, xem-nem, neo-neo, xlm-stellar, etc-ethereum-classic, qtum-qtum, zec-zcash, vet-vechain, bts-bitshares, waves-waves, nxt-nxt, act-achain, ubq-ubiq, xcp-counterparty, ppc-peercoin, etp-metaverse-etp, signa-signa, omni-omni, trx-tron, bnb-binance-coin, ardr-ardor, ht-huobi-token, wan-wanchain, ftm-fantom, matic-polygon, afcash-africunia-bank, avax-avalanche, sol-solana, blvr-believer, cake-pancakeswap, bcna-bitcanna831, fsxu-flashx-ultra, chik-chickenkebab-finance, jgn-juggernaut7492, crx-cryptex, whirl-whirl-finance, etl-etherlite, eubi-eubi-token, swam-swapmatic-token, shells-shells, levelg-levelg, lyr-lyra, ants-fireants, berry-berry, drc-deracoin, sxcc-southxchange-coin, vega-vega-coin, xgk-goldkash, ptd-peseta-digital, mmt-moments-market, gems-algogems, kilt-kilt-protocol, harl-harmonylauncher, alph-alephium, ride-holoride, fcon-spacefalcon, love-diamond-love, kint-kintsugi, astr-astar, chum-chum-coin, polyx-polymesh, kfl-kaafila, evmos-evmos, wtip-worktips9618, xeta-xana, arn-arenum, fayre-fayre, mart-artmeta, azit-azit, fcd-freshcut-diamond, pbt-property-blockchain-trade, fww-farmers-world-wood, cand-canary-dollar, srs-sirius-finance, xden-xiden, arz-arize, hash-provenance-blockchain, joy-drawshop-kingdom-reverse-joystick, orbc-orbis, b3x-bnext-b3x, xmp-maptcoin, gomt-gomeat, pro-proton-coin, slrr-solarr, xgbl-xungible, utg-ultronglow, oxp-onxrp, algx-algodex, bridge-octus-bridge, cvshot-cvshots, xspectar-xspectar, blkz-blocksworkz, sva-solvia, bdlt-bdlt, ogy-origyn-foundation, digau-dignity-gold, trx3l-trx3l, eth3s-eth3s, intr-interlay, crom-crome, tutl-tutela, cc-cloudcoin, ztg-zeitgeist, film-filmcredits, znt-zenith-finance, bnd-bened, mddn-modden234234234, wei-wei, dcrn-decred-next, omc-omchain, turn-big-turn, cmp-caduceus, pmg-pmg-coin, xx-xx-network, neer-metaversenetwork-pioneer, tao-fusotao, cic-crazy-internet-coin, bsx-basilisk, cuc-cuprum-coin, ulx-ultron, fury-fanfury, vxxl-vxxl, spex-stepex, log-logos, metal-metal-blockchain, nai-natiol, ling-lingose |
| limit | display N number records | 15 | True | None |
| sortby | Sort by given column | id | True | id, type, active |
| reverse | Data is sorted in ascending order by default. Reverse flag will sort it in an descending way. Only works when raw data is displayed. | False | True | None |
---

