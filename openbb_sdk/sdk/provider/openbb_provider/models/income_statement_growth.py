"""Income Statement Growth Data Model."""


from datetime import date as dateType
from typing import Literal

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.abstract.query_params import QueryParams
from openbb_provider.metadata import DATA_DESCRIPTIONS, QUERY_DESCRIPTIONS
from openbb_provider.models.base import BaseSymbol


class IncomeStatementGrowthQueryParams(QueryParams, BaseSymbol):
    """Income Statement Growth Query."""

    limit: int = Field(default=10, description=QUERY_DESCRIPTIONS.get("limit", ""))
    period: Literal["annually", "quarterly"] = Field(
        default="annually", description=QUERY_DESCRIPTIONS.get("period", "")
    )


class IncomeStatementGrowthData(Data, BaseSymbol):
    """Income Statement Growth Data."""

    date: dateType = Field(description=DATA_DESCRIPTIONS.get("date", ""))
    period: str = Field(description="The period the statement is returned for.")
    growth_revenue: float = Field(description="Growth rate of total revenue.")
    growth_cost_of_revenue: float = Field(
        description="Growth rate of cost of goods sold."
    )
    growth_gross_profit: float = Field(description="Growth rate of gross profit.")
    growth_gross_profit_ratio: float = Field(
        description="Growth rate of gross profit as a percentage of revenue."
    )
    growth_research_and_development_expenses: float = Field(
        description="Growth rate of expenses on research and development."
    )
    growth_general_and_administrative_expenses: float = Field(
        description="Growth rate of general and administrative expenses."
    )
    growth_selling_and_marketing_expenses: float = Field(
        description="Growth rate of expenses on selling and marketing activities."
    )
    growth_other_expenses: float = Field(
        description="Growth rate of other operating expenses."
    )
    growth_operating_expenses: float = Field(
        description="Growth rate of total operating expenses."
    )
    growth_cost_and_expenses: float = Field(
        description="Growth rate of total costs and expenses."
    )
    growth_interest_expense: float = Field(
        description="Growth rate of interest expenses."
    )
    growth_depreciation_and_amortization: float = Field(
        description="Growth rate of depreciation and amortization expenses."
    )
    growth_ebitda: float = Field(
        description="Growth rate of Earnings Before Interest, Taxes, Depreciation, and Amortization."
    )
    growth_ebitda_ratio: float = Field(
        description="Growth rate of EBITDA as a percentage of revenue."
    )
    growth_operating_income: float = Field(
        description="Growth rate of operating income."
    )
    growth_operating_income_ratio: float = Field(
        description="Growth rate of operating income as a percentage of revenue."
    )
    growth_total_other_income_expenses_net: float = Field(
        description="Growth rate of net total other income and expenses."
    )
    growth_income_before_tax: float = Field(
        description="Growth rate of income before taxes."
    )
    growth_income_before_tax_ratio: float = Field(
        description="Growth rate of income before taxes as a percentage of revenue."
    )
    growth_income_tax_expense: float = Field(
        description="Growth rate of income tax expenses."
    )
    growth_net_income: float = Field(description="Growth rate of net income.")
    growth_net_income_ratio: float = Field(
        description="Growth rate of net income as a percentage of revenue."
    )
    growth_eps: float = Field(description="Growth rate of Earnings Per Share (EPS).")
    growth_eps_diluted: float = Field(
        description="Growth rate of diluted Earnings Per Share (EPS)."
    )
    growth_weighted_average_shs_out: float = Field(
        description="Growth rate of weighted average shares outstanding."
    )
    growth_weighted_average_shs_out_dil: float = Field(
        description="Growth rate of diluted weighted average shares outstanding."
    )
