"""Trading Economics Earnings Calendar fetcher."""


from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, Set, Union

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.economic_calendar import (
    EconomicCalendarData,
    EconomicCalendarQueryParams,
)
from openbb_provider.utils.helpers import make_request
from openbb_provider.utils.countries import country_list
from openbb_tradingeconomics.utils import url_generator
from pandas import to_datetime
from pydantic import Field, field_validator

IMPORTANCE = Literal["Low", "Medium", "High"]

GROUPS = Literal[
    "interest rate",
    "inflation",
    "bonds",
    "consumer",
    "gdp",
    "government",
    "housing",
    "labour",
    "markets",
    "money",
    "prices",
    "trade",
    "business",
]


class TEEconomicCalendarQueryParams(EconomicCalendarQueryParams):
    """TE Economic Calendar Query.

    Source: https://docs.tradingeconomics.com/economic_calendar/
    """

    country: Optional[Union[str, List[str]]] = Field(
        default=None,
        description="Country of the event",
    )
    # TODO: Probably want to figure out the list we can use.
    importance: IMPORTANCE = Field(
        default=None,
        description="Importance of the event.",
    )
    group: GROUPS = Field(default=None, description="Grouping of events")

    @field_validator("country", mode="before", check_fields=False)
    @classmethod
    def validate_country(cls, v: Union[str, List[str], Set[str]]):
        """Validate the country input."""
        if isinstance(v, str):
            return v.lower().replace(" ", "_")
        return ",".join([country.lower().replace(" ", "_") for country in list(v)])

    @field_validator("importance")
    @classmethod
    def importance_to_number(cls, v):
        string_to_value = {"Low": 1, "Medium": 2, "High": 3}
        return string_to_value[v] if v else None


class TEEconomicCalendarData(EconomicCalendarData):
    """TE Economic Calendar Data."""

    __alias_dict__ = {
        "date": "Date",
        "country": "Country",
        "category": "Category",
        "event": "Event",
        "reference": "Reference",
        "source": "Source",
        "sourceurl": "SourceURL",
        "actual": "Actual",
        "consensus": "Forecast",
        "forecast": "TEForecast",
        "url": "URL",
        "importance": "Importance",
        "currency": "Currency",
        "unit": "Unit",
        "ticker": "Ticker",
        "symbol": "Symbol",
        "previous": "Previous",
        "revised": "Revised",
    }

    category: Optional[str] = Field(default=None, description="Category of event.")
    reference: Optional[str] = Field(
        default=None,
        description="Abbreviated period for which released data refers to.",
    )
    source: Optional[str] = Field(default=None, description="Source of the data.")
    sourceurl: Optional[str] = Field(default=None, description="Source URL.")
    forecast: Optional[str] = Field(
        default=None, description="Trading Economics projections"
    )
    url: Optional[str] = Field(default=None, description="Trading Economics URL")
    importance: Optional[Literal[1, 2, 3]] = Field(
        default=None, description="Importance of the event. 1-Low, 2-Medium, 3-High"
    )
    currency: Optional[str] = Field(default=None, description="Currency of the data.")
    unit: Optional[str] = Field(default=None, description="Unit of the data.")

    @field_validator("date", mode="before")
    @classmethod
    def validate_date(cls, v: str) -> datetime:
        return to_datetime(v, utc=True)


class TEEconomicCalendarFetcher(
    Fetcher[
        TEEconomicCalendarQueryParams,
        List[TEEconomicCalendarData],
    ]
):
    """Transform the query, extract and transform the data from the TE endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> TEEconomicCalendarQueryParams:
        """Transform the query params."""
        return TEEconomicCalendarQueryParams(**params)

    @staticmethod
    def extract_data(
        query: TEEconomicCalendarQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the TE endpoint."""
        api_key = credentials.get("tradingeconomics_api_key") if credentials else ""

        if query.country is not None:
            country = (
                query.country.split(",") if "," in query.country else query.country
            )
            country = [country] if isinstance(country, str) else country

            for c in country:
                if c.replace("_", " ").lower() not in country_list:
                    raise ValueError(f"{c} is not a valid country")
            query.country = country

        url = url_generator.generate_url(query)
        if not url:
            raise RuntimeError(
                "No url generated. Check combination of input parameters."
            )
        url = f"{url}{api_key}"
        response = make_request(url, **kwargs)
        if response.status_code != 200:
            raise RuntimeError(f"Error in TE request -> {response.text}")
        return response.json()

    @staticmethod
    def transform_data(
        query: TEEconomicCalendarQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[TEEconomicCalendarData]:
        """Return the transformed data."""
        return [TEEconomicCalendarData.model_validate(d) for d in data]
