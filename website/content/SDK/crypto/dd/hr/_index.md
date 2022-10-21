To obtain charts, make sure to add `chart=True` as the last parameter

## Get underlying data 
### crypto.dd.hr(symbol: str, interval: str = '24h', start_date: int = 1262304000, end_date: int = 1665471332) -> pandas.core.frame.DataFrame

Returns dataframe with mean hashrate of btc or eth blockchain and symbol price
    [Source: https://glassnode.com]

    Parameters
    ----------
    symbol : str
        Blockchain to check hashrate (BTC or ETH)
    start_date : int
        Initial date timestamp (e.g., 1_614_556_800)
    end_date : int
        End date timestamp (e.g., 1_614_556_800)
    interval : str
        Interval frequency (e.g., 24h)

    Returns
    -------
    pd.DataFrame
        mean hashrate and symbol price over time

## Getting charts 
### crypto.dd.hr(symbol: str, start_date: int = 1633935332, end_date: int = 1665471332, interval: str = '24h', export: str = '', external_axes: Optional[List[matplotlib.axes._axes.Axes]] = None, chart=True) -> None

Display dataframe with mean hashrate of btc or eth blockchain and symbol price.
    [Source: https://glassnode.org]

    Parameters
    ----------
    symbol : str
        Blockchain to check mean hashrate (BTC or ETH)
    start_date : int
        Initial date timestamp (e.g., 1_614_556_800)
    end_date : int
        End date timestamp (e.g., 1_614_556_800)
    interval : str
        Interval frequency (possible values are: 24, 1w, 1month)
    export : str
        Export dataframe data to csv,json,xlsx file
    external_axes : Optional[List[plt.Axes]], optional
        External axes (2 axes are expected in the list), by default None
