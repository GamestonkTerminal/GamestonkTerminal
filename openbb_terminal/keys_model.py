import logging
import os
from typing import Dict
import dotenv
import requests
import pandas as pd
from openbb_terminal import config_terminal as cfg
from openbb_terminal.core.config.paths import USER_ENV_FILE
from openbb_terminal.rich_config import console

logger = logging.getLogger(__name__)


def set_fred_key(key: str, show_output: bool = False) -> str:
    """Set FRED API key.

    Parameters
    ----------
        key: str
            Fred API key
    Returns
    -------
    str
        API key status. One of the following:
            not defined
            defined, test failed
            defined, test passed
            defined, test inconclusive
    """
    os.environ["OPENBB_API_FRED_KEY"] = key
    dotenv.set_key(str(USER_ENV_FILE), "OPENBB_API_FRED_KEY", key)
    cfg.API_FRED_KEY = key
    status = check_fred_key(show_output)

    return status


def check_fred_key(show_output: bool = False) -> str:
    """Check FRED key"""

    if cfg.API_FRED_KEY == "REPLACE_ME":
        logger.info("FRED key not defined")
        status = "not defined"
    else:
        r = requests.get(
            f"https://api.stlouisfed.org/fred/series?series_id=GNPCA&api_key={cfg.API_FRED_KEY}"
        )
        if r.status_code in [403, 401, 400]:
            logger.warning("FRED key defined, test failed")
            status = "defined, test failed"
        elif r.status_code == 200:
            logger.info("FRED key defined, test passed")
            status = "defined, test passed"
        else:
            logger.warning("FRED key defined, test inconclusive")
            status = "defined, test inconclusive"

    if show_output:
        console.print(status + "\n")

    return status


def get_keys() -> Dict:
    """Get dictionary with currently set API keys.

    Returns:
        Dict: key: API -> values: KEY
    """

    df = pd.read_csv(str(USER_ENV_FILE), delimiter="=", header=None)
    df = df.rename(columns={0: "API", 1: "KEY"})
    df = df.set_index("API")
    df["KEY"] = df["KEY"].apply(lambda x: x[1:-1])
    keys_dict = df.to_dict().get("KEY")

    return keys_dict
