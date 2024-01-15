---
title: CASH
description: Learn how to use the Cash Flow Statement API endpoint to retrieve information
  about cash flow statements. Understand the parameters and return values of the API,
  and explore the available data fields for cash flow statements.
keywords: 
- Cash Flow Statement
- cash flow statement parameters
- cash flow statement returns
- cash flow statement data
- python obb.equity.fundamental.cash
- symbol
- period
- limit
- provider
- cik
- filing date
- period of report date
- include sources
- order
- sort
- net income
- depreciation and amortization
- stock based compensation
- deferred income tax
- other non-cash items
- changes in operating assets and liabilities
- accounts receivables
- inventory
- vendor non-trade receivables
- other current and non-current assets
- accounts payables
- deferred revenue
- other current and non-current liabilities
- net cash flow from operating activities
- purchases of marketable securities
- sales from maturities of investments
- investments in property plant and equipment
- payments from acquisitions
- other investing activities
- net cash flow from investing activities
- taxes paid on net share settlement
- dividends paid
- common stock repurchased
- debt proceeds
- debt repayment
- other financing activities
- net cash flow from financing activities
- net change in cash
---

<!-- markdownlint-disable MD041 -->

Cash Flow Statement. Information about the cash flow statement.

## Syntax

```excel wordwrap
=OBB.EQUITY.FUNDAMENTAL.CASH(symbol;[period];[limit];[provider];[fiscal_year];[filing_date];[filing_date_lt];[filing_date_lte];[filing_date_gt];[filing_date_gte];[period_of_report_date];[period_of_report_date_lt];[period_of_report_date_lte];[period_of_report_date_gt];[period_of_report_date_gte];[include_sources];[order];[sort])
```

### Example

```excel wordwrap
=OBB.EQUITY.FUNDAMENTAL.CASH("AAPL")
```

---

## Parameters

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| **symbol** | **Text** | **Symbol to get data for.** | **True** |
| period | Text | Time period of the data to return. | False |
| limit | Number | The number of data entries to return. | False |
| provider | Text | Options: fmp, intrinio, polygon, defaults to fmp. | False |
| fiscal_year | Number | The specific fiscal year.  Reports do not go beyond 2008. (provider: intrinio) | False |
| filing_date | Text | Filing date of the financial statement. (provider: polygon) | False |
| filing_date_lt | Text | Filing date less than the given date. (provider: polygon) | False |
| filing_date_lte | Text | Filing date less than or equal to the given date. (provider: polygon) | False |
| filing_date_gt | Text | Filing date greater than the given date. (provider: polygon) | False |
| filing_date_gte | Text | Filing date greater than or equal to the given date. (provider: polygon) | False |
| period_of_report_date | Text | Period of report date of the financial statement. (provider: polygon) | False |
| period_of_report_date_lt | Text | Period of report date less than the given date. (provider: polygon) | False |
| period_of_report_date_lte | Text | Period of report date less than or equal to the given date. (provider: polygon) | False |
| period_of_report_date_gt | Text | Period of report date greater than the given date. (provider: polygon) | False |
| period_of_report_date_gte | Text | Period of report date greater than or equal to the given date. (provider: polygon) | False |
| include_sources | Boolean | Whether to include the sources of the financial statement. (provider: polygon) | False |
| order | Any | Order of the financial statement. (provider: polygon) | False |
| sort | Any | Sort of the financial statement. (provider: polygon) | False |

---

## Return Data

| Name | Description |
| ---- | ----------- |
| symbol | Symbol representing the entity requested in the data.  |
| period_ending | The end date of the reporting period.  |
| fiscal_period | The fiscal period of the report.  |
| fiscal_year | The fiscal year of the fiscal period.  |
| filing_date | The date of the filing. (provider: fmp) |
| accepted_date | The date the filing was accepted. (provider: fmp) |
| reported_currency | The currency in which the cash flow statement was reported. (provider: fmp);     The currency in which the balance sheet is reported. (provider: intrinio) |
| net_income | Net income. (provider: fmp);     Consolidated Net Income. (provider: intrinio) |
| depreciation_and_amortization | Depreciation and amortization. (provider: fmp) |
| deferred_income_tax | Deferred income tax. (provider: fmp) |
| stock_based_compensation | Stock-based compensation. (provider: fmp) |
| change_in_working_capital | Change in working capital. (provider: fmp) |
| change_in_account_receivables | Change in account receivables. (provider: fmp) |
| change_in_inventory | Change in inventory. (provider: fmp) |
| change_in_account_payable | Change in account payable. (provider: fmp) |
| change_in_other_working_capital | Change in other working capital. (provider: fmp) |
| change_in_other_non_cash_items | Change in other non-cash items. (provider: fmp) |
| net_cash_from_operating_activities | Net cash from operating activities. (provider: fmp, intrinio) |
| purchase_of_property_plant_and_equipment | Purchase of property, plant and equipment. (provider: fmp, intrinio) |
| acquisitions | Acquisitions. (provider: fmp, intrinio) |
| purchase_of_investment_securities | Purchase of investment securities. (provider: fmp, intrinio) |
| sale_and_maturity_of_investments | Sale and maturity of investments. (provider: fmp, intrinio) |
| other_investing_activities | Other investing activities. (provider: fmp, intrinio) |
| net_cash_from_investing_activities | Net cash from investing activities. (provider: fmp, intrinio) |
| repayment_of_debt | Repayment of debt. (provider: fmp, intrinio) |
| issuance_of_common_equity | Issuance of common equity. (provider: fmp, intrinio) |
| repurchase_of_common_equity | Repurchase of common equity. (provider: fmp, intrinio) |
| payment_of_dividends | Payment of dividends. (provider: fmp, intrinio) |
| other_financing_activities | Other financing activities. (provider: fmp, intrinio) |
| net_cash_from_financing_activities | Net cash from financing activities. (provider: fmp, intrinio) |
| effect_of_exchange_rate_changes_on_cash | Effect of exchange rate changes on cash. (provider: fmp) |
| net_change_in_cash_and_equivalents | Net change in cash and equivalents. (provider: fmp, intrinio) |
| cash_at_beginning_of_period | Cash at beginning of period. (provider: fmp) |
| cash_at_end_of_period | Cash at end of period. (provider: fmp) |
| operating_cash_flow | Operating cash flow. (provider: fmp) |
| capital_expenditure | Capital expenditure. (provider: fmp) |
| free_cash_flow | Free cash flow. (provider: fmp) |
| link | Link to the filing. (provider: fmp) |
| final_link | Link to the filing document. (provider: fmp) |
| provision_for_loan_losses | Provision for Loan Losses (provider: intrinio) |
| provision_for_credit_losses | Provision for credit losses (provider: intrinio) |
| depreciation_expense | Depreciation Expense. (provider: intrinio) |
| amortization_expense | Amortization Expense. (provider: intrinio) |
| share_based_compensation | Share-based compensation. (provider: intrinio) |
| non_cash_adjustments_to_reconcile_net_income | Non-Cash Adjustments to Reconcile Net Income. (provider: intrinio) |
| changes_in_operating_assets_and_liabilities | Changes in Operating Assets and Liabilities (Net) (provider: intrinio) |
| net_cash_from_continuing_operating_activities | Net Cash from Continuing Operating Activities (provider: intrinio) |
| net_cash_from_discontinued_operating_activities | Net Cash from Discontinued Operating Activities (provider: intrinio) |
| net_income_continuing_operations | Net Income (Continuing Operations) (provider: intrinio) |
| net_income_discontinued_operations | Net Income (Discontinued Operations) (provider: intrinio) |
| divestitures | Divestitures (provider: intrinio) |
| sale_of_property_plant_and_equipment | Sale of Property, Plant, and Equipment (provider: intrinio) |
| purchase_of_investments | Purchase of Investments (provider: intrinio) |
| loans_held_for_sale | Loans Held for Sale (Net) (provider: intrinio) |
| net_cash_from_continuing_investing_activities | Net Cash from Continuing Investing Activities (provider: intrinio) |
| net_cash_from_discontinued_investing_activities | Net Cash from Discontinued Investing Activities (provider: intrinio) |
| repurchase_of_preferred_equity | Repurchase of Preferred Equity (provider: intrinio) |
| issuance_of_preferred_equity | Issuance of Preferred Equity (provider: intrinio) |
| issuance_of_debt | Issuance of Debt (provider: intrinio) |
| cash_interest_received | Cash Interest Received (provider: intrinio) |
| net_change_in_deposits | Net Change in Deposits (provider: intrinio) |
| net_increase_in_fed_funds_sold | Net Increase in Fed Funds Sold (provider: intrinio) |
| net_cash_from_continuing_financing_activities | Net Cash from Continuing Financing Activities (provider: intrinio) |
| net_cash_from_discontinued_financing_activities | Net Cash from Discontinued Financing Activities (provider: intrinio) |
| effect_of_exchange_rate_changes | Effect of Exchange Rate Changes (provider: intrinio) |
| other_net_changes_in_cash | Other Net Changes in Cash (provider: intrinio) |
| cash_income_taxes_paid | Cash Income Taxes Paid (provider: intrinio) |
| cash_interest_paid | Cash Interest Paid (provider: intrinio) |
| net_cash_flow_from_operating_activities_continuing | Net cash flow from operating activities continuing. (provider: polygon) |
| net_cash_flow_from_operating_activities_discontinued | Net cash flow from operating activities discontinued. (provider: polygon) |
| net_cash_flow_from_operating_activities | Net cash flow from operating activities. (provider: polygon) |
| net_cash_flow_from_investing_activities_continuing | Net cash flow from investing activities continuing. (provider: polygon) |
| net_cash_flow_from_investing_activities_discontinued | Net cash flow from investing activities discontinued. (provider: polygon) |
| net_cash_flow_from_investing_activities | Net cash flow from investing activities. (provider: polygon) |
| net_cash_flow_from_financing_activities_continuing | Net cash flow from financing activities continuing. (provider: polygon) |
| net_cash_flow_from_financing_activities_discontinued | Net cash flow from financing activities discontinued. (provider: polygon) |
| net_cash_flow_from_financing_activities | Net cash flow from financing activities. (provider: polygon) |
| net_cash_flow_continuing | Net cash flow continuing. (provider: polygon) |
| net_cash_flow_discontinued | Net cash flow discontinued. (provider: polygon) |
| exchange_gains_losses | Exchange gains losses. (provider: polygon) |
| net_cash_flow | Net cash flow. (provider: polygon) |
