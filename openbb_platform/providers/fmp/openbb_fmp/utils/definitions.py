"""FMP Definitions"""

from typing import Literal

SECTORS = Literal[
    "Consumer Cyclical",
    "Energy",
    "Technology",
    "Industrials",
    "Financial Services",
    "Basic Materials",
    "Communication Services",
    "Consumer Defensive",
    "Healthcare",
    "Real Estate",
    "Utilities",
    "Industrial Goods",
    "Financial",
    "Services",
    "Conglomerates",
]

EXCHANGES = Literal[
    "amex",
    "ase",
    "asx",
    "ath",
    "bme",
    "bru",
    "bud",
    "bue",
    "cai",
    "cnq",
    "cph",
    "dfm",
    "doh",
    "etf",
    "euronext",
    "hel",
    "hkse",
    "ice",
    "iob",
    "ist",
    "jkt",
    "jnb",
    "jpx",
    "kls",
    "koe",
    "ksc",
    "kuw",
    "lse",
    "mex",
    "nasdaq",
    "neo",
    "nse",
    "nyse",
    "nze",
    "osl",
    "otc",
    "pnk",
    "pra",
    "ris",
    "sao",
    "sau",
    "set",
    "sgo",
    "shh",
    "shz",
    "six",
    "sto",
    "tai",
    "tlv",
    "tsx",
    "two",
    "vie",
    "wse",
    "xetra",
]

TRANSACTION_TYPES = Literal[
    "A-Award",
    "C-Conversion",
    "D-Return",
    "E-ExpireShort",
    "F-InKind",
    "G-Gift",
    "H-ExpireLong",
    "I-Discretionary",
    "J-Other",
    "L-Small",
    "M-Exempt",
    "O-OutOfTheMoney",
    "P-Purchase",
    "S-Sale",
    "U-Tender",
    "W-Will",
    "X-InTheMoney",
    "Z-Trust",
]
