"""Yahoo Finance active fetcher."""
import re
from typing import Any, Dict, List, Optional

import pandas as pd
import requests
from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.equity_performance import (
    EquityPerformanceData,
    EquityPerformanceQueryParams,
)
from pydantic import Field


class YFActiveQueryParams(EquityPerformanceQueryParams):
    """YF asset performance active QueryParams.

    Source: https://finance.yahoo.com/screener/predefined/most_actives
    """


class YFActiveData(EquityPerformanceData):
    """YF asset performance active Data."""

    __alias_dict__ = {
        "symbol": "Symbol",
        "name": "Name",
        "volume": "Volume",
        "change": "Change",
        "price": "Price (Intraday)",
        "percent_change": "% Change",
        "market_cap": "Market Cap",
        "avg_volume_3_months": "Avg Vol (3 month)",
        "pe_ratio_ttm": "PE Ratio (TTM)",
    }

    market_cap: str = Field(
        description="Market Cap displayed in billions.",
    )
    avg_volume_3_months: float = Field(
        description="Average volume over the last 3 months in millions.",
    )
    pe_ratio_ttm: Optional[float] = Field(
        description="PE Ratio (TTM).",
        default=None,
    )


class YFActiveFetcher(Fetcher[YFActiveQueryParams, List[YFActiveData]]):
    """YF asset performance active Fetcher."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> YFActiveQueryParams:
        """Transform query params."""
        return YFActiveQueryParams(**params)

    @staticmethod
    def extract_data(
        query: YFActiveQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Get data from YF."""
        headers = {"user_agent": "Mozilla/5.0"}
        html = requests.get(
            "https://finance.yahoo.com/screener/predefined/most_actives",
            headers=headers,
            timeout=10,
        ).text
        html_clean = re.sub(r"(<span class=\"Fz\(0\)\">).*?(</span>)", "", html)
        df = (
            pd.read_html(html_clean, header=None)[0]
            .dropna(how="all", axis=1)
            .replace(float("NaN"), "")
        )
        df["% Change"] = df["% Change"].str.replace("%", "")
        df["Volume"] = df["Volume"].str.replace("M", "").astype(float) * 1000000
        df["Avg Vol (3 month)"] = (
            df["Avg Vol (3 month)"].str.replace("M", "").astype(float) * 1000000
        )
        df = df.apply(pd.to_numeric, errors="ignore")
        return df.to_dict(orient="records")

    @staticmethod
    def transform_data(
        query: EquityPerformanceQueryParams,
        data: List[Dict],
        **kwargs: Any,
    ) -> List[YFActiveData]:
        """Transform data."""
        data = sorted(data, key=lambda d: d["Volume"], reverse=query.sort == "desc")
        return [YFActiveData.model_validate(d) for d in data]
