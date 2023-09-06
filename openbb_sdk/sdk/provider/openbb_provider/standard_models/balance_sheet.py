"""Balance Sheet Data Model."""


from datetime import date as dateType
from typing import Optional

from pydantic import Field

from openbb_provider.abstract.data import Data
from openbb_provider.standard_models.base import (
    BaseSymbol,
    FinancialStatementQueryParams,
)


class BalanceSheetQueryParams(FinancialStatementQueryParams):
    """Balance Sheet query."""


class BalanceSheetData(Data, BaseSymbol):
    """Balance Sheet Data."""

    date: dateType = Field(description="Date of the fetched statement.")
    period: Optional[str] = Field(description="Reporting period of the statement.")
    cik: Optional[int] = Field(description="Central Index Key (CIK) of the company.")

    cash_and_cash_equivalents: Optional[int] = Field(
        description="Cash and cash equivalents"
    )
    short_term_investments: Optional[int] = Field(description="Short-term investments")
    net_receivables: Optional[int] = Field(description="Receivables, net")
    inventory: Optional[int] = Field(description="Inventory")
    other_current_assets: Optional[int] = Field(description="Other current assets")
    total_current_assets: Optional[int] = Field(description="Total current assets")

    marketable_securities: Optional[int] = Field(description="Marketable securities")
    property_plant_equipment_net: Optional[int] = Field(
        description="Property, plant and equipment, net"
    )
    goodwill: Optional[int] = Field(description="Goodwill")

    assets: Optional[int] = Field(description="Total assets")
    current_assets: Optional[int] = Field(description="Total current assets")
    other_current_assets: Optional[int] = Field(description="Other current assets")
    intangible_assets: Optional[int] = Field(description="Intangible assets")
    tax_assets: Optional[int] = Field(description="Accrued income taxes")
    other_non_current_assets: Optional[int] = Field(
        description="Other non-current assets"
    )
    total_non_current_assets: Optional[int] = Field(
        description="Total non-current assets"
    )
    other_assets: Optional[int] = Field(description="Other assets")
    total_assets: Optional[int] = Field(description="Total assets")

    account_payables: Optional[int] = Field(description="Accounts payables")
    short_term_debt: Optional[int] = Field(
        description="Short-term borrowings, Long-term debt due within one year, "
        "Operating lease obligations due within one year, "
        "Finance lease obligations due within one year"
    )
    tax_payables: Optional[int] = Field(description="Accrued income taxes")
    deferred_revenue: Optional[int] = Field(
        description="Accrued income taxes, other deferred revenue"
    )
    other_current_liabilities: Optional[int] = Field(
        description="Other current liabilities"
    )
    total_current_liabilities: Optional[int] = Field(
        description="Total current liabilities"
    )

    long_term_debt: Optional[int] = Field(
        description="Long-term debt, Operating lease obligations, "
        "Long-term finance lease obligations"
    )
    deferred_revenue_non_current: Optional[int] = Field(
        description="Deferred revenue, non-current"
    )
    deferred_tax_liabilities_non_current: Optional[int] = Field(
        description="Deferred income taxes and other"
    )
    current_liabilities: Optional[int] = Field(description="Total current liabilities")
    total_liabilities_and_total_equity: Optional[int] = Field(
        description="Total liabilities and total equity"
    )
    other_liabilities: Optional[int] = Field(description="Other liabilities")
    other_non_current_liabilities: Optional[int] = Field(
        description="Other non-current liabilities"
    )
    non_current_liabilities: Optional[int] = Field(
        description="Total non-current liabilities"
    )
    total_liabilities_and_stockholders_equity: Optional[int] = Field(
        description="Total liabilities and stockholders' equity"
    )
    total_non_current_liabilities: Optional[int] = Field(
        description="Total non-current liabilities"
    )
    other_liabilities: Optional[int] = Field(description="Other liabilities")
    total_liabilities: Optional[int] = Field(description="Total liabilities")

    preferred_stock: Optional[int] = Field(description="Preferred stock")
    common_stock: Optional[int] = Field(description="Common stock")
    retained_earnings: Optional[int] = Field(description="Retained earnings")
    accumulated_other_comprehensive_income_loss: Optional[int] = Field(
        description="Accumulated other comprehensive income (loss)"
    )
    other_shareholder_equity: Optional[int] = Field(
        description="Other shareholder's equity"
    )
    total_shareholder_equity: Optional[int] = Field(
        description="Total shareholder's equity"
    )

    total_equity: Optional[int] = Field(description="Total equity")
    total_liabilities_and_shareholders_equity: Optional[int] = Field(
        description="Total liabilities and shareholder's equity"
    )
    minority_interest: Optional[int] = Field(description="Minority interest")
    total_liabilities_and_total_equity: Optional[int] = Field(
        description="Total liabilities and total equity"
    )
