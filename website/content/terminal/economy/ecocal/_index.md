```
usage: ecocal [-c COUNTRY [COUNTRY ...]] [-i {high,medium,low,all}]
              [-cat {Employment,Credit,Balance,Economic Activity,Central Banks,Bonds,Inflation,Confidence Index} [{Employment,Credit,Balance,Economic Activity,Central Banks,Bonds,Inflation,Confidence Index} ...]]
              [-s START_DATE] [-e END_DATE] [-h] [--export EXPORT] [--raw]
```
Economic calendar.

```
optional arguments:
  -c COUNTRY [COUNTRY ...], --country COUNTRY [COUNTRY ...]
                        Display calendar for specific country. (default: united states)
  -i {high,medium,low,all}, --importances {high,medium,low,all}
                        Event importance classified as high, medium or low. (default: high)
  -cat {Employment,Credit,Balance,Economic Activity,Central Banks,Bonds,Inflation,Confidence Index} [{Employment,Credit,Balance,Economic Activity,Central Banks,Bonds,Inflation,Confidence Index} ...], --categories {Employment,Credit,Balance,Economic Activity,Central Banks,Bonds,Inflation,Confidence Index} [{Employment,Credit,Balance,Economic Activity,Central Banks,Bonds,Inflation,Confidence Index} ...]
                        Event category. (default: None)
  -s START_DATE, --start_date START_DATE
                        The start date of the data (format: YEAR-MONTH-DAY, i.e. 2010-12-31) (default: None)
  -e END_DATE, --end_date END_DATE
                        The start date of the data (format: YEAR-MONTH-DAY, i.e. 2010-12-31) (default: None)
  -h, --help            show this help message (default: False)
  --export EXPORT       Export raw data into csv, json, xlsx (default: )
  --raw                 Flag to display raw data (default: False)
```

Example:
```
2022 Jul 11, 00:12 (🦋) /economy/ $ ecocal

                                                     Calendar (GMT +1:00)
┏━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┓
┃ date       ┃ time  ┃ zone          ┃ currency ┃ importance ┃ event                          ┃ actual ┃ forecast ┃ previous ┃
┡━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━┩
│ 12/07/2022 │ 18:00 │ united states │ USD      │ high       │ EIA Short-Term Energy Outlook  │        │          │          │
├────────────┼───────┼───────────────┼──────────┼────────────┼────────────────────────────────┼────────┼──────────┼──────────┤
│ 13/07/2022 │ 14:30 │ united states │ USD      │ high       │ Core CPI (MoM)  (Jun)          │        │ 0.6%     │ 0.6%     │
├────────────┼───────┼───────────────┼──────────┼────────────┼────────────────────────────────┼────────┼──────────┼──────────┤
│ 13/07/2022 │ 16:30 │ united states │ USD      │ high       │ Crude Oil Inventories          │        │          │ 8.235M   │
├────────────┼───────┼───────────────┼──────────┼────────────┼────────────────────────────────┼────────┼──────────┼──────────┤
│ 14/07/2022 │ 14:30 │ united states │ USD      │ high       │ Initial Jobless Claims         │        │ 235K     │ 235K     │
├────────────┼───────┼───────────────┼──────────┼────────────┼────────────────────────────────┼────────┼──────────┼──────────┤
│ 14/07/2022 │ 14:30 │ united states │ USD      │ high       │ PPI (MoM)  (Jun)               │        │ 0.8%     │ 0.8%     │
├────────────┼───────┼───────────────┼──────────┼────────────┼────────────────────────────────┼────────┼──────────┼──────────┤
│ 15/07/2022 │ 14:30 │ united states │ USD      │ high       │ Core Retail Sales (MoM)  (Jun) │        │ 0.6%     │ 0.5%     │
├────────────┼───────┼───────────────┼──────────┼────────────┼────────────────────────────────┼────────┼──────────┼──────────┤
│ 15/07/2022 │ 14:30 │ united states │ USD      │ high       │ Retail Sales (MoM)  (Jun)      │        │ 0.8%     │ -0.3%    │
└────────────┴───────┴───────────────┴──────────┴────────────┴────────────────────────────────┴────────┴──────────┴──────────┘
```
