"""yfinance Major Indices end of day fetcher."""


from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.descriptions import QUERY_DESCRIPTIONS
from openbb_provider.models.major_indices_eod import (
    MajorIndicesEODData,
    MajorIndicesEODQueryParams,
)
from pydantic import Field, validator
from yfinance import Ticker

from openbb_yfinance.utils.types import INTERVALS, PERIODS


class YFinanceMajorIndicesEODQueryParams(MajorIndicesEODQueryParams):
    """YFinance Major Indices end of day Query.

    Source: https://finance.yahoo.com/world-indices
    """

    interval: Optional[INTERVALS] = Field(default="1d", description="Data granularity.")
    period: Optional[PERIODS] = Field(
        default=None, description=QUERY_DESCRIPTIONS.get("period", "")
    )


class YFinanceMajorIndicesEODData(MajorIndicesEODData):
    """YFinance Major Indices end of day Data."""

    class Config:
        fields = {
            "date": "Date",
            "open": "Open",
            "high": "High",
            "low": "Low",
            "close": "Close",
            "volume": "Volume",
        }

    @validator("Date", pre=True, check_fields=False)
    def date_validate(cls, v):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%dT%H:%M:%S")


class YFinanceMajorIndicesEODFetcher(
    Fetcher[
        MajorIndicesEODQueryParams,
        MajorIndicesEODData,
        YFinanceMajorIndicesEODQueryParams,
        YFinanceMajorIndicesEODData,
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFinanceMajorIndicesEODQueryParams:
        now = datetime.now().date()
        transformed_params = params
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - timedelta(days=7)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now
        return YFinanceMajorIndicesEODQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFinanceMajorIndicesEODQueryParams, credentials: Optional[Dict[str, str]]
    ) -> List[YFinanceMajorIndicesEODData]:
        query.symbol = f"^{query.symbol}"

        now = datetime.now().date()
        query.start_date = query.start_date or (now - timedelta(days=8))
        query.end_date = query.end_date or (now - timedelta(days=1))

        if query.period:
            data = Ticker(query.symbol).history(
                interval=query.interval,
                period=query.period,
                actions=False,
                raise_errors=True,
            )
        else:
            data = Ticker(query.symbol).history(
                interval=query.interval,
                start=query.start_date,
                end=query.end_date,
                actions=False,
                raise_errors=True,
            )

        data = data.reset_index()
        data["Date"] = (
            data["Date"].dt.tz_localize(None).dt.strftime("%Y-%m-%dT%H:%M:%S")
        )
        data = data.to_dict("records")

        return [YFinanceMajorIndicesEODData(**d) for d in data]

    @staticmethod
    def transform_data(
        data: List[YFinanceMajorIndicesEODData],
    ) -> List[YFinanceMajorIndicesEODData]:
        return data
