""" Alpha Vantage View """
__docformat__ = "numpy"

import os
import matplotlib.pyplot as plt
from gamestonk_terminal.helper_funcs import export_data
from gamestonk_terminal.economy import alphavantage_model
from gamestonk_terminal import feature_flags as gtff


def realtime_performance_sector(raw: bool, export: str):
    """Display Real-Time Performance sector. [Source: AlphaVantage]

    Parameters
    ----------
    raw : bool
        Output only raw data
    export : str
        Export dataframe data to csv,json,xlsx file
    """
    df_sectors = alphavantage_model.get_sector_data()

    if raw:
        df_sec = df_sectors["Rank A: Real-Time Performance"].copy()
        print(df_sec.to_string())

    else:
        # pylint: disable=invalid-sequence-index
        df_sectors["Rank A: Real-Time Performance"].plot(kind="bar")
        plt.title("Real Time Performance (%) per Sector")
        plt.tight_layout()
        plt.grid()
        if gtff.USE_ION:
            plt.ion()
        plt.show()
    print("")

    export_data(
        export,
        os.path.dirname(os.path.abspath(__file__)),
        "rtps",
        df_sectors,
    )
