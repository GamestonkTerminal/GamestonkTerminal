```
usage: tft [--lstm-layers LSTM_LAYERS] [--num-attention-heads NUM_ATTENTION_HEADS] [--full-attention] [--hidden-continuous-size HIDDEN_CONTINUOUS_SIZE] [--hidden-size HIDDEN_SIZE] [--past-covariates PAST_COVARIATES] [-d {GME}]
           [-c TARGET_COLUMN] [-n N_DAYS] [--forecast-horizon FORECAST_HORIZON] [-t TRAIN_SPLIT] [-i INPUT_CHUNK_LENGTH] [-o OUTPUT_CHUNK_LENGTH] [--force-reset FORCE_RESET] [--save-checkpoints SAVE_CHECKPOINTS]
           [--model-save-name MODEL_SAVE_NAME] [--n-epochs N_EPOCHS] [--dropout DROPOUT] [--batch-size BATCH_SIZE] [--residuals] [-f] [-h] [--export EXPORT]
```

Perform TFT forecast (Temporal Fusion Transformer).

```
optional arguments:

  --lstm-layers LSTM_LAYERS
                        Number of LSTM layers. (default: 1)
  --num-attention-heads NUM_ATTENTION_HEADS
                        Number of attention heads. (default: 4)
  --full-attention      Whether to apply a multi-head attention query. (default: False)
  --hidden-continuous-size HIDDEN_CONTINUOUS_SIZE
                        Default hidden size for processing continuous variables. (default: 8)
  --hidden-size HIDDEN_SIZE
                        Size for feature maps for each hidden RNN layer (h_n) (default: 16)
  --past-covariates PAST_COVARIATES
                        Past covariates(columns/features) in same dataset. Comma separated. (default: None)
  -d {GME}, --target-dataset {GME}
                        The name of the dataset you want to select (default: None)
  -c TARGET_COLUMN, --target-column TARGET_COLUMN
                        The name of the specific column you want to use (default: close)
  -n N_DAYS, --n-days N_DAYS
                        prediction days. (default: 5)
  --forecast-horizon FORECAST_HORIZON
                        Days/Points to forecast for historical back-testing (default: 5)
  -t TRAIN_SPLIT, --train-split TRAIN_SPLIT
                        Start point for rolling training and forecast window. 0.0-1.0 (default: 0.85)
  -i INPUT_CHUNK_LENGTH, --input-chunk-length INPUT_CHUNK_LENGTH
                        Number of past time steps for forecasting module at prediction time. (default: 14)
  -o OUTPUT_CHUNK_LENGTH, --output-chunk-length OUTPUT_CHUNK_LENGTH
                        The length of the forecast of the model. (default: 5)
  --force-reset FORCE_RESET
                        If set to True, any previously-existing model with the same name will be reset (all checkpoints will be discarded). (default: True)
  --save-checkpoints SAVE_CHECKPOINTS
                        Whether to automatically save the untrained model and checkpoints. (default: True)
  --model-save-name MODEL_SAVE_NAME
                        Name of the model to save. (default: tft_model)
  --n-epochs N_EPOCHS   Number of epochs over which to train the model. (default: 100)
  --dropout DROPOUT     Fraction of neurons afected by Dropout. (default: 0.1)
  --batch-size BATCH_SIZE
                        Number of time series (input and output) used in each training pass (default: 32)
  --residuals           Show the residuals for the model. (default: False)
  -f, --forecast_only   Do not plot the hisotorical data without forecasts. (default: False)
  -h, --help            show this help message (default: False)
  --export EXPORT       Export figure into png, jpg, pdf, svg (default: )

For more information and examples, use 'about export' to access the related guide.
```

Example:
```
2022 Jul 23, 10:36 (🦋) /forecast/ $ load GME_20220719_123734.csv -a GME

2022 Jul 23, 11:03 (🦋) /forecast/ $ tft GME
100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 115/115 [00:07<00:00, 15.10it/s]
TFT model obtains MAPE: 44.60%



       Actual price: $ 146.64
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ Datetime            ┃ Prediction ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 2022-07-19 00:00:00 │ $ 169.69   │
├─────────────────────┼────────────┤
│ 2022-07-20 00:00:00 │ $ 168.53   │
├─────────────────────┼────────────┤
│ 2022-07-21 00:00:00 │ $ 167.33   │
├─────────────────────┼────────────┤
│ 2022-07-22 00:00:00 │ $ 167.23   │
├─────────────────────┼────────────┤
│ 2022-07-25 00:00:00 │ $ 165.82   │
└─────────────────────┴────────────┘
```
![tft](https://user-images.githubusercontent.com/72827203/180615444-47bcdd54-0693-4415-9617-ed3a571b26c6.png)
