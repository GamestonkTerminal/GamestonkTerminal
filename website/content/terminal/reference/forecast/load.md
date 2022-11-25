---
title: load
description: OpenBB Terminal Function
---

# load

Load custom dataset (from previous export, custom imports).

### Usage

```python
load [-f {20221103_171440_stocks_quantitative_analysis_cdf.xlsx,20221103_171440_stocks_quantitative_analysis_summary.xlsx,20221103_171441_stocks_quantitative_analysis_normality.xlsx,20221103_171441_stocks_quantitative_analysis_summary.xlsx,20221103_171554_stocks_quantitative_analysis_cdf.xlsx,20221103_171554_stocks_quantitative_analysis_summary.xlsx,20221103_171555_stocks_quantitative_analysis_normality.xlsx,20221103_171555_stocks_quantitative_analysis_summary.xlsx,20221103_171741_stocks_quantitative_analysis_summary.xlsx,20221103_171742_stocks_quantitative_analysis_cdf.xlsx,20221103_171742_stocks_quantitative_analysis_normality.xlsx,20221103_171742_stocks_quantitative_analysis_summary.xlsx,20221103_171923_stocks_quantitative_analysis_cdf.xlsx,20221103_171923_stocks_quantitative_analysis_summary.xlsx,20221103_171924_stocks_quantitative_analysis_normality.xlsx,20221103_171924_stocks_quantitative_analysis_summary.xlsx,20221103_172442_stocks_quantitative_analysis_cdf.xlsx,20221103_172442_stocks_quantitative_analysis_summary.xlsx,20221103_172443_stocks_quantitative_analysis_normality.xlsx,20221103_172443_stocks_quantitative_analysis_summary.xlsx,20221103_172648_econometrics_dataset.xlsx,20221103_173150_stocks_quantitative_analysis_cdf.xlsx,20221103_173150_stocks_quantitative_analysis_summary.xlsx,20221103_173151_stocks_quantitative_analysis_normality.xlsx,20221103_173151_stocks_quantitative_analysis_summary.xlsx,20221103_173401_econometrics_dataset.xlsx,20221103_181013_stocks_quantitative_analysis_cdf.xlsx,20221103_181013_stocks_quantitative_analysis_summary.xlsx,20221103_181014_stocks_quantitative_analysis_normality.xlsx,20221103_181014_stocks_quantitative_analysis_summary.xlsx,20221103_181228_econometrics_dataset.xlsx,20221103_181529_stocks_quantitative_analysis_cdf.xlsx,20221103_181529_stocks_quantitative_analysis_normality.xlsx,20221103_181529_stocks_quantitative_analysis_summary.xlsx,20221103_181734_econometrics_dataset.xlsx,20221104_161018_stocks_quantitative_analysis_summary.xlsx,20221104_161019_stocks_quantitative_analysis_cdf.xlsx,20221104_161019_stocks_quantitative_analysis_normality.xlsx,20221104_161019_stocks_quantitative_analysis_summary.xlsx,20221104_161238_econometrics_dataset.xlsx,20221104_161752_stocks_quantitative_analysis_summary.xlsx,20221104_161753_stocks_quantitative_analysis_cdf.xlsx,20221104_161754_stocks_quantitative_analysis_normality.xlsx,20221104_161754_stocks_quantitative_analysis_summary.xlsx,20221104_162013_econometrics_dataset.xlsx,20221104_162505_stocks_quantitative_analysis_cdf.xlsx,20221104_162505_stocks_quantitative_analysis_summary.xlsx,20221104_162506_stocks_quantitative_analysis_normality.xlsx,20221104_162506_stocks_quantitative_analysis_summary.xlsx,20221104_162726_econometrics_dataset.xlsx,20221104_163317_stocks_quantitative_analysis_cdf.xlsx,20221104_163317_stocks_quantitative_analysis_summary.xlsx,20221104_163318_stocks_quantitative_analysis_normality.xlsx,20221104_163318_stocks_quantitative_analysis_summary.xlsx,20221104_163542_econometrics_dataset.xlsx,20221104_164405_stocks_quantitative_analysis_cdf.xlsx,20221104_164405_stocks_quantitative_analysis_summary.xlsx,20221104_164406_stocks_quantitative_analysis_normality.xlsx,20221104_164406_stocks_quantitative_analysis_summary.xlsx,20221104_164550_stocks_quantitative_analysis_cdf.xlsx,20221104_164550_stocks_quantitative_analysis_summary.xlsx,20221104_164551_stocks_quantitative_analysis_normality.xlsx,20221104_164551_stocks_quantitative_analysis_summary.xlsx,20221104_164700_stocks_quantitative_analysis_cdf.xlsx,20221104_164700_stocks_quantitative_analysis_summary.xlsx,20221104_164701_stocks_quantitative_analysis_normality.xlsx,20221104_164701_stocks_quantitative_analysis_summary.xlsx,20221104_164802_stocks_quantitative_analysis_cdf.xlsx,20221104_164802_stocks_quantitative_analysis_summary.xlsx,20221104_164803_stocks_quantitative_analysis_normality.xlsx,20221104_164803_stocks_quantitative_analysis_summary.xlsx,20221104_165019_econometrics_dataset.xlsx}] [-a ALIAS]
```

---

## Parameters

| Name | Description | Default | Optional | Choices |
| ---- | ----------- | ------- | -------- | ------- |
| file | File to load data in (can be custom import, may have been exported before.) | None | True | 20221103_171440_stocks_quantitative_analysis_cdf.xlsx, 20221103_171440_stocks_quantitative_analysis_summary.xlsx, 20221103_171441_stocks_quantitative_analysis_normality.xlsx, 20221103_171441_stocks_quantitative_analysis_summary.xlsx, 20221103_171554_stocks_quantitative_analysis_cdf.xlsx, 20221103_171554_stocks_quantitative_analysis_summary.xlsx, 20221103_171555_stocks_quantitative_analysis_normality.xlsx, 20221103_171555_stocks_quantitative_analysis_summary.xlsx, 20221103_171741_stocks_quantitative_analysis_summary.xlsx, 20221103_171742_stocks_quantitative_analysis_cdf.xlsx, 20221103_171742_stocks_quantitative_analysis_normality.xlsx, 20221103_171742_stocks_quantitative_analysis_summary.xlsx, 20221103_171923_stocks_quantitative_analysis_cdf.xlsx, 20221103_171923_stocks_quantitative_analysis_summary.xlsx, 20221103_171924_stocks_quantitative_analysis_normality.xlsx, 20221103_171924_stocks_quantitative_analysis_summary.xlsx, 20221103_172442_stocks_quantitative_analysis_cdf.xlsx, 20221103_172442_stocks_quantitative_analysis_summary.xlsx, 20221103_172443_stocks_quantitative_analysis_normality.xlsx, 20221103_172443_stocks_quantitative_analysis_summary.xlsx, 20221103_172648_econometrics_dataset.xlsx, 20221103_173150_stocks_quantitative_analysis_cdf.xlsx, 20221103_173150_stocks_quantitative_analysis_summary.xlsx, 20221103_173151_stocks_quantitative_analysis_normality.xlsx, 20221103_173151_stocks_quantitative_analysis_summary.xlsx, 20221103_173401_econometrics_dataset.xlsx, 20221103_181013_stocks_quantitative_analysis_cdf.xlsx, 20221103_181013_stocks_quantitative_analysis_summary.xlsx, 20221103_181014_stocks_quantitative_analysis_normality.xlsx, 20221103_181014_stocks_quantitative_analysis_summary.xlsx, 20221103_181228_econometrics_dataset.xlsx, 20221103_181529_stocks_quantitative_analysis_cdf.xlsx, 20221103_181529_stocks_quantitative_analysis_normality.xlsx, 20221103_181529_stocks_quantitative_analysis_summary.xlsx, 20221103_181734_econometrics_dataset.xlsx, 20221104_161018_stocks_quantitative_analysis_summary.xlsx, 20221104_161019_stocks_quantitative_analysis_cdf.xlsx, 20221104_161019_stocks_quantitative_analysis_normality.xlsx, 20221104_161019_stocks_quantitative_analysis_summary.xlsx, 20221104_161238_econometrics_dataset.xlsx, 20221104_161752_stocks_quantitative_analysis_summary.xlsx, 20221104_161753_stocks_quantitative_analysis_cdf.xlsx, 20221104_161754_stocks_quantitative_analysis_normality.xlsx, 20221104_161754_stocks_quantitative_analysis_summary.xlsx, 20221104_162013_econometrics_dataset.xlsx, 20221104_162505_stocks_quantitative_analysis_cdf.xlsx, 20221104_162505_stocks_quantitative_analysis_summary.xlsx, 20221104_162506_stocks_quantitative_analysis_normality.xlsx, 20221104_162506_stocks_quantitative_analysis_summary.xlsx, 20221104_162726_econometrics_dataset.xlsx, 20221104_163317_stocks_quantitative_analysis_cdf.xlsx, 20221104_163317_stocks_quantitative_analysis_summary.xlsx, 20221104_163318_stocks_quantitative_analysis_normality.xlsx, 20221104_163318_stocks_quantitative_analysis_summary.xlsx, 20221104_163542_econometrics_dataset.xlsx, 20221104_164405_stocks_quantitative_analysis_cdf.xlsx, 20221104_164405_stocks_quantitative_analysis_summary.xlsx, 20221104_164406_stocks_quantitative_analysis_normality.xlsx, 20221104_164406_stocks_quantitative_analysis_summary.xlsx, 20221104_164550_stocks_quantitative_analysis_cdf.xlsx, 20221104_164550_stocks_quantitative_analysis_summary.xlsx, 20221104_164551_stocks_quantitative_analysis_normality.xlsx, 20221104_164551_stocks_quantitative_analysis_summary.xlsx, 20221104_164700_stocks_quantitative_analysis_cdf.xlsx, 20221104_164700_stocks_quantitative_analysis_summary.xlsx, 20221104_164701_stocks_quantitative_analysis_normality.xlsx, 20221104_164701_stocks_quantitative_analysis_summary.xlsx, 20221104_164802_stocks_quantitative_analysis_cdf.xlsx, 20221104_164802_stocks_quantitative_analysis_summary.xlsx, 20221104_164803_stocks_quantitative_analysis_normality.xlsx, 20221104_164803_stocks_quantitative_analysis_summary.xlsx, 20221104_165019_econometrics_dataset.xlsx |
| alias | Alias name to give to the dataset | None | True | None |


---

## Examples

```python
(🦋) /forecast/ $ load aapl.csv

(🦋) /forecast/ $ show aapl
                  Dataset aapl | Showing 10 of 759 rows
┏━━━┳━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━┓
┃   ┃ date       ┃ open  ┃ high  ┃ low   ┃ close ┃ adj_close ┃ volume    ┃
┡━━━╇━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 0 │ 2019-06-10 │ 47.95 │ 48.84 │ 47.90 │ 48.15 │ 46.99     │ 104883600 │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 1 │ 2019-06-11 │ 48.72 │ 49.00 │ 48.40 │ 48.70 │ 47.53     │ 107731600 │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 2 │ 2019-06-12 │ 48.49 │ 48.99 │ 48.35 │ 48.55 │ 47.38     │ 73012800  │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 3 │ 2019-06-13 │ 48.67 │ 49.20 │ 48.40 │ 48.54 │ 47.37     │ 86698400  │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 4 │ 2019-06-14 │ 47.89 │ 48.40 │ 47.58 │ 48.19 │ 47.03     │ 75046000  │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 5 │ 2019-06-17 │ 48.22 │ 48.74 │ 48.04 │ 48.47 │ 47.31     │ 58676400  │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 6 │ 2019-06-18 │ 49.01 │ 50.07 │ 48.80 │ 49.61 │ 48.42     │ 106204000 │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 7 │ 2019-06-19 │ 49.92 │ 49.97 │ 49.33 │ 49.47 │ 48.28     │ 84496800  │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 8 │ 2019-06-20 │ 50.09 │ 50.15 │ 49.51 │ 49.87 │ 48.67     │ 86056000  │
├───┼────────────┼───────┼───────┼───────┼───────┼───────────┼───────────┤
│ 9 │ 2019-06-21 │ 49.70 │ 50.21 │ 49.54 │ 49.69 │ 48.50     │ 191202400 │
└───┴────────────┴───────┴───────┴───────┴───────┴───────────┴───────────┘
```
---
