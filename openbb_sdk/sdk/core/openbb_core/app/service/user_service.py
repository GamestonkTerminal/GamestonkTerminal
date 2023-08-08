"""User service."""
from functools import reduce
from pathlib import Path
from typing import Any, Dict, List, MutableMapping, Optional

from openbb_core.app.constants import USER_SETTINGS_PATH
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.repository.abstract.access_token_repository import (
    AccessTokenRepository as AbstractAccessTokenRepository,
)
from openbb_core.app.repository.abstract.user_settings_repository import (
    UserSettingsRepository as AbstractUserSettingsRepository,
)
from openbb_core.app.repository.in_memory.access_token_repository import (
    AccessTokenRepository as InMemoryAccessTokenRepository,
)
from openbb_core.app.repository.in_memory.user_settings_repository import (
    UserSettingsRepository as InMemoryUserSettingsRepository,
)
from openbb_core.app.repository.mongodb.access_token_repository import (
    AccessTokenRepository as MongoDBAccessTokenRepository,
)
from openbb_core.app.repository.mongodb.user_settings_repository import (
    UserSettingsRepository as MongoDBUserSettingsRepository,
)
from pymongo.mongo_client import MongoClient


class UserService:
    """User service."""

    REPOSITORY_DIRECTORY = Path(__file__).parent.parent.parent.parent
    USER_SETTINGS_PATH = USER_SETTINGS_PATH
    USER_SETTINGS_ALLOWED_FIELD_SET = {"credentials", "preferences", "defaults"}

    @staticmethod
    def build_token_repository(
        valid_client: bool,
        mongodb_client: Optional[MongoClient] = None,
        access_token_repository: Optional[AbstractAccessTokenRepository] = None,
    ) -> AbstractAccessTokenRepository:
        """Build token repository."""
        if access_token_repository:
            pass
        elif mongodb_client and valid_client:
            access_token_repository = MongoDBAccessTokenRepository(
                client=mongodb_client
            )
        else:
            access_token_repository = InMemoryAccessTokenRepository()
        return access_token_repository

    @staticmethod
    def build_user_settings_repository(
        valid_client: bool,
        mongodb_client: Optional[MongoClient] = None,
        user_settings_repository: Optional[AbstractUserSettingsRepository] = None,
    ) -> AbstractUserSettingsRepository:
        """Build user settings repository."""
        if user_settings_repository:
            pass
        elif mongodb_client and valid_client:
            user_settings_repository = MongoDBUserSettingsRepository(
                client=mongodb_client
            )
        else:
            user_settings_repository = InMemoryUserSettingsRepository()
        return user_settings_repository

    @staticmethod
    def valid_client(client: Optional[MongoClient] = None) -> bool:
        """Check if the client is valid."""
        if client is None:
            return False

        try:
            # Check if the connection is established
            server_info = client.server_info()
        except Exception:
            server_info = None

        return bool(server_info)

    @classmethod
    def read_default_user_settings(cls, path: Optional[Path] = None) -> UserSettings:
        """Read default user settings."""
        path = path or cls.USER_SETTINGS_PATH

        if path.exists():
            with path.open(mode="r") as file:
                user_settings_json = file.read()

            user_settings = UserSettings.parse_raw(user_settings_json)
        else:
            user_settings = UserSettings()

        return user_settings

    @classmethod
    def write_default_user_settings(
        cls,
        user_settings: UserSettings,
        path: Optional[Path] = None,
    ) -> None:
        """Write default user settings."""
        path = path or cls.USER_SETTINGS_PATH

        user_settings_json = user_settings.json(
            include=cls.USER_SETTINGS_ALLOWED_FIELD_SET,
            indent=4,
            sort_keys=True,
        )
        with path.open(mode="w") as file:
            file.write(user_settings_json)

    @classmethod
    def update_default(cls, user_settings: UserSettings) -> UserSettings:
        """Update default user settings."""
        d1 = cls.read_default_user_settings().dict()
        d2 = user_settings.dict() if user_settings else {}
        updated = cls.merge_dicts([d1, d2])

        return UserSettings.parse_obj(updated)

    @staticmethod
    def merge_dicts(list_of_dicts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Merge a list of dictionaries."""

        def recursive_merge(d1: Dict, d2: Dict) -> Dict:
            """Recursively merge dict d2 into dict d1 if d2 is value is not None."""
            for k, v in d1.items():
                if k in d2 and all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                    d2[k] = recursive_merge(v, d2[k])

            d3 = d1.copy()
            d3.update((k, v) for k, v in d2.items() if v is not None)
            return d3

        result: Dict[str, Any] = {}
        for d in list_of_dicts:
            result = reduce(recursive_merge, (result, d))
        return result

    def __init__(
        self,
        mongodb_client: Optional[MongoClient] = None,
        access_token_repository: Optional[AbstractAccessTokenRepository] = None,
        user_settings_repository: Optional[AbstractUserSettingsRepository] = None,
        default_user_settings: Optional[UserSettings] = None,
    ):
        valid_client = self.valid_client(client=mongodb_client)

        self._mongodb_client = mongodb_client
        self._token_repository = self.build_token_repository(
            mongodb_client=mongodb_client,
            access_token_repository=access_token_repository,
            valid_client=valid_client,
        )
        self._user_settings_repository = self.build_user_settings_repository(
            mongodb_client=mongodb_client,
            user_settings_repository=user_settings_repository,
            valid_client=valid_client,
        )
        self._default_user_settings = (
            default_user_settings or self.read_default_user_settings()
        )

    @property
    def mongodb_client(self) -> Optional[MongoClient]:
        """Return MongoDB client."""
        return self._mongodb_client

    @property
    def default_user_settings(self) -> UserSettings:
        """Return default user settings."""
        return self._default_user_settings

    @default_user_settings.setter
    def default_user_settings(self, default_user_settings: UserSettings) -> None:
        """Set default user settings."""
        self._default_user_settings = default_user_settings

    @property
    def access_token_repository(self) -> AbstractAccessTokenRepository:
        """Access token repository."""
        return self._token_repository

    @property
    def user_settings_repository(self) -> AbstractUserSettingsRepository:
        """User settings repository."""
        return self._user_settings_repository

    def refresh_default_default_user_settings(self) -> UserSettings:
        """Refresh default default user settings."""
        self._default_user_settings = self.read_default_user_settings()

        return self._default_user_settings
