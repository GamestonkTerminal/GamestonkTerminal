"""FMP Analyst Estimates fetcher."""


from typing import Any, Dict, List, Optional

from openbb_provider.abstract.fetcher import Fetcher
from openbb_provider.standard_models.analyst_estimates import (
    AnalystEstimatesData,
    AnalystEstimatesQueryParams,
)

from openbb_fmp.utils.helpers import create_url, get_data_many


class FMPAnalystEstimatesQueryParams(AnalystEstimatesQueryParams):
    """FMP Analysts Estimates Query.

    Source: https://site.financialmodelingprep.com/developer/docs/analyst-estimates-api/
    """


class FMPAnalystEstimatesData(AnalystEstimatesData):
    """FMP Analyst Estimates Data."""

    class Config:
        """Pydantic alias config using fields Dict."""

        fields = {
            "estimated_revenue_low": "estimatedRevenueLow",
            "estimated_revenue_high": "estimatedRevenueHigh",
            "estimated_revenue_avg": "estimatedRevenueAvg",
            "estimated_ebitda_low": "estimatedEbitdaLow",
            "estimated_ebitda_high": "estimatedEbitdaHigh",
            "estimated_ebitda_avg": "estimatedEbitdaAvg",
            "estimated_ebit_low": "estimatedEbitLow",
            "estimated_ebit_high": "estimatedEbitHigh",
            "estimated_ebit_avg": "estimatedEbitAvg",
            "estimated_net_income_low": "estimatedNetIncomeLow",
            "estimated_net_income_high": "estimatedNetIncomeHigh",
            "estimated_net_income_avg": "estimatedNetIncomeAvg",
            "estimated_sga_expense_low": "estimatedSgaExpenseLow",
            "estimated_sga_expense_high": "estimatedSgaExpenseHigh",
            "estimated_sga_expense_avg": "estimatedSgaExpenseAvg",
            "estimated_eps_avg": "estimatedEpsAvg",
            "estimated_eps_high": "estimatedEpsHigh",
            "estimated_eps_low": "estimatedEpsLow",
            "number_analyst_estimated_revenue": "numberAnalystEstimatedRevenue",
            "number_analysts_estimated_eps": "numberAnalystsEstimatedEps",
        }


class FMPAnalystEstimatesFetcher(
    Fetcher[
        FMPAnalystEstimatesQueryParams,
        List[FMPAnalystEstimatesData],
    ]
):
    """Transform the query, extract and transform the data from the FMP endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> FMPAnalystEstimatesQueryParams:
        """Transform the query params."""

        return FMPAnalystEstimatesQueryParams(**params)

    @staticmethod
    def extract_data(
        query: FMPAnalystEstimatesQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the FMP endpoint."""

        api_key = credentials.get("fmp_api_key") if credentials else ""

        query.period = "quarter" if query.period == "quarterly" else "annual"

        url = create_url(
            3, f"analyst-estimates/{query.symbol}", api_key, query, ["symbol"]
        )

        return get_data_many(url, **kwargs)

    @staticmethod
    def transform_data(data: List[Dict]) -> List[FMPAnalystEstimatesData]:
        """Return the transformed data."""

        return [FMPAnalystEstimatesData(**d) for d in data]
