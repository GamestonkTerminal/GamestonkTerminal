from datetime import date
from typing import Optional
from urllib.parse import urlencode

# IMPORT THIRD-PARTY
import requests


root_url = "https://api.stlouisfed.org/fred"


class Fred:
    def __init__(self, api_key: Optional[str]):
        self.api_key = api_key

    def __fetch_data(self, url: str):
        full_url = f"{url}&api_key={self.api_key}&file_type=json"
        response = requests.get(full_url, timeout=10)
        return response.json()

    def get_series(
        self,
        series_id: str,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        **kwargs,
    ) -> dict:
        """
        Get data for a Fred series id. This fetches the latest known data.
        Code copied from: https://github.com/mortada/fredapi/blob/master/fredapi/fred.py

        Parameters
        ----------
        series_id : str
            Fred series id such as 'CPIAUCSL'
        start_date : date
            earliest observation date
        end_date : date
            latest observation date
        kwargs : additional parameters
            Any additional parameters supported by FRED. You can see the full list here:
            https://api.stlouisfed.org/docs/fred/series_observations.html

        Returns
        -------
        data : Series
            a Series where each index is the observation date and the value is the data for the Fred series
        """
        url = f"{root_url}/series/observations?series_id={series_id}"
        if start_date:
            url += "&observation_start=" + start_date.strftime("%Y-%m-%d")
        if end_date:
            url += "&observation_end=" + end_date.strftime("%Y-%m-%d")
        if kwargs.keys():
            url += "&" + urlencode(kwargs)
        root = self.__fetch_data(url)
        if root is None:
            raise ValueError("No data exists for series id: " + series_id)
        return root["observations"]
