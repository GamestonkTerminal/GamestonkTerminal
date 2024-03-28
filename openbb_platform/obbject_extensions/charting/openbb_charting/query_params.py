"""Charting Extension Query Params."""

from typing import Any, Dict, List, Literal, Optional, Union

from openbb_core.provider.abstract.data import Data
from openbb_core.provider.abstract.query_params import QueryParams
from pydantic import Field

from openbb_charting.core.to_chart import ChartIndicators

MAMODES = Literal["ema", "sma", "wma", "hna", "zlma", "rma"]


def _get_type_name(t):
    """Get the type name of a type hint."""
    if isinstance(t, str):
        return t
    elif hasattr(t, "__origin__") and hasattr(t.__origin__, "__name__"):
        return f"{t.__origin__.__name__}[{', '.join([_get_type_name(arg) for arg in t.__args__])}]"
    elif hasattr(t, "__name__"):
        return t.__name__
    else:
        return str(t)


class BaseQueryParams(QueryParams):
    """Base Query Parmams Base Model."""

    def __init__(self, **data):
        super().__init__(**data)
        self.__doc__ = self.__repr__()

    def __repr__(self):
        fields = self.__class__.model_fields
        repr_str = (
            "\n"
            + self.__class__.__name__
            + "\n\n"
            + "    Parameters\n"
            + "    ----------\n"
            + "\n".join(
                [
                    f"\n    {k} ({_get_type_name(v.annotation)}):\n        {v.description}".replace(
                        ". ", ".\n        "
                    )
                    for k, v in fields.items()
                ]
            )
        )
        return repr_str


class ChartQueryParams(BaseQueryParams):

    data: Optional[Union[Data, List[Data]]] = Field(
        default=None,
        description="Filtered versions of the data contained in the original `self.results`."
        + " Columns should be the same as the original data."
        + " Example use is to reduce the number of columns, or the length of data, to plot.",
    )


class EquityPricePerformanceChartQueryParams(ChartQueryParams):
    """Equity Price Performance Chart Query Params."""

    title: Optional[str] = Field(
        default=None,
        description="Title of the chart.",
    )
    orientation: Literal["v", "h"] = Field(
        default="v",
        description="Orientation of the bars.",
    )
    limit: Optional[int] = Field(
        default=None,
        description="Limit the number of bars to plot, from the most recent."
        + " If None, the periods from one-day to five-years will be plotted, if available.",
    )
    layout_kwargs: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional keyword arguments to pass to the Plotly `update_layout` method.",
    )


class EtfPricePerformanceChartQueryParams(EquityPricePerformanceChartQueryParams):
    """ETF Price Performance Chart Query Params."""


class EquityPriceHistoricalChartQueryParams(ChartQueryParams):
    """Equity Historical Price Chart Query Params."""

    title: Optional[str] = Field(
        default=None,
        description="Title of the chart.",
    )
    target: Optional[str] = Field(
        default=None,
        description="The specific column to target. If supplied, this will override the candles and volume parameters.",
    )
    multi_symbol: bool = Field(
        default=False,
        description="Flag to indicate whether the data contains multiple symbols."
        + " This is mostly handled automatically, but if the chart fails to generate try setting this to True.",
    )
    same_axis: bool = Field(
        default=False,
        description="If True, forces all data to be plotted on the same axis.",
    )
    normalize: bool = Field(
        default=False,
        description="If True, the data will be normalized and placed on the same axis.",
    )
    returns: bool = Field(
        default=False,
        description="If True, the cumulative returns for the length of the time series will be calculated and plotted.",
    )
    candles: bool = Field(
        default=True,
        description="If True, and OHLC exists, and there is only one symbol in the data, candles will be plotted.",
    )
    heikin_ashi: bool = Field(
        default=False,
        description="If True, and `candles=True`, Heikin Ashi candles will be plotted.",
    )
    volume: bool = Field(
        default=True,
        description="If True, and volume exists, and `candles=True`, volume will be plotted.",
    )
    indicators: Optional[Union[ChartIndicators, Dict[str, Dict[str, Any]]]] = Field(
        default=None,
        description="Indicators to be plotted, formatted as a dictionary."
        + " Data containing multiple symbols will ignore indicators."
        + """
        Example:
            indicators = dict(
                sma=dict(length=[20,30,50]),
                adx=dict(length=14),
                rsi=dict(length=14),
            )""",
    )


class EconomyFredSeriesChartQueryParams(ChartQueryParams):
    """FRED Series Chart Query Params."""

    title: Optional[str] = Field(
        default=None,
        description="Title of the chart.",
    )
    y1title: Optional[str] = Field(
        default=None,
        description="Right Y-axis title.",
    )
    y2title: Optional[str] = Field(
        default=None,
        description="Left Y-axis title.",
    )
    xtitle: Optional[str] = Field(
        default=None,
        description="X-axis title.",
    )
    dropnan: bool = Field(
        default=True,
        description="If True, rows containing NaN will be dropped.",
    )
    normalize: bool = Field(
        default=False,
        description="If True, the data will be normalized and placed on the same axis.",
    )
    allow_unsafe: bool = Field(
        default=False,
        description="If True, the method will attempt to pass all supplied data to the chart constructor."
        + " This can result in unexpected behavior.",
    )


class TechnicalConesChartQueryParams(ChartQueryParams):
    """Technical Cones Chart Query Params."""

    title: Optional[str] = Field(
        default=None,
        description="Title of the chart.",
    )
    symbol: Optional[str] = Field(
        default=None,
        description="Symbol represented by the data. Used to label the chart.",
    )


class MAQueryParams(ChartQueryParams):
    """Moving Average Query Params."""

    target: str = Field(
        default="close",
        description="The column to calculate the moving average on.",
    )
    index: str = Field(
        default="date",
        description="The index column.",
    )
    length: Optional[Union[int, List[int]]] = Field(
        default=50,
        description="Window length for the moving average."
        "+ The number is relative to the interval of the time series data.",
    )
    offset: Optional[int] = Field(
        default=0,
        description="Number of periods to offset for the moving average.",
    )
    dropnan: bool = Field(
        default=False,
        description="If True, rows containing NaN will be dropped."
        + " This will reduce the length of the charted data by the longest window.",
    )
    symbol: Optional[str] = Field(
        default=None,
        description="Symbol represented by the data. Used to label the chart.",
    )


class TechnicalSMAChartQueryParams(MAQueryParams):
    """Technical SMA Chart Query Params."""


class TechnicalEMAChartQueryParams(MAQueryParams):
    """Technical EMA Chart Query Params."""


class TechnicalHMAChartQueryParams(MAQueryParams):
    """Technical HMA Chart Query Params."""


class TechnicalWMAChartQueryParams(MAQueryParams):
    """Technical WMA Chart Query Params."""


class TechnicalZLMAChartQueryParams(MAQueryParams):
    """Technical ZLMA Chart Query Params."""


class TechnicalADXChartQueryParams(ChartQueryParams):
    """Technical ADX Chart Query Params."""

    length: Optional[int] = Field(
        default=50,
        description="Window length for the ADX, by default is 50.",
    )
    scalar: Optional[float] = Field(
        default=100,
        description="Scalar to multiply the ADX by, default is 100.",
    )
    drift: Optional[int] = Field(
        default=1,
        description="Drift value for the ADX, by default is 1.",
    )


class TechnicalArooonChartQueryParams(ChartQueryParams):
    """Technical Aroon Chart Query Params."""

    length: Optional[int] = Field(
        default=25,
        description="Window length for the Aroon, by default is 50.",
    )
    scalar: Optional[float] = Field(
        default=100,
        description="Scalar to multiply the Aroon by, default is 100.",
    )


class TechnicalMACDChartQueryParams(ChartQueryParams):
    """Technical MACD Chart Query Params."""

    fast: Optional[int] = Field(
        default=12,
        description="Window length for the fast EMA, by default is 12.",
    )
    slow: Optional[int] = Field(
        default=26,
        description="Window length for the slow EMA, by default is 26.",
    )
    signal: Optional[int] = Field(
        default=9,
        description="Window length for the signal line, by default is 9.",
    )
    scalar: Optional[float] = Field(
        default=100,
        description="Scalar to multiply the MACD by, default is 100.",
    )


class TechnicalRSIChartQueryParams(ChartQueryParams):
    """Technical RSI Chart Query Params."""

    length: Optional[int] = Field(
        default=14,
        description="Window length for the RSI, by default is 14.",
    )
    scalar: Optional[float] = Field(
        default=100,
        description="Scalar to multiply the RSI by, default is 100.",
    )
    drift: Optional[int] = Field(
        default=1,
        description="Drift value for the RSI, by default is 1.",
    )


class ChartParams:
    """Chart Query Params."""

    crypto_price_historical = EquityPriceHistoricalChartQueryParams
    equity_price_historical = EquityPriceHistoricalChartQueryParams
    economy_fred_series = EconomyFredSeriesChartQueryParams
    equity_price_historical = EquityPriceHistoricalChartQueryParams
    equity_price_performance = EquityPricePerformanceChartQueryParams
    etf_historical = EtfPricePerformanceChartQueryParams
    etf_price_performance = EquityPricePerformanceChartQueryParams
    index_price_historical = EquityPriceHistoricalChartQueryParams
    technical_cones = TechnicalConesChartQueryParams
    technical_sma = TechnicalSMAChartQueryParams
    technical_ema = TechnicalEMAChartQueryParams
    technical_hma = TechnicalHMAChartQueryParams
    technical_wma = TechnicalWMAChartQueryParams
    technical_zlma = TechnicalZLMAChartQueryParams
    technical_adx = TechnicalADXChartQueryParams
    technical_aroon = TechnicalArooonChartQueryParams
    technical_macd = TechnicalMACDChartQueryParams
    technical_rsi = TechnicalRSIChartQueryParams


class IndicatorsQueryParams(BaseQueryParams):
    """Indicators Query Params."""


class MAIndicatorsQueryParams(IndicatorsQueryParams):
    """Moving Average Indicators Query Params."""

    length: Union[int, List[int]] = Field(
        default=50,
        description="Window length for the moving average, by default is 50."
        + " The number is relative to the interval of the time series data.",
    )
    offset: int = Field(
        default=0,
        description="Number of periods to offset for the moving average, by default is 0.",
    )


class SMAIndicatorsQueryParams(MAIndicatorsQueryParams):
    """Simple Moving Average Indicators Query Params."""


class EMAIndicatorsQueryParams(MAIndicatorsQueryParams):
    """Exponential Moving Average Indicators Query Params."""


class HMAIndicatorsQueryParams(MAIndicatorsQueryParams):
    """Hull Moving Average Indicators Query Params."""


class WMAIndicatorsQueryParams(MAIndicatorsQueryParams):
    """Weighted Moving Average Indicators Query Params."""


class ZLMAIndicatorsQueryParams(MAIndicatorsQueryParams):
    """Zero-Lag Moving Average Indicators Query Params."""


class ADIndicatorsQueryParams(IndicatorsQueryParams):
    """Accumulation/Distribution Indicators Query Params."""

    offset: int = Field(
        default=0,
        description="Offset value for the AD, by default is 0.",
    )


class ADOscillatorIndicatorsQueryParams(IndicatorsQueryParams):
    """Accumulation/Distribution Oscillator Indicators Query Params."""

    fast: int = Field(
        default=3,
        description="Number of periods to use for the fast calculation, by default 3.",
    )
    slow: int = Field(
        default=10,
        description="Number of periods to use for the slow calculation, by default 10.",
    )
    offset: int = Field(
        default=0,
        description="Offset to be used for the calculation, by default is 0.",
    )


class ADXIndicatorsQueryParams(IndicatorsQueryParams):
    """Average Directional Index Indicators Query Params."""

    length: int = Field(
        default=50,
        description="Window length for the ADX, by default is 50.",
    )
    scalar: float = Field(
        default=100,
        description="Scalar to multiply the ADX by, default is 100.",
    )
    drift: int = Field(
        default=1,
        description="Drift value for the ADX, by default is 1.",
    )


class AroonIndicatorsQueryParams(IndicatorsQueryParams):
    """Aroon Indicators Query Params."""

    length: int = Field(
        default=25,
        description="Window length for the Aroon, by default is 50.",
    )
    scalar: float = Field(
        default=100,
        description="Scalar to multiply the Aroon by, default is 100.",
    )


class ATRIndicatorsQueryParams(IndicatorsQueryParams):
    """Average True Range Indicators Query Params."""

    length: int = Field(
        default=14,
        description="Window length for the ATR, by default is 14.",
    )
    mamode: Literal["rma", "ema", "sma", "wma"] = Field(
        default="rma",
        description="The mode to use for the moving average calculation.",
    )
    drift: int = Field(
        default=1,
        description="The difference period.",
    )
    offset: int = Field(
        default=0,
        description="Number of periods to offset the result, by default is 0.",
    )


class CCIIndicatorsQueryParams(IndicatorsQueryParams):
    """Commodity Channel Index Indicators Query Params."""

    length: int = Field(
        default=14,
        description="Window length for the CCI, by default is 14.",
    )
    scalar: float = Field(
        default=0.015,
        description="Scalar to multiply the CCI by, default is 0.015.",
    )


class DonchianIndicatorsQueryParams(IndicatorsQueryParams):
    """Donchian Channel Indicators Query Params."""

    lower: Optional[int] = Field(
        default=20,
        description="Window length for the lower band, by default is 20.",
    )
    upper: Optional[int] = Field(
        default=20,
        description="Window length for the upper band, by default is 20.",
    )
    offset: Optional[int] = Field(
        default=0,
        description="Number of periods to offset the result, by default is 0.",
    )


class FisherIndicatorsQueryParams(IndicatorsQueryParams):
    """Fisher Transform Indicators Query Params."""

    length: int = Field(
        default=14,
        description="Window length for the Fisher Transform, by default is 14.",
    )
    signal: int = Field(
        default=1,
        description="Fisher Signal Period",
    )


class KCIndicatorsQueryParams(IndicatorsQueryParams):
    """Keltner Channel Indicators Query Params."""

    length: int = Field(
        default=20,
        description="Window length for the Keltner Channel, by default is 20.",
    )
    scalar: float = Field(
        default=20,
        description="Scalar to multiply the ATR, by default is 20.",
    )
    mamode: MAMODES = Field(
        default="rma",
        description="The mode to use for the moving average calculation, by default is ema.",
    )
    offset: int = Field(
        default=0,
        description="Number of periods to offset the result, by default is 0.",
    )


class OBVIndicatorsQueryParams(IndicatorsQueryParams):
    """On Balance Volume Indicators Query Params."""

    offset: int = Field(
        default=0,
        description="Number of periods to offset the result, by default is 0.",
    )


class RSIIndicatorsQueryParams(IndicatorsQueryParams):
    """RSI Indicators Query Params."""

    length: int = Field(
        default=14,
        description="Window length for the RSI, by default is 14.",
    )
    scalar: float = Field(
        default=100,
        description="Scalar to multiply the RSI by, default is 100.",
    )
    drift: int = Field(
        default=1,
        description="Drift value for the RSI, by default is 1.",
    )


class StochIndicatorsQueryParams(IndicatorsQueryParams):
    """Stochastic Oscillator Indicators Query Params."""

    fast_k: int = Field(
        default=14,
        description="The fast K period, by default 14.",
    )
    slow_d: int = Field(
        default=3,
        description="The slow D period, by default 3.",
    )
    slow_k: int = Field(
        default=3,
        description="The slow K period, by default 3.",
    )


class FibIndicatorsQueryParams(IndicatorsQueryParams):
    """Fibonacci Retracement Indicators Query Params."""

    period: int = Field(
        default=120,
        description="The period to calculate the Fibonacci Retracement, by default 120.",
    )
    start_date: Optional[str] = Field(
        default=None,
        description="The start date for the Fibonacci Retracement.",
    )
    end_date: Optional[str] = Field(
        default=None,
        description="The end date for the Fibonacci Retracement.",
    )


class ClenowIndicatorsQueryParams(IndicatorsQueryParams):
    """Clenow Volatility Adjusted Momentum Indicators Query Params."""

    period: int = Field(
        default=90,
        description="The number of periods for the momentum, by default 90.",
    )


class DemarkIndicatorsQueryParams(IndicatorsQueryParams):
    """Demark Indicators Query Params."""

    show_all: bool = Field(
        default=False,
        description="Show 1 - 13. If set to False, show 6 - 9.",
    )
    offset: int = Field(
        default=0,
        description="Number of periods to offset the result, by default is 0.",
    )


class IchimokuIndicatorsQueryParams(IndicatorsQueryParams):
    """Ichimoku Cloud Indicators Query Params."""

    conversion: int = Field(
        default=9,
        description="The conversion line period, by default 9.",
    )
    base: int = Field(
        default=26,
        description="The base line period, by default 26.",
    )
    lagging: int = Field(
        default=52,
        description="The lagging line period, by default 52.",
    )
    offset: int = Field(
        default=26,
        description="The offset period, by default 26.",
    )
    lookahead: bool = Field(
        default=False,
        description="Drops the Chikou Span Column to prevent potential data leak",
    )


class SRLinesIndicatorsQueryParams(IndicatorsQueryParams):
    """Support and Resistance Lines Indicators Query Params."""

    show: bool = Field(
        default=True,
        description="Show the support and resistance lines.",
    )


class IndicatorsParams(QueryParams):
    """Indicators Query Params."""

    sma: SMAIndicatorsQueryParams = Field(
        default=SMAIndicatorsQueryParams(),
        description=repr(SMAIndicatorsQueryParams()),
    )
    ema: EMAIndicatorsQueryParams = Field(
        default=EMAIndicatorsQueryParams(),
        description=repr(EMAIndicatorsQueryParams()),
    )
    hma: HMAIndicatorsQueryParams = Field(
        default=HMAIndicatorsQueryParams(),
        description=repr(HMAIndicatorsQueryParams()),
    )
    wma: WMAIndicatorsQueryParams = Field(
        default=WMAIndicatorsQueryParams(),
        description=repr(WMAIndicatorsQueryParams()),
    )
    zlma: ZLMAIndicatorsQueryParams = Field(
        default=ZLMAIndicatorsQueryParams(),
        description=repr(ZLMAIndicatorsQueryParams()),
    )
    ad: ADIndicatorsQueryParams = Field(
        default=ADIndicatorsQueryParams(),
        description=repr(ADIndicatorsQueryParams()),
    )
    adoscillator: ADOscillatorIndicatorsQueryParams = Field(
        default=ADOscillatorIndicatorsQueryParams(),
        description=repr(ADOscillatorIndicatorsQueryParams()),
    )
    adx: ADXIndicatorsQueryParams = Field(
        default=ADXIndicatorsQueryParams(),
        description=repr(ADXIndicatorsQueryParams()),
    )
    aroon: AroonIndicatorsQueryParams = Field(
        default=AroonIndicatorsQueryParams(),
        description=repr(AroonIndicatorsQueryParams()),
    )
    atr: ATRIndicatorsQueryParams = Field(
        default=ATRIndicatorsQueryParams(),
        description=repr(ATRIndicatorsQueryParams()),
    )
    cci: CCIIndicatorsQueryParams = Field(
        default=CCIIndicatorsQueryParams(),
        description=repr(CCIIndicatorsQueryParams()),
    )
    clenow: ClenowIndicatorsQueryParams = Field(
        default=ClenowIndicatorsQueryParams(),
        description=repr(ClenowIndicatorsQueryParams()),
    )
    demark: DemarkIndicatorsQueryParams = Field(
        default=DemarkIndicatorsQueryParams(),
        description=repr(DemarkIndicatorsQueryParams()),
    )
    donchian: DonchianIndicatorsQueryParams = Field(
        default=DonchianIndicatorsQueryParams(),
        description=repr(DonchianIndicatorsQueryParams()),
    )
    fib: FibIndicatorsQueryParams = Field(
        default=FibIndicatorsQueryParams(),
        description=repr(FibIndicatorsQueryParams()),
    )
    fisher: FisherIndicatorsQueryParams = Field(
        default=FisherIndicatorsQueryParams(),
        description=repr(FisherIndicatorsQueryParams()),
    )
    ichimoku: IchimokuIndicatorsQueryParams = Field(
        default=IchimokuIndicatorsQueryParams(),
        description=repr(IchimokuIndicatorsQueryParams()),
    )
    kc: KCIndicatorsQueryParams = Field(
        default=KCIndicatorsQueryParams(),
        description=repr(KCIndicatorsQueryParams()),
    )
    obv: OBVIndicatorsQueryParams = Field(
        default=OBVIndicatorsQueryParams(),
        description=repr(OBVIndicatorsQueryParams()),
    )
    rsi: RSIIndicatorsQueryParams = Field(
        default=RSIIndicatorsQueryParams(),
        description=repr(RSIIndicatorsQueryParams()),
    )
    srlines: SRLinesIndicatorsQueryParams = Field(
        default=SRLinesIndicatorsQueryParams(),
        description=repr(SRLinesIndicatorsQueryParams()),
    )
    stoch: StochIndicatorsQueryParams = Field(
        default=StochIndicatorsQueryParams(),
        description=repr(StochIndicatorsQueryParams()),
    )

    def __repr__(self):
        fields = self.__class__.model_fields
        repr_str = "\n" + "\n".join(
            [
                f"{str(v.description).replace('IndicatorsQueryParams', ':').replace('ADOs', 'AD Os')}"
                for k, v in fields.items()
            ]
        )
        return repr_str
