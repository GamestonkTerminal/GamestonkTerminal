"""Alpha Vantage Stock End of Day fetcher."""


from datetime import datetime
from typing import Any, Dict, List, Literal, Optional, get_args

import pandas as pd
from dateutil.relativedelta import relativedelta
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.stock_eod import StockEODData, StockEODQueryParams
from openbb_provider.utils.descriptions import DATA_DESCRIPTIONS
from openbb_provider.utils.helpers import get_querystring
from pydantic import Field, NonNegativeFloat, PositiveFloat, root_validator, validator


class AlphaVantageStockEODQueryParams(StockEODQueryParams):
    """Alpha Vantage Stock End of Day Query.

    Source: https://www.alphavantage.co/documentation/
    """

    function: Literal[
        "TIME_SERIES_INTRADAY",
        "TIME_SERIES_DAILY",
        "TIME_SERIES_WEEKLY",
        "TIME_SERIES_MONTHLY",
    ] = Field(
        description="The time series of your choice. ",
        default="TIME_SERIES_DAILY",
    )
    interval: Optional[Literal["1min", "5min", "15min", "30min", "60min"]] = Field(
        description="The interval between two consecutive data points in the time series.",
        default="60min",
        available_on_functions=["TIME_SERIES_INTRADAY"],
        required_on_functions=["TIME_SERIES_INTRADAY"],
    )
    adjusted: Optional[bool] = Field(
        description="Output time series is adjusted by historical split and dividend events.",
        default=True,
        available_on_functions=["TIME_SERIES_INTRADAY"],
    )
    extended_hours: Optional[bool] = Field(
        description="Extended trading hours during pre-market and after-hours.",
        default=False,
        available_on_functions=["TIME_SERIES_INTRADAY"],
    )
    month: Optional[str] = Field(
        description="Query a specific month in history (in YYYY-MM format).",
        default=None,
        available_on_functions=["TIME_SERIES_INTRADAY"],
    )
    outputsize: Optional[Literal["compact", "full"]] = Field(
        description="Compact returns only the latest 100 data points in the intraday "
        "time series; full returns trailing 30 days of the most recent intraday data "
        "if the month parameter (see above) is not specified, or the full intraday "
        "data for a specific month in history if the month parameter is specified.",
        default="compact",
        available_on_functions=[
            "TIME_SERIES_INTRADAY",
            "TIME_SERIES_DAILY",
            "TIME_SERIES_DAILY_ADJUSTED",
        ],
    )

    @root_validator(pre=True)
    def adjusted_function_validate(cls, values):  # pylint: disable=E0213
        function = values["function"]
        adjusted = values.get("adjusted", None)

        if function != "TIME_SERIES_INTRADAY":
            values["function"] = function if not adjusted else f"{function}_ADJUSTED"

        return values

    @root_validator(pre=True)
    def on_functions_validate(cls, values):  # pylint: disable=E0213
        """
        Validate that the functions used on custom extra Field attributes
        `available_on_functions` and `required_on_functions` are valid functions.
        """
        custom_attributes = ["available_on_functions", "required_on_functions"]

        fields = cls.__fields__
        available_functions = get_args(getattr(fields["function"], "type_"))

        def validate_functions(functions: List[str]):
            for f in functions:
                if f not in available_functions:
                    raise ValueError(
                        f"Function {f} must be on of the following: {available_functions}"
                    )

        for field in fields:
            for attr in custom_attributes:
                if functions := fields[field].field_info.extra.get(attr, None):
                    validate_functions(functions)

        return values

    @root_validator
    def on_functions_criteria_validate(cls, values):  # pylint: disable=E0213
        """
        Validate that the fields are set to None if the function is not available
        and that the required fields are not None if the function is required.
        """

        fields = cls.__fields__
        function = values["function"]

        for field in fields:
            if (
                available_on_functions := fields[field].field_info.extra.get(
                    "available_on_functions", None
                )
            ) and function not in available_on_functions:
                values[field] = None
            if (
                (
                    required_on_functions := fields[field].field_info.extra.get(
                        "required_on_functions", None
                    )
                )
                and function in required_on_functions
                and values[field] is None
            ):
                raise ValueError(f"Field {field} is required on function {function}")

        return values

    @validator("month")
    def month_validate(cls, v):  # pylint: disable=E0213
        """Validate month, check if the month is in YYYY-MM format."""
        if v is not None:
            try:
                datetime.strptime(v, "%Y-%m")
            except ValueError as e:
                raise e
        return v


class AlphaVantageStockEODData(StockEODData):
    """Alpha Vantage Stock End of Day Data."""

    class Config:
        """Pydantic alias config using fields dict."""

        fields = {"date": "timestamp", "adj_close": "adjusted_close"}

    adjusted_close: PositiveFloat = Field(
        description=DATA_DESCRIPTIONS.get("adj_close", "")
    )
    dividend_amount: NonNegativeFloat = Field(
        description="Dividend amount paid for the corresponding date.",
    )
    split_coefficient: NonNegativeFloat = Field(
        description="Split coefficient for the corresponding date.",
    )


class AlphaVantageStockEODFetcher(
    Fetcher[
        AlphaVantageStockEODQueryParams,
        List[AlphaVantageStockEODData],
    ]
):
    """Transform the query, extract and transform the data from the Alpha Vantage endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> AlphaVantageStockEODQueryParams:
        """Transform the query."""

        transformed_params = params

        now = datetime.now().date()
        if params.get("start_date") is None:
            transformed_params["start_date"] = now - relativedelta(years=1)

        if params.get("end_date") is None:
            transformed_params["end_date"] = now

        return AlphaVantageStockEODQueryParams(**transformed_params)

    @staticmethod
    def extract_data(
        query: AlphaVantageStockEODQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> dict:
        """Return the raw data from the Alpha Vantage endpoint."""

        api_key = credentials.get("alpha_vantage_api_key") if credentials else ""

        query_str = get_querystring(query.dict(), ["start_date", "end_date"])

        url = f"https://www.alphavantage.co/query?{query_str}&datatype=csv&apikey={api_key}"

        data = pd.read_csv(url)
        data["timestamp"] = pd.to_datetime(data["timestamp"])

        data = data[
            (data["timestamp"] >= pd.to_datetime(query.start_date))
            & (data["timestamp"] <= pd.to_datetime(query.end_date))
        ]

        return data.to_dict("records")

    @staticmethod
    def transform_data(
        data: dict,
    ) -> List[AlphaVantageStockEODData]:
        """Transform the data to the standard format."""

        return [AlphaVantageStockEODData.parse_obj(**d) for d in data]
