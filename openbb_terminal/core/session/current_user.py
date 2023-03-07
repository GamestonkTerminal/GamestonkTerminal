# IMPORTS STANDARD
from copy import deepcopy
from typing import Optional

# IMPORTS INTERNAL
from openbb_terminal.core.models import (
    CredentialsModel,
    PreferencesModel,
    ProfileModel,
    UserModel,
)
from openbb_terminal.core.session.env_handler import reading_env
from openbb_terminal.core.terminal_style import TerminalStyle

__env_dict = reading_env()
__credentials = CredentialsModel(**__env_dict)
__preferences = PreferencesModel(**__env_dict)
__profile = ProfileModel()
__local_user = UserModel(  # type: ignore
    credentials=__credentials,
    preferences=__preferences,
    profile=__profile,
)
__current_user = __local_user


def get_current_user() -> UserModel:
    """Get current user."""
    return deepcopy(__current_user)


def set_current_user(user: UserModel):
    """Set current user."""
    global __current_user  # pylint: disable=global-statement
    __current_user = user


def is_local() -> bool:
    """Check if user is guest.

    Returns
    -------
    bool
        True if user is guest, False otherwise.
    """
    return not bool(__current_user.profile.token)


def copy_user(
    credentials: Optional[CredentialsModel] = None,
    preferences: Optional[PreferencesModel] = None,
    profile: Optional[ProfileModel] = None,
    user: Optional[UserModel] = None,
):
    current_user = user or get_current_user()
    credentials = credentials or current_user.credentials
    preferences = preferences or current_user.preferences
    profile = profile or current_user.profile

    user_copy = UserModel(  # type: ignore
        credentials=credentials,
        preferences=preferences,
        profile=profile,
    )

    return user_copy


theme = TerminalStyle(
    __current_user.preferences.MPL_STYLE,
    __current_user.preferences.PMF_STYLE,
    __current_user.preferences.RICH_STYLE,
    __current_user.preferences.USER_DATA_DIRECTORY / "styles" / "user",
    __current_user.preferences.USE_CMD_LOCATION_FIGURE,
    __current_user.preferences.USE_WATERMARK,
    __current_user.preferences.USE_ION,
)
