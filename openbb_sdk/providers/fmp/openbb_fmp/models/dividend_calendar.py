"""FMP Dividend Calendar fetcher."""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.models.dividend_calendar import (
    DividendCalendarData,
    DividendCalendarQueryParams,
)
from pydantic import validator

from openbb_fmp.utils.helpers import get_data_many, get_querystring


class FMPDividendCalendarQueryParams(DividendCalendarQueryParams):
    """FMP Dividend Calendar Query.

    Source: https://site.financialmodelingprep.com/developer/docs/dividend-calendar-api/

    The maximum time interval between the start and end date can be 3 months.
    Default value for time interval is 1 month.
    """


class FMPDividendCalendarData(DividendCalendarData):
    """FMP Dividend Calendar Data."""

    class Config:
        fields = {
            "adj_dividend": "adjDividend",
            "record_date": "recordDate",
            "payment_date": "paymentDate",
            "declaration_date": "declarationDate",
        }

    @validator("date", pre=True, check_fields=False)
    def date_validate(cls, v: str):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%d") if v else None

    @validator("recordDate", pre=True, check_fields=False)
    def record_date_validate(cls, v: str):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%d") if v else None

    @validator("paymentDate", pre=True, check_fields=False)
    def payment_date_validate(cls, v: str):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%d") if v else None

    @validator("declarationDate", pre=True, check_fields=False)
    def declaration_date_validate(cls, v: str):  # pylint: disable=E0213
        return datetime.strptime(v, "%Y-%m-%d") if v else None


class FMPDividendCalendarFetcher(
    Fetcher[
        DividendCalendarQueryParams,
        DividendCalendarData,
        FMPDividendCalendarQueryParams,
        FMPDividendCalendarData,
    ]
):
    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPDividendCalendarQueryParams:
        now = datetime.now().date()
        transformed_params = params
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - timedelta(days=31)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now - timedelta(days=1)
        return FMPDividendCalendarQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: FMPDividendCalendarQueryParams, credentials: Optional[Dict[str, str]]
    ) -> List[FMPDividendCalendarData]:
        api_key = credentials.get("fmp_api_key") if credentials else ""

        base_url = "https://financialmodelingprep.com/api/v3"
        query_str = get_querystring(query.dict(by_alias=True), [])
        query_str = query_str.replace("start_date", "from").replace("end_date", "to")
        url = f"{base_url}/stock_dividend_calendar?{query_str}&apikey={api_key}"
        return get_data_many(url, FMPDividendCalendarData)

    @staticmethod
    def transform_data(
        data: List[FMPDividendCalendarData],
    ) -> List[FMPDividendCalendarData]:
        return data
