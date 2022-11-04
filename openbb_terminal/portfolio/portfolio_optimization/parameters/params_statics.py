DEFAULT_RANGE = [value / 1000 for value in range(0, 1001)]
DEFAULT_BOOL = ["True", "False"]

AVAILABLE_OPTIONS = {
    "historic_period": ["d", "w", "mo", "y", "ytd", "max"],
    "start_period": ["Any"],
    "end_period": ["Any"],
    "log_returns": DEFAULT_BOOL,
    "return_frequency": ["d", "w", "m"],
    "max_nan": DEFAULT_RANGE,
    "threshold_value": DEFAULT_RANGE,
    "nan_fill_method": [
        "linear",
        "time",
        "nearest",
        "zero",
        "slinear",
        "quadratic",
        "cubic",
    ],
    "risk_free": DEFAULT_RANGE,
    "significance_level": DEFAULT_RANGE,
    "risk_measure": [
        "MV",
        "MAD",
        "MSV",
        "FLPM",
        "SLPM",
        "CVaR",
        "EVaR",
        "WR",
        "ADD",
        "UCI",
        "CDaR",
        "EDaR",
        "MDD",
    ],
    "target_return": DEFAULT_RANGE + [-x for x in DEFAULT_RANGE],
    "target_risk": DEFAULT_RANGE + [-x for x in DEFAULT_RANGE],
    "expected_return": ["hist", "ewma1", "ewma2"],
    "covariance": [
        "hist",
        "ewma1",
        "ewma2",
        "ledoit",
        "oas",
        "shrunk",
        "gl",
        "jlogo",
        "fixed",
        "spectral",
        "shrink",
    ],
    "smoothing_factor_ewma": DEFAULT_RANGE,
    "long_allocation": DEFAULT_RANGE,
    "short_allocation": DEFAULT_RANGE,
    "risk_aversion": [value / 100 for value in range(-500, 501)],
    "amount_portfolios": range(1, 10001),
    "random_seed": range(1, 10001),
    "tangency": DEFAULT_BOOL,
    "risk_parity_model": ["A", "B", "C"],
    "penal_factor": DEFAULT_RANGE + [-x for x in DEFAULT_RANGE],
    "co_dependence": [
        "pearson",
        "spearman",
        "abs_pearson",
        "abs_spearman",
        "distance",
        "mutual_info",
        "tail",
    ],
    "cvar_simulations": range(1, 10001),
    "cvar_significance": DEFAULT_RANGE,
    "linkage": [
        "single",
        "complete",
        "average",
        "weighted",
        "centroid",
        "ward",
        "dbht",
    ],
    "max_clusters": range(1, 101),
    "amount_bins": ["KN", "FD", "SC", "HGR", "Integer"],
    "alpha_tail": DEFAULT_RANGE,
    "leaf_order": DEFAULT_BOOL,
    "objective": ["MinRisk", "Utility", "Sharpe", "MaxRet"],
}

DEFAULT_PARAMETERS = [
    "historic_period",
    "start_period",
    "end_period",
    "log_returns",
    "return_frequency",
    "max_nan",
    "threshold_value",
    "nan_fill_method",
    "risk_free",
    "significance_level",
]
MODEL_PARAMS = {
    "maxsharpe": [
        "risk_measure",
        "target_return",
        "target_risk",
        "expected_return",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "short_allocation",
    ],
    "minrisk": [
        "risk_measure",
        "target_return",
        "target_risk",
        "expected_return",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "short_allocation",
    ],
    "maxutil": [
        "risk_measure",
        "target_return",
        "target_risk",
        "expected_return",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "short_allocation",
        "risk_aversion",
    ],
    "maxret": [
        "risk_measure",
        "target_return",
        "target_risk",
        "expected_return",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
    ],
    "maxdiv": ["covariance", "long_allocation"],
    "maxdecorr": ["covariance", "long_allocation"],
    "ef": [
        "risk_measure",
        "long_allocation",
        "short_allocation",
        "amount_portfolios",
        "random_seed",
        "tangency",
    ],
    "equal": ["risk_measure", "long_allocation"],
    "mktcap": ["risk_measure", "long_allocation"],
    "dividend": ["risk_measure", "long_allocation"],
    "riskparity": [
        "risk_measure",
        "target_return",
        "long_allocation",
        "risk_contribution",
    ],
    "relriskparity": [
        "risk_measure",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "risk_contribution",
        "risk_parity_model",
        "penal_factor",
    ],
    "hrp": [
        "risk_measure",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "co_dependence",
        "cvar_simulations",
        "cvar_significance",
        "linkage",
        "amount_clusters",
        "max_clusters",
        "amount_bins",
        "alpha_tail",
        "leaf_order",
        "objective",
    ],
    "herc": [
        "risk_measure",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "co_dependence",
        "cvar_simulations",
        "cvar_significance",
        "linkage",
        "amount_clusters",
        "max_clusters",
        "amount_bins",
        "alpha_tail",
        "leaf_order",
        "objective",
    ],
    "nco": [
        "risk_measure",
        "covariance",
        "smoothing_factor_ewma",
        "long_allocation",
        "co_dependence",
        "cvar_simulations",
        "cvar_significance",
        "linkage",
        "amount_clusters",
        "max_clusters",
        "amount_bins",
        "alpha_tail",
        "leaf_order",
        "objective",
    ],
}
