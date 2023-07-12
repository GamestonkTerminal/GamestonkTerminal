"""FMP Cash Flow Statement Fetcher."""

# IMPORT STANDARD
from datetime import (
    date as dateType,
    datetime,
)
from typing import Dict, List, Literal, Optional

# IMPORT INTERNAL
from openbb_provider.model.abstract.data import Data, QueryParams
from openbb_provider.model.data.cash_flows import (
    CashFlowStatementData,
    CashFlowStatementQueryParams,
)
from openbb_provider.provider.abstract.fetcher import Fetcher
from openbb_provider.provider.provider_helpers import data_transformer

# IMPORT THIRD-PARTY
from pydantic import Field, NonNegativeInt, root_validator

from .helpers import create_url, get_data_many


class FMPCashFlowStatementQueryParams(QueryParams):
    """FMP Cash Flow Statement QueryParams.

    Source: https://financialmodelingprep.com/developer/docs/#Cash-Flow-Statement

    Parameter
    ---------
    symbol : Optional[str]
        The symbol of the company if cik is not provided.
    cik : Optional[str]
        The CIK of the company if symbol is not provided.
    period : Literal["annual", "quarter"]
        The period of the cash flow statement. Default is "annual".
    limit : Optional[NonNegativeInt]
        The limit of the cash flow statement.
    """

    symbol: Optional[str]
    cik: Optional[str]
    period: Literal["annual", "quarter"] = Field(default="annual")
    limit: Optional[NonNegativeInt]

    @root_validator()
    def check_symbol_or_cik(cls, values):  # pylint: disable=E0213
        if values.get("symbol") is None and values.get("cik") is None:
            raise ValueError("symbol or cik must be provided")
        return values


class FMPCashFlowStatementData(Data):
    date: dateType
    symbol: str
    cik: Optional[int]
    reportedCurrency: str = Field(alias="currency")
    fillingDate: Optional[dateType]
    acceptedDate: Optional[datetime]
    calendarYear: Optional[int]
    period: Optional[str]
    netIncome: Optional[int]
    depreciationAndAmortization: Optional[int]
    deferredIncomeTax: Optional[int]
    stockBasedCompensation: Optional[int]
    changeInWorkingCapital: Optional[int]
    accountsReceivables: Optional[int]
    inventory: Optional[int]
    accountsPayables: Optional[int]
    otherWorkingCapital: Optional[int]
    otherNonCashItems: Optional[int]
    netCashProvidedByOperatingActivities: Optional[int] = Field(
        alias="net_cash_flow_from_operating_activities"
    )
    investmentsInPropertyPlantAndEquipment: Optional[int]
    acquisitionsNet: Optional[int]
    purchasesOfInvestments: Optional[int]
    salesMaturitiesOfInvestments: Optional[int]
    otherInvestingActivites: Optional[int]
    netCashUsedForInvestingActivites: Optional[int] = Field(
        alias="net_cash_flow_from_investing_activities"
    )
    debtRepayment: Optional[int]
    commonStockIssued: Optional[int]
    commonStockRepurchased: Optional[int]
    dividendsPaid: Optional[int]
    otherFinancingActivites: Optional[int] = Field(alias="other_financing_activities")
    netCashUsedProvidedByFinancingActivities: Optional[int] = Field(
        alias="net_cash_flow_from_financing_activities"
    )
    effectOfForexChangesOnCash: Optional[int] = Field(alias="exchange_gain_losses")
    netChangeInCash: Optional[int] = Field(alias="net_cash_flow")
    cashAtEndOfPeriod: Optional[int]
    cashAtBeginningOfPeriod: Optional[int]
    operatingCashFlow: Optional[int]
    capitalExpenditure: Optional[int]
    freeCashFlow: Optional[int]
    link: Optional[str]
    finalLink: Optional[str]


class FMPCashFlowStatementFetcher(
    Fetcher[
        CashFlowStatementQueryParams,
        CashFlowStatementData,
        FMPCashFlowStatementQueryParams,
        FMPCashFlowStatementData,
    ]
):
    @staticmethod
    def transform_query(
        query: CashFlowStatementQueryParams, extra_params: Optional[Dict] = None
    ) -> FMPCashFlowStatementQueryParams:
        period = "annual" if query.period == "annually" else "quarter"
        return FMPCashFlowStatementQueryParams(
            symbol=query.symbol, period=period, **extra_params if extra_params else {}  # type: ignore
        )

    @staticmethod
    def extract_data(
        query: FMPCashFlowStatementQueryParams, api_key: str
    ) -> List[FMPCashFlowStatementData]:
        url = create_url(
            3, f"cash-flow-statement/{query.symbol}", api_key, query, ["symbol"]
        )
        return get_data_many(url, FMPCashFlowStatementData)

    @staticmethod
    def transform_data(
        data: List[FMPCashFlowStatementData],
    ) -> List[CashFlowStatementData]:
        return data_transformer(data, CashFlowStatementData)
