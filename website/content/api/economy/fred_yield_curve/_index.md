To obtain charts, make sure to add `chart=True` as the last parameter

## Get underlying data 
### economy.fred_yield_curve(date: datetime.datetime = None) -> Tuple[pandas.core.frame.DataFrame, str]

Gets yield curve data from FRED

    Parameters
    ----------
    date: datetime
        Date to get curve for.  If None, gets most recent date

    Returns
    -------
    pd.DataFrame:
        Dataframe of yields and maturities
    str
        Date for which the yield curve is obtained

## Getting charts 
### economy.fred_yield_curve(date: datetime.datetime = datetime.datetime(2022, 10, 11, 7, 55, 32, 575569, chart=True), external_axes: Optional[List[matplotlib.axes._axes.Axes]] = None, raw: bool = False, export: str = '')

Display yield curve based on US Treasury rates for a specified date.

    Parameters
    ----------
    date: datetime
        Date to get yield curve for
    external_axes: Optional[List[plt.Axes]]
        External axes to plot data on
