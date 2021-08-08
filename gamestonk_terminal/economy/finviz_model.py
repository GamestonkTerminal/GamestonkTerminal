""" Finviz Model """
__docformat__ = "numpy"

from finvizfinance.group import valuation, performance, spectrum


def get_valuation_performance_data(group: str, data_type: str):
    """Get group (sectors, industry or country) valuation/performance data

    Parameters
    ----------
    group : str
       sectors, industry or country
    data_type : str
       valuation or performance

    Returns
    ----------
    pd.DataFrame
        dataframe with valuation/performance data
    """
    if data_type == "valuation":
        return valuation.Valuation().ScreenerView(group=group)
    return performance.Performance().ScreenerView(group=group)


def get_spectrum_data(group: str):
    """Get group (sectors, industry or country) valuation/performance data

    Parameters
    ----------
    group : str
       sectors, industry or country
    """
    spectrum.Spectrum().ScreenerView(group=group)
