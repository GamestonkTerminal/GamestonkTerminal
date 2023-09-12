"""Income Statement Data Model."""


from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data, StrictInt
from openbb_provider.standard_models.base import (
    BaseSymbol,
    FinancialStatementQueryParams,
)


class IncomeStatementQueryParams(FinancialStatementQueryParams):
    """Income Statement Query."""


class IncomeStatementData(Data, BaseSymbol):
    """Income Statement Data."""

    date: dateType = Field(description="Date of the income statement.")
    period: Optional[str] = Field(
        default=None, description="Period of the income statement."
    )
    cik: Optional[str] = Field(default=None, description="Central Index Key.")

    revenue: Optional[StrictInt] = Field(default=None, description="Revenue.")
    cost_of_revenue: Optional[StrictInt] = Field(
        default=None, description="Cost of revenue."
    )
    gross_profit: Optional[StrictInt] = Field(default=None, description="Gross profit.")
    cost_and_expenses: Optional[StrictInt] = Field(
        default=None, description="Cost and expenses."
    )
    gross_profit_ratio: Optional[float] = Field(
        default=None, description="Gross profit ratio."
    )

    research_and_development_expenses: Optional[StrictInt] = Field(
        default=None, description="Research and development expenses."
    )
    general_and_administrative_expenses: Optional[StrictInt] = Field(
        default=None, description="General and administrative expenses."
    )
    selling_and_marketing_expenses: float = Field(
        default=None, description="Selling and marketing expenses."
    )
    selling_general_and_administrative_expenses: Optional[StrictInt] = Field(
        default=None, description="Selling, general and administrative expenses."
    )
    other_expenses: Optional[StrictInt] = Field(
        default=None, description="Other expenses."
    )
    operating_expenses: Optional[StrictInt] = Field(
        default=None, description="Operating expenses."
    )

    depreciation_and_amortization: Optional[StrictInt] = Field(
        default=None, description="Depreciation and amortization."
    )
    ebitda: Optional[StrictInt] = Field(
        default=None,
        description="Earnings before interest, taxes, depreciation and amortization.",
    )
    ebitda_ratio: Optional[float] = Field(
        default=None,
        description="Earnings before interest, taxes, depreciation and amortization ratio.",
    )
    operating_income: Optional[StrictInt] = Field(
        default=None, description="Operating income."
    )
    operating_income_ratio: Optional[float] = Field(
        default=None, description="Operating income ratio."
    )

    interest_income: Optional[StrictInt] = Field(
        default=None, description="Interest income."
    )
    interest_expense: Optional[StrictInt] = Field(
        default=None, description="Interest expense."
    )
    total_other_income_expenses_net: Optional[StrictInt] = Field(
        default=None, description="Total other income expenses net."
    )

    income_before_tax: Optional[StrictInt] = Field(
        default=None, description="Income before tax."
    )
    income_before_tax_ratio: Optional[float] = Field(
        default=None, description="Income before tax ratio."
    )
    income_tax_expense: Optional[StrictInt] = Field(
        default=None, description="Income tax expense."
    )

    net_income: Optional[StrictInt] = Field(default=None, description="Net income.")
    net_income_ratio: Optional[float] = Field(
        default=None, description="Net income ratio."
    )
    eps: Optional[float] = Field(default=None, description="Earnings per share.")
    eps_diluted: Optional[float] = Field(
        default=None, description="Earnings per share diluted."
    )
    weighted_average_shares_outstanding: Optional[StrictInt] = Field(
        default=None, description="Weighted average shares outstanding."
    )
    weighted_average_shares_outstanding_dil: Optional[StrictInt] = Field(
        default=None, description="Weighted average shares outstanding diluted."
    )
    link: Optional[str] = Field(
        default=None, description="Link to the income statement."
    )
    final_link: Optional[str] = Field(
        default=None, description="Final link to the income statement."
    )
