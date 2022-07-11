```
usage: desc [-n {OPTIONS}] [-h] [--export {csv,json,xlsx}]
```

Plot correlation coefficients of a dataset.

```
optional arguments:
  -d {TSLA}, --target-dataset {TSLA}
                        The name of the dataset you want to select (default: None)
  -h, --help            show this help message (default: False)
  --export EXPORT       Export figure into png, jpg, pdf, svg (default: )

For more information and examples, use 'about corr' to access the related guide.
```

Example:
```
(🦋) /forecasting/ $ load TSLA.csv

(🦋) /forecasting/ $ corr TSLA
TODO: screen shot

```
