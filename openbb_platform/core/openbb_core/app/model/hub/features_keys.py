"""Model for API keys for various providers."""

from typing import Optional

from pydantic import BaseModel, Field


class FeaturesKeys(BaseModel):
    """API keys for various providers."""

    API_BITQUERY_KEY: Optional[str] = Field(default=None)
    API_BIZTOC_TOKEN: Optional[str] = Field(default=None)
    API_CMC_KEY: Optional[str] = Field(default=None)
    API_COINGLASS_KEY: Optional[str] = Field(default=None)
    API_CRYPTO_PANIC_KEY: Optional[str] = Field(default=None)
    API_DAPPRADAR_KEY: Optional[str] = Field(default=None)
    API_DATABENTO_KEY: Optional[str] = Field(default=None)
    API_EODHD_KEY: Optional[str] = Field(default=None)
    API_ETHPLORER_KEY: Optional[str] = Field(default=None)
    API_FINNHUB_KEY: Optional[str] = Field(default=None)
    API_FRED_KEY: Optional[str] = Field(default=None)
    API_GITHUB_KEY: Optional[str] = Field(default=None)
    API_GLASSNODE_KEY: Optional[str] = Field(default=None)
    API_INTRINIO_KEY: Optional[str] = Field(default=None)
    API_KEY_ALPHAVANTAGE: Optional[str] = Field(default=None)
    API_KEY_FINANCIALMODELINGPREP: Optional[str] = Field(default=None)
    API_KEY_QUANDL: Optional[str] = Field(default=None)
    API_MESSARI_KEY: Optional[str] = Field(default=None)
    API_NEWS_TOKEN: Optional[str] = Field(default=None)
    API_POLYGON_KEY: Optional[str] = Field(default=None)
    API_REDDIT_CLIENT_ID: Optional[str] = Field(default=None)
    API_REDDIT_CLIENT_SECRET: Optional[str] = Field(default=None)
    API_REDDIT_PASSWORD: Optional[str] = Field(default=None)
    API_REDDIT_USERNAME: Optional[str] = Field(default=None)
    API_REDDIT_USER_AGENT: Optional[str] = Field(default=None)
    API_SANTIMENT_KEY: Optional[str] = Field(default=None)
    API_SHROOM_KEY: Optional[str] = Field(default=None)
    API_SMARTSTAKE_KEY: Optional[str] = Field(default=None)
    API_SMARTSTAKE_TOKEN: Optional[str] = Field(default=None)
    API_TOKEN_TERMINAL_KEY: Optional[str] = Field(default=None)
    API_WHALE_ALERT_KEY: Optional[str] = Field(default=None)
