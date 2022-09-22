# IMPORTATION STANDARD
from pathlib import Path


HOME_DIRECTORY = Path.home()
REPOSITORY_DIRECTORY = Path(__file__).parent.parent.parent.parent
SETTINGS_DIRECTORY = HOME_DIRECTORY / ".openbb_terminal"
REPOSITORY_ENV_FILE = REPOSITORY_DIRECTORY / ".env"
USER_ENV_FILE = SETTINGS_DIRECTORY / ".env"

USER_DATA_DIRECTORY = HOME_DIRECTORY / "OpenBBUserData"
