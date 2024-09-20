"""Primary Dealer Positioning Series IDs."""

# pylint: disable=line-too-long
# flake8: noqa

FAILS_SERIES_TO_TITLE = {
    "PDFTD-CS": "FTD Corporate Securities",
    "PDFTR-CS": "FTR Corporate Securities",
    "PDFASCFDA": "FTD Corporate Securities",
    "PDFASCFRA": "FTR Corporate Securities",
    "PDFTD-FGEM": "FTD Agency and GSE Securities (Ex-MBS)",
    "PDFTR-FGEM": "FTR Agency and GSE Securities (Ex-MBS)",
    "PDFASFAFDA": "FTD Agency and GSE Securities (Ex-MBS)",
    "PDFASFAFRA": "FTR Agency and GSE Securities (Ex-MBS)",
    "PDFTD-FGM": "FTD Agency and GSE MBS",
    "PDFTR-FGM": "FTR Agency and GSE MBS",
    "PDFTD-OM": "FTD Other MBS",
    "PDFTR-OM": "FTR Other MBS",
    "PDFASMBFDA": "FTD MBS",
    "PDFASMBFRA": "FTR MBS",
    "PDFTD-UST": "FTD TIPS",
    "PDFTR-UST": "FTR TIPS",
    "PDFTD-USTET": "FTD Treasury Securities (Ex-TIPS)",
    "PDFTR-USTET": "FTR Treasury Securities (Ex-TIPS)",
    "PDFASUFRA": "FTR Treasury Securities",
    "PDFASUFDA": "FTD Treasury Securities",
}


POSITION_SERIES_TO_TITLE = {
    "PDPOSGS-B": "BILLS (EX. TIPS): DEALER POSITION - LONG. - BILLS (EX. TIPS): DEALER POSITION - SHORT",
    "PDPOSGSC-L2": "TREASURIES (EX. TIPS) COUPONS DUE IN LESS THAN OR EQUAL TO 2 YEARS: DEALER POSITION - NET",
    "PDPOSGSC-G2L3": "TREASURIES (EX. TIPS) COUPONS DUE IN MORE THAN 2 YEARS BUT LESS THAN OR EQUAL TO 3 YEARS: DEALER POSITION - NET",
    "PDPOSGSC-G3L6": "TREASURIES (EX. TIPS) COUPONS DUE IN MORE THAN 3 YEARS BUT LESS THAN OR EQUAL TO 6 YEARS: DEALER POSITION - NET",
    "PDPOSGSC-G6L7": "TREASURIES (EX. TIPS) COUPONS DUE IN MORE THAN 6 YEARS BUT LESS THAN OR EQUAL TO 7 YEARS: DEALER POSITION - NET",
    "PDPOSGSC-G7L11": "TREASURIES (EX. TIPS) COUPONS DUE IN MORE THAN 7 YEARS BUT LESS THAN OR EQUAL TO 11 YEARS: DEALER POSITION - NET",
    "PDPOSGSC-G11L21": "TREASURIES (EX. TIPS): COUPONS DUE IN MORE THAN 11 YEARS BUT LESS THAN OR EQUAL TO 21 YEARS: OUTRIGHT POSITIONS - NET",
    "PDPOSGSC-G21": "TREASURIES (EX. TIPS): COUPONS DUE IN MORE THAN 21 YEARS: OUTRIGHT POSITIONS - NET",
    "PDPOSTIPS-L2": "TIPS DUE IN LESS THAN OR EQUAL TO 2 YEARS: DEALER POSITION - NET",
    "PDPOSTIPS-G2": "TIPS DUE IN MORE THAN 2 YEARS BUT LESS THAN OR EQUAL TO 6 YEARS: DEALER POSITION - NET",
    "PDPOSTIPS-G6L11": "TIPS DUE IN MORE THAN 6 YEARS BUT LESS THAN OR EQUAL TO 11 YEARS: DEALER POSITION - NET",
    "PDPOSTIPS-G11": "TIPS DUE IN MORE THAN 11 YEARS: DEALER POSITION - NET",
    "PDPOSGS-BFRN": "FLOATING RATE NOTES: DEALER POSITION - NET",
    "PDPOSFGS-C": "AGENCY AND GSE (EX. MBS) - COUPONS: DEALER POSITION - NET",
    "PDPOSFGS-DN": "AGENCY AND GSE (EX. MBS) - DISCOUNT NOTES: DEALER POSITION - NET",
    "PDPOSMBSFGS-TBA": "MBS: FEDERAL AGENCY AND GSE MBS: TBAs - OUTRIGHT POSITIONS - NET",
    "PDPOSMBSFGS-OR": "MBS - ALL OTHER FEDERAL AGENCY AND GSE RESIDENTIAL MBS: DEALER POSITION - NET",
    "PDPOSMBSFGS-ST": "MBS: FEDERAL AGENCY AND GSE MBS: SPECIFIED POOLS - OUTRIGHT POSITIONS - NET",
    "PDPOSMBSNA-R": "MBS - NON-AGENCY RESIDENTIAL MBS: DEALER POSITION - NET",
    "PDPOSMBSFGS-C": "MBS - FEDERAL AGENCY AND GSE CMBS: DEALER POSITION - NET",
    "PDPOSMBSNA-O": "MBS - NON-AGENCY OTHER CMBS: DEALER POSITION - NET",
    "PDPOSSMGO-L13": "STATE AND MUNICIPAL GOVERNMENT OBLIGATIONS DUE IN LESS THAN OR EQUAL TO 13 MONTHS: DEALER POSITION - NET",
    "PDPOSSMGO-G13": "STATE AND MUNICIPAL GOVERNMENT OBLIGATIONS DUE IN MORE THAN 13 MONTHS BUT LESS THAN OR EQUAL TO 5 YEARS: DEALER POSITION - NET",
    "PDPOSSMGO-G5L10": "STATE AND MUNICIPAL GOVERNMENT OBLIGATIONS DUE IN MORE THAN 5 YEARS BUT LESS THAN OR EQUAL TO 10 YEARS: DEALER POSITION - NET",
    "PDPOSSMGO-G10": "STATE AND MUNICIPAL GOVERNMENT OBLIGATIONS DUE IN MORE THAN 10 YEARS: DEALER POSITION - NET",
    "PDPOSCSCP": "COMMERCIAL PAPER: DEALER POSITION - NET",
    "PDPOSCSBND-L13": "CORPORATE SECURITIES: INVESTMENT GRADE BONDS, NOTES AND DEBENTURES DUE IN LESS THAN OR EQUAL TO 13 MONTHS: DEALER POSITION - NET",
    "PDPOSCSBND-G13": "CORPORATE SECURITIES: INVESTMENT GRADE BONDS NOTES AND DEBENTURES DUE IN MORE THAN 13 MONTHS BUT LESS THAN OR EQUAL TO 5 YEARS: DEALER POSITION - NET",
    "PDPOSCSBND-G5L10": "CORPORATE SECURITIES INVESTMENT GRADE BONDS NOTES AND DEBENTURES DUE IN MORE THAN 5 YEARS BUT LESS THAN OR EQUAL TO 10 YEARS: DEALER POSITION - NET",
    "PDPOSCSBND-G10": "CORPORATE SECURITIES INVESTMENT GRADE BONDS NOTES AND DEBENTURES DUE IN MORE THAN 10 YEARS: DEALER POSITION - NET",
    "PDPOSCSBND-BELL13": "CORPORATE SECURITIES BELOW INVESTMENT GRADE DUE IN LESS THAN OR EQUAL TO 13 MONTHS: DEALER POSITION - NET",
    "PDPOSCSBND-BELG13": "CORPORATE SECURITIES BELOW INVESTMENT GRADE BONDS NOTES AND DEBENTURES DUE IN MORE THAN 13 MONTHS BUT LESS THAN OR EQUAL TO 5 YEARS: DEALER POSITION - NET",
    "PDPOSCSBND-BELG5L10": "CORPORATE SECURITIES BELOW INVESTMENT GRADE BONDS NOTES AND DEBENTURES DUE IN MORE THAN 5 YEARS BUT LESS THAN OR EQUAL TO 10 YEARS: DEALER POSITION - NET",
    "PDPOSCSBND-BELG10": "CORPORATE SECURITIES BELOW INVESTMENT GRADE BONDS NOTES AND DEBENTURES DUE IN MORE THAN 10 YEARS: DEALER POSITION - NET",
    "PDPOSABS-ALB": "AUTOMOBILE LOAN-BACKED SECURITIES: DEALER POSITION - NET",
    "PDPOSABS-CCB": "CREDIT CARD-BACKED SECURITIES: DEALER POSITION - NET",
    "PDPOSABS-SLB": "STUDENT LOAN-BACKED SECURITIES: DEALER POSITION - NET",
    "PDPOSABS-OAB": "OTHER DEALER POSITION - NET",
}

POSITION_SERIES_TO_FIELD = {
    "dealer_position": {
        "PDPOSGS-B": "bills",
        "PDPOSGSC-L2": "coupons_lte_2_years",
        "PDPOSGSC-G2L3": "coupons_gt_2_years_lt_3_years",
        "PDPOSGSC-G3L6": "coupons_gt_3_years_lt_6_years",
        "PDPOSGSC-G6L7": "coupons_gt_6_years_lt_7_years",
        "PDPOSGSC-G7L11": "coupons_gt_7_years_lt_11_years",
        "PDPOSGSC-G11L21": "coupons_gt_11_years_lt_21_years",
        "PDPOSGSC-G21": "coupons_gt_21_years",
        "PDPOSTIPS-L2": "tips_lt_2_years",
        "PDPOSTIPS-G2": "tips_gt_2_years_lt_6_years",
        "PDPOSTIPS-G6L11": "tips_gt_6_years_lt_11_years",
        "PDPOSTIPS-G11": "tips_gt_11_years",
        "PDPOSGS-BFRN": "floating_rate_notes",
        "PDPOSFGS-DN": "discount_notes",
        "PDPOSFGS-C": "coupons_agency",
        "PDPOSMBSFGS-TBA": "mbs_agency_and_gse_tba",
        "PDPOSMBSFGS-OR": "mbs_agency_and_gse_other_residential",
        "PDPOSMBSFGS-ST": "mbs_agency_and_gse_specified_pools",
        "PDPOSMBSNA-R": "mbs_non_agency_residential",
        "PDPOSMBSFGS-C": "cmbs_agency_and_gse",
        "PDPOSMBSNA-O": "cmbs_non_agency",
        "PDPOSSMGO-L13": "municipal_lt_13_months",
        "PDPOSSMGO-G13": "municipal_gt_13_months_lt_5_years",
        "PDPOSSMGO-G5L10": "municipal_gt_5_years_lt_10_years",
        "PDPOSSMGO-G10": "municipal_gt_10_years",
        "PDPOSCSCP": "commercial_paper",
        "PDPOSCSBND-L13": "corporate_investment_grade_lt_13_months",
        "PDPOSCSBND-G13": "corporate_investment_grade_gt_13_months_lt_5_years",
        "PDPOSCSBND-G5L10": "corporate_investment_grade_gt_5_years_lt_10_years",
        "PDPOSCSBND-G10": "corporate_investment_grade_gt_10_years",
        "PDPOSCSBND-BELL13": "corporate_junk_lt_13_months",
        "PDPOSCSBND-BELG13": "corporate_junk_gt_13_months_lt_5_years",
        "PDPOSCSBND-BELG5L10": "corporate_junk_gt_5_years_lt_10_years",
        "PDPOSCSBND-BELG10": "corporate_junk_gt_10_years",
        "PDPOSABS-ALB": "abs_autos",
        "PDPOSABS-CCB": "abs_credit_cards",
        "PDPOSABS-SLB": "abs_student_loans",
        "PDPOSABS-OAB": "abs_other",
    },
}

POSITION_GROUPS_TO_SERIES = {
    "treasuries": [
        "PDPOSGS-B",
        "PDPOSGSC-L2",
        "PDPOSGSC-G2L3",
        "PDPOSGSC-G3L6",
        "PDPOSGSC-G6L7",
        "PDPOSGSC-G7L11",
        "PDPOSGSC-G11L21",
        "PDPOSGSC-G21",
        "PDPOSFGS-C",
        "PDPOSTIPS-L2",
        "PDPOSTIPS-G2",
        "PDPOSTIPS-G6L11",
        "PDPOSTIPS-G11",
        "PDPOSGS-BFRN",
        "PDPOSFGS-DN",
    ],
    "bills": ["PDPOSGS-B"],
    "coupons": [
        "PDPOSGSC-L2",
        "PDPOSGSC-G2L3",
        "PDPOSGSC-G3L6",
        "PDPOSGSC-G6L7",
        "PDPOSGSC-G7L11",
        "PDPOSGSC-G11L21",
        "PDPOSGSC-G21",
    ],
    "notes": ["PDPOSGS-BFRN", "PDPOSFGS-DN"],
    "tips": ["PDPOSTIPS-L2", "PDPOSTIPS-G2", "PDPOSTIPS-G6L11", "PDPOSTIPS-G11"],
    "mbs": [
        "PDPOSMBSFGS-TBA",
        "PDPOSMBSFGS-OR",
        "PDPOSMBSFGS-ST",
        "PDPOSMBSNA-R",
        "PDPOSMBSFGS-C",
        "PDPOSMBSNA-O",
    ],
    "cmbs": ["PDPOSMBSFGS-C", "PDPOSMBSNA-O"],
    "municipal": ["PDPOSSMGO-L13", "PDPOSSMGO-G13", "PDPOSSMGO-G5L10", "PDPOSSMGO-G10"],
    "corporate": [
        "PDPOSCSCP",
        "PDPOSCSBND-L13",
        "PDPOSCSBND-G13",
        "PDPOSCSBND-G5L10",
        "PDPOSCSBND-G10",
        "PDPOSCSBND-BELL13",
        "PDPOSCSBND-BELG13",
        "PDPOSCSBND-BELG5L10",
        "PDPOSCSBND-BELG10",
    ],
    "commercial_paper": ["PDPOSCSCP"],
    "corporate_ig": [
        "PDPOSCSBND-L13",
        "PDPOSCSBND-G13",
        "PDPOSCSBND-G5L10",
        "PDPOSCSBND-G10",
    ],
    "corporate_junk": [
        "PDPOSCSBND-BELL13",
        "PDPOSCSBND-BELG13",
        "PDPOSCSBND-BELG5L10",
        "PDPOSCSBND-BELG10",
    ],
    "abs": ["PDPOSABS-ALB", "PDPOSABS-CCB", "PDPOSABS-SLB", "PDPOSABS-OAB"],
}
