"""FMP Provider module."""


# IMPORT THIRD-PARTY

# IMPORT INTERNAL
from openbb_provider.abstract.provider import Provider

from openbb_fmp.models.analyst_estimates import FMPAnalystEstimatesFetcher
from openbb_fmp.models.available_indices import FMPAvailableIndicesFetcher
from openbb_fmp.models.balance_sheet import FMPBalanceSheetFetcher
from openbb_fmp.models.cash_flow import FMPCashFlowStatementFetcher
from openbb_fmp.models.company_profile import FMPCompanyProfileFetcher
from openbb_fmp.models.crypto_eod import FMPCryptoEODFetcher
from openbb_fmp.models.crypto_price import FMPCryptoPriceFetcher
from openbb_fmp.models.dividend_calendar import FMPDividendCalendarFetcher
from openbb_fmp.models.earnings_calendar import FMPEarningsCalendarFetcher
from openbb_fmp.models.earnings_call_transcript import FMPEarningsCallTranscriptFetcher
from openbb_fmp.models.esg_risk_rating import FMPESGRiskRatingFetcher
from openbb_fmp.models.esg_score import FMPESGScoreFetcher
from openbb_fmp.models.esg_sector import FMPESGSectorFetcher
from openbb_fmp.models.executive_compensation import FMPExecutiveCompensationFetcher
from openbb_fmp.models.executives import FMPKeyExecutivesFetcher
from openbb_fmp.models.forex_eod import FMPForexEODFetcher
from openbb_fmp.models.forex_pairs import FMPForexPairsFetcher
from openbb_fmp.models.forex_price import FMPForexPriceFetcher
from openbb_fmp.models.global_news import FMPGlobalNewsFetcher
from openbb_fmp.models.historical_dividends import FMPHistoricalDividendsFetcher
from openbb_fmp.models.historical_employees import FMPHistoricalEmployeesFetcher
from openbb_fmp.models.historical_stock_splits import FMPHistoricalStockSplitsFetcher
from openbb_fmp.models.income_statement import FMPIncomeStatementFetcher
from openbb_fmp.models.institutional_ownership import FMPInstitutionalOwnershipFetcher
from openbb_fmp.models.key_metrics import FMPKeyMetricsFetcher
from openbb_fmp.models.major_indices_constituents import (
    FMPMajorIndicesConstituentsFetcher,
)
from openbb_fmp.models.major_indices_eod import FMPMajorIndicesEODFetcher
from openbb_fmp.models.major_indices_price import FMPMajorIndicesPriceFetcher
from openbb_fmp.models.price_target import FMPPriceTargetFetcher
from openbb_fmp.models.price_target_consensus import FMPPriceTargetConsensusFetcher
from openbb_fmp.models.revenue_business_line import FMPRevenueBusinessLineFetcher
from openbb_fmp.models.revenue_geographic import FMPRevenueGeographicFetcher
from openbb_fmp.models.risk_premium import FMPRiskPremiumFetcher
from openbb_fmp.models.sec_filings import FMPSECFilingsFetcher
from openbb_fmp.models.share_statistics import FMPShareStatisticsFetcher
from openbb_fmp.models.stock_eod import FMPStockEODFetcher
from openbb_fmp.models.stock_insider_trading import FMPStockInsiderTradingFetcher
from openbb_fmp.models.stock_multiples import FMPStockMultiplesFetcher
from openbb_fmp.models.stock_news import FMPStockNewsFetcher
from openbb_fmp.models.stock_ownership import FMPStockOwnershipFetcher
from openbb_fmp.models.stock_peers import FMPStockPeersFetcher
from openbb_fmp.models.stock_price import FMPStockPriceFetcher
from openbb_fmp.models.stock_splits import FMPStockSplitCalendarFetcher
from openbb_fmp.models.treasury_rates import FMPTreasuryRatesFetcher

# mypy: disable-error-code="list-item"

fmp_provider = Provider(
    name="fmp",
    description="Provider for FMP.",
    required_credentials=["api_key"],
    fetcher_list=[
        FMPKeyExecutivesFetcher,
        FMPStockEODFetcher,
        FMPGlobalNewsFetcher,
        FMPStockNewsFetcher,
        FMPIncomeStatementFetcher,
        FMPBalanceSheetFetcher,
        FMPCashFlowStatementFetcher,
        FMPShareStatisticsFetcher,
        FMPMajorIndicesEODFetcher,
        FMPRevenueGeographicFetcher,
        FMPRevenueBusinessLineFetcher,
        FMPInstitutionalOwnershipFetcher,
        FMPCompanyProfileFetcher,
        FMPStockInsiderTradingFetcher,
        FMPStockOwnershipFetcher,
        FMPESGScoreFetcher,
        FMPESGSectorFetcher,
        FMPESGRiskRatingFetcher,
        FMPStockPriceFetcher,
        FMPPriceTargetConsensusFetcher,
        FMPPriceTargetFetcher,
        FMPAnalystEstimatesFetcher,
        FMPEarningsCalendarFetcher,
        FMPEarningsCallTranscriptFetcher,
        FMPHistoricalStockSplitsFetcher,
        FMPStockSplitCalendarFetcher,
        FMPHistoricalDividendsFetcher,
        FMPKeyMetricsFetcher,
        FMPSECFilingsFetcher,
        FMPTreasuryRatesFetcher,
        FMPExecutiveCompensationFetcher,
        FMPCryptoPriceFetcher,
        FMPCryptoEODFetcher,
        FMPMajorIndicesPriceFetcher,
        FMPForexEODFetcher,
        FMPForexPriceFetcher,
        FMPForexPairsFetcher,
        FMPStockPeersFetcher,
        FMPStockMultiplesFetcher,
        FMPHistoricalEmployeesFetcher,
        FMPAvailableIndicesFetcher,
        FMPRiskPremiumFetcher,
        FMPMajorIndicesConstituentsFetcher,
        FMPDividendCalendarFetcher,
    ],
)
