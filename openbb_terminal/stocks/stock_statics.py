INTERVALS = [1, 5, 15, 30, 60]
SOURCES = ["YahooFinance", "AlphaVantage", "EODHD"]
CANDLE_SORT = [
    "open",
    "high",
    "low",
    "close",
    "adjclose",
    "volume",
    "dividends",
    "stock_splits",
]

market_coverage_suffix = {
    "united_states": ["CBT", "CME", "NYB", "CMX", "NYM", "US", ""],
    "argentina": ["BA"],
    "austria": ["VI"],
    "australia": ["AX"],
    "belgium": ["BR"],
    "brazil": ["SA"],
    "canada": ["CN", "NE", "TO", "V"],
    "chile": ["SN"],
    "china": ["SS", "SZ"],
    "czech_republic": ["PR"],
    "denmark": ["CO"],
    "egypt": ["CA"],
    "estonia": ["TL"],
    "europe": ["NX"],
    "finland": ["HE"],
    "france": ["PA"],
    "germany": ["BE", "BM", "DU", "F", "HM", "HA", "MU", "SG", "DE"],
    "greece": ["AT"],
    "hong_kong": ["HK"],
    "hungary": ["BD"],
    "iceland": ["IC"],
    "india": ["BO", "NS"],
    "indonesia": ["JK"],
    "ireland": ["IR"],
    "israel": ["TA"],
    "italy": ["MI"],
    "japan": ["T", "S"],
    "latvia": ["RG"],
    "lithuania": ["VS"],
    "malaysia": ["KL"],
    "mexico": ["MX"],
    "netherlands": ["AS"],
    "new_zealand": ["NZ"],
    "norway": ["OL"],
    "portugal": ["LS"],
    "qatar": ["QA"],
    "russia": ["ME"],
    "singapore": ["SI"],
    "south_africa": ["JO"],
    "south_korea": ["KS", "KQ"],
    "spain": ["MC"],
    "saudi_arabia": ["SAU"],
    "sweden": ["ST"],
    "switzerland": ["SW"],
    "taiwan": ["TWO", "TW"],
    "thailand": ["BK"],
    "turkey": ["IS"],
    "united_kingdom": ["L", "IL"],
    "venezuela": ["CR"],
}

INCOME_PLOT = {
    "AlphaVantage": {
        "reportedcurrency": "reported_currency",
        "grossprofit": "gross_profit",
        "totalrevenue": "total_revenue",
        "costofrevenue": "cost_of_revenue",
        "costofgoodsandservicessold": "cost_of_goods_and_services_sold",
        "operatingincome": "operating_income",
        "sellinggeneralandadministrative": "selling_general_and_administrative",
        "researchanddevelopment": "research_and_development_expenses",
        "operatingexpenses": "operating_expenses",
        "investmentincomenet": "investment_income_net",
        "netinterestincome": "net_interest_income",
        "interestincome": "interest_income",
        "interestexpense": "interest_expense",
        "noninterestincome": "revenue",
        "othernonoperatingincome": "other_non_operating_income",
        "depreciation": "depreciation",
        "depreciationandamortization": "depreciation_and_amortization",
        "incomebeforetax": "income_before_tax",
        "incometaxexpense": "income_tax_expense",
        "interestanddebtexpense": "interest_and_debt_expense",
        "netincomefromcontinuingoperations": "net_income_from_continuing_operations",
        "comprehensiveincomenetoftax": "comprehensive_income_net_of_tax",
        "ebit": "ebit",
        "ebitda": "ebitda",
        "netincome": "net_income",
    },
    "Polygon": {
        "cost_of_revenue": "cost_of_revenue",
        "diluted_earnings_per_share": "diluted_earnings_per_share",
        "costs_and_expenses": "costs_and_expenses",
        "gross_profit": "gross_profit",
        "nonoperating_income_loss": "non_operating_income_loss",
        "operating_income_loss": "operating_income",
        "participating_securities_distributed_and_undistributed_earnings_loss_basic": "participating_securities_"
        "distributed_and_undistributed_ea"
        "rnings_loss_basic",
        "income_tax_expense_benefit": "income_tax_expense",
        "income_tax_expense_benefit_current": "current_income_tax_expense",
        "net_income_loss_attributable_to_parent": "net_income_loss_attributable_to_parent",
        "net_income_loss": "net_income",
        "income_tax_expense_benefit_deferred": "income_tax_expense_benefit_deferred",
        "preferred_stock_dividends_and_other_adjustments": "preferred_stock_dividends_and_other_adjustments",
        "operating_expenses": "operating_expenses",
        "income_loss_from_continuing_operations_before_tax": "continuing_operations_net_income",
        "net_income_loss_attributable_to_noncontrolling_interest": "net_income_loss_attributable_to_"
        "non_controlling_interest",
        "income_loss_from_continuing_operations_after_tax": "income_before_tax",
        "revenues": "revenue",
        "net_income_loss_available_to_common_stockholders_basic": "net_income_available_to_common_shareholders",
        "benefits_costs_expenses": "benefits_costs_expenses",
        "basic_earnings_per_share": "basic_earnings_per_share",
        "interest_expense_operating": "income_tax_expense",
        "income_loss_before_equity_method_investments": "income_loss_before_equity_method_investments",
        "cost_of_revenue_goods": "cost_of_revenue_goods",
    },
    "YahooFinance": {
        "total_revenue": "total_revenue",
        "cost_of_revenue": "cost_of_revenue",
        "gross_profit": "gross_profit",
        "research_development": "research_and_development_expenses",
        "selling_general_and_administrative": "selling_general_and_administrative",
        "total_operating_expenses": "operating_expenses",
        "operating_income_or_loss": "operating_income",
        "interest_expense": "interest_expense",
        "total_other_income/expenses_net": "other_non_operating_income",
        "income_before_tax": "income_before_tax",
        "income_tax_expense": "income_tax_expense",
        "income_from_continuing_operations": "net_income_from_continuing_operations",
        "net_income": "net_income",
        "net_income_available_to_common_shareholders": "net_income_available_to_common_shareholders",
        "basic_eps": "basic_earnings_per_share",
        "diluted_eps": "diluted_earnings_per_share",
        "basic_average_shares": "basic_average_shares",
        "diluted_average_shares": "diluted_average_shares",
        "ebitda": "ebitda",
    },
    "FinancialModelingPrep": {
        "reported_currency": "reported_currency",
        "cik": "cik",
        "filling_date": "filling_date",
        "accepted_date": "accepted_date",
        "calendar_year": "calendar_year",
        "period": "period",
        "revenue": "revenue",
        "cost_of_revenue": "cost_of_revenue",
        "gross_profit": "gross_profit",
        "gross_profit_ratio": "gross_profit_ratio",
        "research_and_development_expenses": "research_and_development_expenses",
        "general_and_administrative_expenses": "general_and_administrative_expenses",
        "selling_and_marketing_expenses": "selling_and_marketing_expenses",
        "selling_general_and_administrative_expenses": "selling_general_and_administrative",
        "other_expenses": "other_expenses",
        "operating_expenses": "operating_expenses",
        "cost_and_expenses": "costs_and_expenses",
        "interest_income": "interest_income",
        "interest_expense": "interest_expense",
        "depreciation_and_amortization": "depreciation_and_amortization",
        "ebitda": "ebitda",
        "ebitdaratio": "ebitda_ratio",
        "operating_income": "operating_income",
        "operating_income_ratio": "operating_income_ratio",
        "total_other_income_expenses_net": "non_operating_income_loss",
        "income_before_tax": "income_before_tax",
        "income_before_tax_ratio": "income_before_tax_ratio",
        "income_tax_expense": "income_tax_expense",
        "net_income": "net_income",
        "net_income_ratio": "net_income_ratio",
        "eps": "basic_earnings_per_share",
        "epsdiluted": "diluted_earnings_per_share",
        "weighted_average_shs_out": "basic_average_shares",
        "weighted_average_shs_out_dil": "diluted_average_shares",
        "link": "link",
        "final_link": "final_link",
    },
}
INCOME_PLOT_CHOICES = [
    "gross_profit",
    "total_revenue",
    "cost_of_revenue",
    "cost_of_goods_and_services_sold",
    "operating_income",
    "selling_general_and_administrative",
    "research_and_development_expenses",
    "operating_expenses",
    "investment_income_net",
    "net_interest_income",
    "interest_income",
    "interest_expense",
    "revenue",
    "other_non_operating_income",
    "depreciation",
    "depreciation_and_amortization",
    "income_before_tax",
    "income_tax_expense",
    "interest_and_debt_expense",
    "net_income_from_continuing_operations",
    "comprehensive_income_net_of_tax",
    "ebit",
    "ebitda",
    "net_income",
    "diluted_earnings_per_share",
    "costs_and_expenses",
    "non_operating_income_loss",
    "participating_securities_distributed_and_undistributed_earnings_loss_basic",
    "net_income_loss_attributable_to_parent",
    "income_tax_expense_benefit_deferred",
    "preferred_stock_dividends_and_other_adjustments",
    "net_income_loss_attributable_to_non_controlling_interest",
    "continuing_operations_net_income",
    "income_before_tax",
    "net_income_available_to_common_shareholders",
    "benefits_costs_expenses",
    "basic_earnings_per_share",
    "income_loss_before_equity_method_investments",
    "basic_average_shares",
    "diluted_average_shares",
    "gross_profit_ratio",
    "general_and_administrative_expenses",
    "selling_and_marketing_expenses",
    "other_expenses",
    "ebitda_ratio",
    "operating_income_ratio",
    "income_before_tax_ratio",
    "net_income_ratio",
    "current_income_tax_expense",
]
BALANCE_PLOT = {
    "AlphaVantage": {
        "reportedcurrency": "reported_currency",
        "totalassets": "total_assets",
        "totalcurrentassets": "total_current_assets",
        "cashandcashequivalentsatcarryingvalue": "cash_and_cash_equivalents",
        "cashandshortterminvestments": "cash_and_short_term_investments",
        "inventory": "inventory",
        "currentnetreceivables": "net_receivables",
        "totalnoncurrentassets": "total_non_current_assets",
        "propertyplantequipment": "property_plant_equipment",
        "accumulateddepreciationamortizationppe": "accumulated_depreciation_amortization_ppe",
        "intangibleassets": "intangible_assets",
        "intangibleassetsexcludinggoodwill": "intangible_assets_excluding_goodwill",
        "goodwill": "goodwill",
        "investments": "investments",
        "longterminvestments": "long_term_investments",
        "shortterminvestments": "short_term_investments",
        "othercurrentassets": "other_current_assets",
        "othernoncurrentassets": "other_non_current_assets",
        "totalliabilities": "total_liabilities",
        "totalcurrentliabilities": "total_current_liabilities",
        "currentaccountspayable": "current_accounts_payable",
        "deferredrevenue": "deferred_revenue",
        "currentdebt": "current_debt",
        "shorttermdebt": "short_term_debt",
        "totalnoncurrentliabilities": "total_non_current_liabilities",
        "capitalleaseobligations": "capital_lease_obligations",
        "longtermdebt": "long_term_debt",
        "currentlongtermdebt": "current_long_term_debt",
        "longtermdebtnoncurrent": "long_term_debt_non_current",
        "shortlongtermdebttotal": "short_long_term_debt_total",
        "othercurrentliabilities": "other_current_liabilities",
        "othernoncurrentliabilities": "other_non_current_liabilities",
        "totalshareholderequity": "total_shareholder_equity",
        "treasurystock": "treasury_stock",
        "retainedearnings": "retained_earnings",
        "commonstock": "common_stock",
        "commonstocksharesoutstanding": "common_stock_shares_outstanding",
    },
    "Polygon": {
        "equity_attributable_to_noncontrolling_interest": "equity_attributable_to_non_controlling_interest",
        "liabilities": "total_liabilities",
        "noncurrent_assets": "total_non_current_assets",
        "equity": "equity",
        "assets": "total_assets",
        "current_assets": "total_current_assets",
        "equity_attributable_to_parent": "equity_attributable_to_parent",
        "current_liabilities": "total_current_liabilities",
        "noncurrent_liabilities": "total_non_current_liabilities",
        "fixed_assets": "fixed_assets",
        "other_than_fixed_noncurrent_assets": "other_than_fixed_non_current_assets",
        "liabilities_and_equity": "liabilities_and_equity",
    },
    "YahooFinance": {
        "cash_and_cash_equivalents": "cash_and_cash_equivalents",
        "other_short-term_investments": "short_term_investments",
        "total_cash": "cash_and_short_term_investments",
        "net_receivables": "net_receivables",
        "inventory": "inventory",
        "other_current_assets": "other_current_assets",
        "total_current_assets": "total_current_assets",
        "gross_property, plant_and_equipment": "gross_property, plant_and_equipment",
        "accumulated_depreciation": "accumulated_depreciation_amortization_ppe",
        "net_property, plant_and_equipment": "property_plant_equipment",
        "equity_and_other_investments": "long_term_investments",
        "other_long-term_assets": "other_non_currrent_assets",
        "total_non-current_assets": "total_non_current_assets",
        "total_assets": "total_assets",
        "current_debt": "current_debt",
        "accounts_payable": "current_accounts_payable",
        "deferred_revenues": "deferred_revenue",
        "other_current_liabilities": "other_current_liabilities",
        "total_current_liabilities": "total_current_liabilities",
        "long-term_debt": "long_term_debt",
        "deferred_tax_liabilities": "deferred_tax_liabilities",
        "other_long-term_liabilities": "other_non_current_liabilities",
        "total_non-current_liabilities": "total_non_current_liabilities",
        "total_liabilities": "total_liabilities",
        "common_stock": "common_stock",
        "retained_earnings": "retained_earnings",
        "accumulated_other_comprehensive_income": "accumulated_other_comprehensive_income",
        "total_stockholders'_equity": "total_shareholder_equity",
        "total_liabilities_and_stockholders'_equity": "total_liabilities_and_stockholders_equity",
    },
    "FinancialModelingPrep": {
        "reported_currency": "reported_currency",
        "cik": "cik",
        "filling_date": "filing_date",
        "accepted_date": "accepted_date",
        "calendar_year": "calendar_year",
        "period": "period",
        "cash_and_cash_equivalents": "cash_and_cash_equivalents",
        "short_term_investments": "short_term_investments",
        "cash_and_short_term_investments": "cash_and_short_term_investments",
        "net_receivables": "net_receivables",
        "inventory": "inventory",
        "other_current_assets": "other_current_assets",
        "total_current_assets": "total_current_assets",
        "property_plant_equipment_net": "property_plant_equipment",
        "goodwill": "goodwill",
        "intangible_assets": "intangible_assets_excluding_goodwill",
        "goodwill_and_intangible_assets": "intangible_assets",
        "long_term_investments": "long_term_investments",
        "tax_assets": "tax_assets",
        "other_non_current_assets": "other_non_currrent_assets",
        "total_non_current_assets": "total_non_current_assets",
        "other_assets": "other_assets",
        "total_assets": "total_assets",
        "account_payables": "current_accounts_payable",
        "short_term_debt": "current_debt",
        "tax_payables": "tax_payables",
        "deferred_revenue": "deferred_revenue",
        "other_current_liabilities": "other_non_current_liabilities",
        "total_current_liabilities": "total_current_liabilities",
        "long_term_debt": "long_term_debt_non_current",
        "deferred_revenue_non_current": "deferred_revenue_non_current",
        "deferred_tax_liabilities_non_current": "deferred_tax_liabilities",
        "other_non_current_liabilities": "other_non_current_liabilities",
        "total_non_current_liabilities": "total_non_current_liabilities",
        "other_liabilities": "other_liabilities",
        "capital_lease_obligations": "capital_lease_obligations",
        "total_liabilities": "total_liabilities",
        "preferred_stock": "preferred_stock",
        "common_stock": "common_stock",
        "retained_earnings": "retained_earnings",
        "accumulated_other_comprehensive_income_loss": "accumulated_other_comprehensive_income",
        "othertotal_stockholders_equity": "other_total_stockholders_equity",
        "total_stockholders_equity": "total_shareholder_equity",
        "total_liabilities_and_stockholders_equity": "total_liabilities_and_stockholders_equity",
        "minority_interest": "equity_attributable_to_non_controlling_interest",
        "total_equity": "equity",
        "total_liabilities_and_total_equity": "liabilities_and_equity",
        "total_investments": "total_investments",
        "total_debt": "total_debt",
        "net_debt": "net_debt",
        "link": "link",
        "final_link": "final_link",
    },
}
BALANCE_PLOT_CHOICES = [
    "total_assets",
    "total_current_assets",
    "cash_and_cash_equivalents",
    "cash_and_short_term_investments",
    "inventory",
    "net_receivables",
    "total_non_current_assets",
    "property_plant_equipment",
    "accumulated_depreciation_amortization_ppe",
    "intangible_assets",
    "intangible_assets_excluding_goodwill",
    "goodwill",
    "investments",
    "long_term_investments",
    "short_term_investments",
    "other_current_assets",
    "other_non_currrent_assets",
    "total_liabilities",
    "total_current_liabilities",
    "current_accounts_payable",
    "deferred_revenue",
    "current_debt",
    "short_term_debt",
    "total_non_current_liabilities",
    "capital_lease_obligations",
    "long_term_debt",
    "current_long_term_debt",
    "long_term_debt_non_current",
    "short_long_term_debt_total",
    "other_current_liabilities",
    "other_non_current_liabilities",
    "total_shareholder_equity",
    "treasury_stock",
    "retained_earnings",
    "common_stock",
    "common_stock_shares_outstanding",
    "equity_attributable_to_non_controlling_interest",
    "equity_attributable_to_parent",
    "fixed_assets",
    "other_than_fixed_non_current_assets",
    "liabilities_and_equity",
    "equity",
    "gross_property,",
    "plant_and_equipment",
    "tax_payables",
    "other_assets",
    "tax_assets",
    "deferred_revenue_non_current",
    "deferred_tax_liabilities",
    "other_liabilities",
    "preferred_stock",
    "accumulated_other_comprehensive_income",
    "other_total_stockholders_equity",
    "total_liabilities_and_stockholders_equity",
    "total_investments",
    "total_debt",
    "net_debt",
]
CASH_PLOT = {
    "AlphaVantage": {
        "reportedcurrency": "reported_currency",
        "operatingcashflow": "operating_cash_flow",
        "paymentsforoperatingactivities": "payments_for_operating_activities",
        "proceedsfromoperatingactivities": "proceeds_from_operating_activities",
        "changeinoperatingliabilities": "change_in_operating_liabilities",
        "changeinoperatingassets": "change_in_operating_assets",
        "depreciationdepletionandamortization": "depreciation_depletion_and_amortization",
        "capitalexpenditures": "capital_expenditure",
        "changeinreceivables": "change_in_receivables",
        "changeininventory": "inventory",
        "profitloss": "profit_loss",
        "cashflowfrominvestment": "cash_flow_from_investment",
        "cashflowfromfinancing": "cash_flow_from_financing",
        "proceedsfromrepaymentsofshorttermdebt": "proceeds_from_repayments_of_short_term_debt",
        "paymentsforrepurchaseofcommonstock": "common_stock_repurchased",
        "paymentsforrepurchaseofequity": "payments_for_repurchase_of_equity",
        "paymentsforrepurchaseofpreferredstock": "payments_for_repurchase_of_preferred_stock",
        "dividendpayout": "dividends_paid",
        "dividendpayoutcommonstock": "dividend_payout_common_stock",
        "dividendpayoutpreferredstock": "dividend_payout_preferred_stock",
        "proceedsfromissuanceofcommonstock": "common_stock_issued",
        "proceedsfromissuanceoflongtermdebtandcapitalsecuritiesnet": "proceeds_from_issuance_of_long_term_",
        "proceedsfromissuanceofpreferredstock": "proceeds_from_issuance_of_preferred_stock",
        "proceedsfromrepurchaseofequity": "proceeds_from_repurchase_of_equity",
        "proceedsfromsaleoftreasurystock": "proceeds_from_sale_of_treasury_stock",
        "changeincashandcashequivalents": "net_change_in_cash",
        "changeinexchangerate": "change_in_exchange_rate",
        "netincome": "net_income",
    },
    "Polygon": {
        "net_cash_flow_from_financing_activities_continuing": "net_cash_flow_from_financing_activities_continuing",
        "net_cash_flow_continuing": "net_cash_flow_continuing",
        "net_cash_flow_from_investing_activities": "cash_flow_from_investment",
        "net_cash_flow": "net_change_in_cash",
        "net_cash_flow_from_operating_activities": "operating_cash_flow",
        "net_cash_flow_from_financing_activities": "cash_flow_from_financing",
        "net_cash_flow_from_operating_activities_continuing": "net_cash_provided_by_operating_activities",
        "net_cash_flow_from_investing_activities_continuing": "net_cash_flow_from_investing_activities_continuing",
        "exchange_gains_losses": "change_in_exchange_rate",
    },
    "YahooFinance": {
        "net_income": "net_income",
        "depreciation_&_amortisation": "depreciation_and_amortization",
        "deferred_income_taxes": "deferred_income_taxes",
        "stock-based_compensation": "stock_based_compensation",
        "change_in_working_capital": "change_in_working_capital",
        "accounts_receivable": "change_in_receivables",
        "inventory": "inventory",
        "accounts_payable": "accounts_payable",
        "other_working_capital": "other_working_capital",
        "other_non-cash_items": "other_non_cash_items",
        "net_cash_provided_by_operating_activities": "net_cash_provided_by_operating_activities",
        "investments_in_property, plant_and_equipment": "investments_in_property_plant_and_equipment",
        "acquisitions, net": "acquisitions_net",
        "purchases_of_investments": "purchases_of_investments",
        "sales/maturities_of_investments": "sales_maturities_of_investments",
        "other_investing_activities": "other_investing_activities",
        "net_cash_used_for_investing_activities": "cash_flow_from_investment",
        "debt_repayment": "debt_repayment",
        "common_stock_issued": "common_stock_issued",
        "common_stock_repurchased": "common_stock_repurchased",
        "dividends_paid": "dividends_paid",
        "other_financing_activities": "other_financing_activities",
        "net_cash_used_provided_by_(used_for)_financing_activities": "cash_flow_from_financing",
        "net_change_in_cash": "net_change_in_cash",
        "cash_at_beginning_of_period": "cash_at_beginning_of_period",
        "cash_at_end_of_period": "cash_at_end_of_period",
        "operating_cash_flow": "operating_cash_flow",
        "capital_expenditure": "capital_expenditure",
        "free_cash_flow": "free_cash_flow",
    },
    "FinancialModelingPrep": {
        "reported_currency": "reported_currency",
        "cik": "cik",
        "filling_date": "filling_date",
        "accepted_date": "accepted_date",
        "calendar_year": "calendar_year",
        "period": "period",
        "net_income": "net_income",
        "depreciation_and_amortization": "depreciation_and_amortization",
        "deferred_income_tax": "deferred_income_taxes",
        "stock_based_compensation": "stock_based_compensation",
        "change_in_working_capital": "change_in_working_capital",
        "accounts_receivables": "change_in_receivables",
        "inventory": "inventory",
        "accounts_payables": "accounts_payable",
        "other_working_capital": "other_working_capital",
        "other_non_cash_items": "other_non_cash_items",
        "net_cash_provided_by_operating_activities": "net_cash_provided_by_operating_activities",
        "investments_in_property_plant_and_equipment": "investments_in_property_plant_and_equipment",
        "acquisitions_net": "acquisitions_net",
        "purchases_of_investments": "purchases_of_investments",
        "sales_maturities_of_investments": "sales_maturities_of_investments",
        "other_investing_activites": "other_investing_activities",
        "net_cash_used_for_investing_activites": "cash_flow_from_investment",
        "debt_repayment": "debt_repayment",
        "common_stock_issued": "common_stock_issued",
        "common_stock_repurchased": "common_stock_repurchased",
        "dividends_paid": "dividends_paid",
        "other_financing_activites": "other_financing_activities",
        "net_cash_used_provided_by_financing_activities": "cash_flow_from_financing",
        "effect_of_forex_changes_on_cash": "change_in_exchange_rate",
        "net_change_in_cash": "net_change_in_cash",
        "cash_at_end_of_period": "cash_at_end_of_period",
        "cash_at_beginning_of_period": "cash_at_beginning_of_period",
        "operating_cash_flow": "operating_cash_flow",
        "capital_expenditure": "capital_expenditure",
        "free_cash_flow": "free_cash_flow",
        "link": "link",
        "final_link": "final_link",
    },
}
CASH_PLOT_CHOICES = [
    "operating_cash_flow",
    "payments_for_operating_activities",
    "proceeds_from_operating_activities",
    "change_in_operating_liabilities",
    "change_in_operating_assets",
    "depreciation_depletion_and_amortization",
    "capital_expenditure",
    "change_in_receivables",
    "inventory",
    "profit_loss",
    "cash_flow_from_investment",
    "cash_flow_from_financing",
    "proceeds_from_repayments_of_short_term_debt",
    "common_stock_repurchased",
    "payments_for_repurchase_of_equity",
    "payments_for_repurchase_of_preferred_stock",
    "dividends_paid",
    "dividend_payout_common_stock",
    "dividend_payout_preferred_stock",
    "common_stock_issued",
    "proceeds_from_issuance_of_long_term_debt_and_capital_securities_net",
    "proceeds_from_issuance_of_preferred_stock",
    "proceeds_from_repurchase_of_equity",
    "proceeds_from_sale_of_treasury_stock",
    "net_change_in_cash",
    "change_in_exchange_rate",
    "net_income",
    "depreciation_&_amortisation",
    "net_cash_flow_from_financing_activities_continuing",
    "net_cash_flow_from_investing_activities_continuing",
    "net_cash_flow_continuing",
    "net_cash_provided_by_operating_activities",
    "deferred_income_taxes",
    "stock_based_compensation",
    "change_in_working_capital",
    "accounts_payable",
    "other_working_capital",
    "investments_in_property,_plant_and_equipment",
    "acquisitions_net",
    "purchases_of_investments",
    "sales_maturities_of_investments",
    "other_investing_activities",
    "debt_repayment",
    "other_financing_activities",
    "cash_at_beginning_of_period",
    "cash_at_end_of_period",
    "free_cash_flow",
    "other_non_cash_items",
]
