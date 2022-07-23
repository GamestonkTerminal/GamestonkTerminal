```
usage: theta [-d {GME}] [-c TARGET_COLUMN] [-n N_DAYS] [--forecast-horizon FORECAST_HORIZON] [-s {N,A,M}] [-p SEASONAL_PERIODS] [-w START_WINDOW] [--residuals] [-f] [-h] [--export EXPORT]
```

Perform Theta forecast.

```
optional arguments:

  -d {GME}, --target-dataset {GME}
                        The name of the dataset you want to select (default: None)
  -c TARGET_COLUMN, --target-column TARGET_COLUMN
                        The name of the specific column you want to use (default: close)
  -n N_DAYS, --n-days N_DAYS
                        prediction days. (default: 5)
  --forecast-horizon FORECAST_HORIZON
                        Days/Points to forecast for historical back-testing (default: 5)
  -s {N,A,M}, --seasonal {N,A,M}
                        Seasonality: N: None, A: Additive, M: Multiplicative. (default: M)
  -p SEASONAL_PERIODS, --periods SEASONAL_PERIODS
                        Seasonal periods: 4: Quarterly, 7: Daily (default: 7)
  -w START_WINDOW, --window START_WINDOW
                        Start point for rolling training and forecast window. 0.0-1.0 (default: 0.85)
  --residuals           Show the residuals for the model. (default: False)
  -f, --forecast_only   Do not plot the hisotorical data without forecasts. (default: False)
  -h, --help            show this help message (default: False)
  --export EXPORT       Export figure into png, jpg, pdf, svg (default: )

For more information and examples, use 'about export' to access the related guide.
```

Example:
```
2022 Jul 23, 10:36 (🦋) /forecasting/ $ load GME_20220719_123734.csv -a GME

2022 Jul 23, 11:01 (🦋) /forecasting/ $ theta GME
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 115/115 [00:23<00:00,  4.88it/s]
Theta Model obtains MAPE: 12.71%



       Actual price: $ 146.64
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Datetime            ┃ Prediction ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 2022-07-19 00:00:00 │ $ 145.41   │
├─────────────────────┼────────────┤
│ 2022-07-20 00:00:00 │ $ 147.28   │
├─────────────────────┼────────────┤
│ 2022-07-21 00:00:00 │ $ 147.28   │
├─────────────────────┼────────────┤
│ 2022-07-22 00:00:00 │ $ 148.66   │
├─────────────────────┼────────────┤
│ 2022-07-25 00:00:00 │ $ 147.18   │
└─────────────────────┴────────────┘
```
![theta](https://user-images.githubusercontent.com/72827203/180615324-5b50445c-cc95-4efa-84a6-85e85ddc2d28.png)
