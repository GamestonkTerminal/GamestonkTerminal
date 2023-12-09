"""Intrinio Income Statement Model."""

from typing import Any, Dict, List, Literal, Optional

from openbb_core.provider.abstract.fetcher import Fetcher
from openbb_core.provider.standard_models.financial_statements import (
    FinancialStatementsQueryParams,
    IncomeStatementData,
)
from openbb_core.provider.utils.helpers import (
    ClientResponse,
    ClientSession,
    amake_requests,
)
from openbb_intrinio.utils.helpers import get_data_one
from pydantic import Field, field_validator


class IntrinioIncomeStatementQueryParams(FinancialStatementsQueryParams):
    """Intrinio Income Statement Query.

    Source: https://docs.intrinio.com/documentation/web_api/get_company_fundamentals_v2
    Source: https://docs.intrinio.com/documentation/web_api/get_fundamental_standardized_financials_v2
    """

    period: Literal["annual", "quarter", "ttm", "ytd"] = Field(default="annual")

    @field_validator("symbol", mode="after", check_fields=False)
    @classmethod
    def handle_symbol(cls, v) -> str:
        """Handle symbols with a dash and replace it with a dot for Intrinio."""
        return v.replace("-", ".")


class IntrinioIncomeStatementData(IncomeStatementData):
    """Intrinio Income Statement Data."""

    __alias_dict__ = {
        "amortization_expense": "amortizationexpense",
        "amortizationof_deferred_policy_acquisition_costs": "amortizationofdeferredpolicyacquisitioncosts",
        "basic_and_diluted_earnings_per_share": "basicdilutedeps",
        "basic_earnings_per_share": "basiceps",
        "capitalized_lease_obligations_interest_expense": "capitalizedleaseobligationinterestexpense",
        "cash_dividends_to_common_per_share": "cashdividendspershare",
        "current_and_future_benefits": "currentandfuturebenefits",
        "depletion_expense": "depletionexpense",
        "deposits_interest_expense": "depositsinterestexpense",
        "deposits_and_money_market_investments_interest_income": "depositsinterestincome",
        "depreciation_expense": "depreciationexpense",
        "diluted_earnings_per_share": "dilutedeps",
        "exploration_expense": "explorationexpense",
        "extraordinary_income": "extraordinaryincome",
        "federal_funds_purchased_and_securities_sold_interest_expense": "fedfundsandrepointerestexpense",
        "federal_funds_sold_and_securities_borrowed_interest_income": "fedfundsandrepointerestincome",
        "impairment_charge": "impairmentexpense",
        "income_tax_expense": "incometaxexpense",
        "pre_tax_income_margin": "pretaxincomemargin",
        "investment_banking_income": "investmentbankingincome",
        "investment_securities_interest_income": "investmentsecuritiesinterestincome",
        "loans_and_leases_interest_income": "loansandleaseinterestincome",
        "long_term_debt_interest_expense": "longtermdebtinterestexpense",
        "marketing_expense": "marketingexpense",
        "consolidated_net_income": "netincome",
        "net_income_continuing_operations": "netincomecontinuing",
        "net_income_discontinued_operations": "netincomediscontinued",
        "net_income_attributable_to_common_shareholders": "netincometocommon",
        "net_income_attributable_to_noncontrolling_interest": "netincometononcontrollinginterest",
        "net_interest_income": "netinterestincome",
        "net_occupancy_and_equipment_expense": "netoccupancyequipmentexpense",
        "net_realized_and_unrealized_capital_gains_on_investments": "netrealizedcapitalgains",
        "non_operating_income": "nonoperatingincome",
        "operating_revenue": "operatingrevenue",
        "operating_cost_of_revenue": "operatingcostofrevenue",
        "other_adjustments_to_consolidated_net_income": "otheradjustmentstoconsolidatednetincome",
        "other_adjustments_to_net_income_attributable_to_common_shareholders": "otheradjustmentstonetincometocommon",
        "other_adjustment_to_net_income_attributable_to_common_shareholders": "otheradjustmentstonetincometocommon",
        "other_cost_of_revenue": "othercostofrevenue",
        "other_gains": "othergains",
        "other_income": "otherincome",
        "other_interest_expense": "otherinterestexpense",
        "other_interest_income": "otherinterestincome",
        "other_non_interest_income": "othernoninterestincome",
        "other_operating_expenses": "otheroperatingexpenses",
        "other_revenue": "otherrevenue",
        "other_service_charges": "otherservicechargeincome",
        "other_special_charges": "otherspecialcharges",
        "insurance_policy_acquisition_costs": "policyacquisitioncosts",
        "preferred_stock_dividends_declared": "preferreddividends",
        "premiums_earned": "premiumsearned",
        "property_and_liability_insurance_claims": "propertyliabilityinsuranceclaims",
        "provision_for_credit_losses": "provisionforcreditlosses",
        "research_and_development_expense": "rdexpense",
        "restructuring_charge": "restructuringcharge",
        "salaries_and_employee_benefits": "salariesandemployeebenefitsexpense",
        "service_charges_on_deposit_accounts": "servicechargesondepositsincome",
        "selling_general_and_admin_expense": "sgaexpense",
        "short_term_borrowings_interest_expense": "shorttermborrowinginterestexpense",
        "cost_of_revenue": "totalcostofrevenue",
        "gross_profit": "totalgrossprofit",
        "gross_profit_ratio": "grossmargin",
        "total_interest_expense": "totalinterestexpense",
        "interest_and_investment_income": "totalinterestincome",
        "total_non_interest_expense": "totalnoninterestexpense",
        "total_non_interest_income": "totalnoninterestincome",
        "total_operating_expenses": "totaloperatingexpenses",
        "total_operating_income": "totaloperatingincome",
        "total_other_income": "totalotherincome",
        "total_pre_tax_income": "totalpretaxincome",
        "revenue": "totalrevenue",
        "trading_account_interest_income": "tradingaccountinterestincome",
        "trust_fees_by_commissions": "trustfeeincome",
        "ebit": "ebit",
        "ebitda": "ebitda",
        "ebitda_margin": "ebitdamargin",
        "weighted_average_basic_and_diluted_shares_outstanding": "weightedavebasicdilutedsharesos",
        "weighted_average_basic_shares_outstanding": "weightedavebasicsharesos",
        "weighted_average_diluted_shares_outstanding": "weightedavedilutedsharesos",
    }


class IntrinioIncomeStatementFetcher(
    Fetcher[
        IntrinioIncomeStatementQueryParams,
        List[IntrinioIncomeStatementData],
    ]
):
    """Transform the query, extract and transform the data from the Intrinio endpoints."""

    @staticmethod
    def transform_query(params: Dict[str, Any]) -> IntrinioIncomeStatementQueryParams:
        """Transform the query params."""
        return IntrinioIncomeStatementQueryParams(**params)

    @staticmethod
    async def aextract_data(
        query: IntrinioIncomeStatementQueryParams,
        credentials: Optional[Dict[str, str]],
        **kwargs: Any,
    ) -> List[Dict]:
        """Return the raw data from the Intrinio endpoint."""
        api_key = credentials.get("intrinio_api_key") if credentials else ""
        statement_code = "income_statement"
        if query.period in ["quarter", "annual"]:
            period_type = "FY" if query.period == "annual" else "QTR"
        if query.period in ["ttm", "ytd"]:
            period_type = query.period.upper()
        data_tags = [
            "ebit",
            "ebitda",
            "ebitdamargin",
            "pretaxincomemargin",
            "grossmargin",
        ]

        fundamentals_data: Dict = {}

        base_url = "https://api-v2.intrinio.com"

        fundamentals_url = (
            f"{base_url}/companies/{query.symbol}/fundamentals?"
            f"statement_code={statement_code}&type={period_type}&api_key={api_key}"
        )
        fundamentals_data = (await get_data_one(fundamentals_url, **kwargs)).get(
            "fundamentals", []
        )

        fiscal_periods = [
            f"{item['fiscal_year']}-{item['fiscal_period']}"
            for item in fundamentals_data
        ]
        fiscal_periods = fiscal_periods[: query.limit]

        async def callback(response: ClientResponse, session: ClientSession) -> Dict:
            """Return the response."""
            intrinio_id = response.url.parts[-2].replace(statement_code, "calculations")

            statement_data = await response.json()

            calculations_url = f"{base_url}/fundamentals/{intrinio_id}/standardized_financials?api_key={api_key}"
            calculations_data = await session.get_json(calculations_url)

            calculations_data = [
                item
                for item in calculations_data.get("standardized_financials", [])
                if item["data_tag"]["tag"] in data_tags
            ]

            return {
                "period_ending": statement_data["fundamental"]["end_date"],
                "fiscal_period": statement_data["fundamental"]["fiscal_period"],
                "fiscal_year": statement_data["fundamental"]["fiscal_year"],
                "financials": statement_data["standardized_financials"]
                + calculations_data,
            }

        intrinio_id = f"{query.symbol}-{statement_code}"
        urls = [
            f"{base_url}/fundamentals/{intrinio_id}-{period}/standardized_financials?api_key={api_key}"
            for period in fiscal_periods
        ]

        return await amake_requests(urls, callback, **kwargs)

    @staticmethod
    def transform_data(
        query: IntrinioIncomeStatementQueryParams, data: List[Dict], **kwargs: Any
    ) -> List[IntrinioIncomeStatementData]:
        """Return the transformed data."""
        transformed_data: List[IntrinioIncomeStatementData] = []

        for item in data:
            sub_dict: Dict[str, Any] = {}

            for sub_item in item["financials"]:
                field_name = sub_item["data_tag"]["tag"]
                sub_dict[field_name] = (
                    float(sub_item["value"])
                    if sub_item["value"] and sub_item["value"] != 0
                    else None
                )

            sub_dict["period_ending"] = item["period_ending"]
            sub_dict["fiscal_year"] = item["fiscal_year"]
            sub_dict["fiscal_period"] = item["fiscal_period"]

            transformed_data.append(IntrinioIncomeStatementData(**sub_dict))

        return transformed_data
