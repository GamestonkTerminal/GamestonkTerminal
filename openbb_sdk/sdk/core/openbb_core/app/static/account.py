# pylint: disable=W0212:protected-access
import json
from pathlib import Path
from typing import TYPE_CHECKING, Optional

from openbb_core.app.command_runner import CommandRunnerSession
from openbb_core.app.model.hub.hub_session import HubSession
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.service.hub_service import HubService
from openbb_core.app.service.user_service import UserService

if TYPE_CHECKING:
    from openbb_core.app.static.container import Container


class OpenBBError(Exception):
    pass


class Account:
    def __init__(self, app: "Container"):
        self._app = app

    def create_hub_service(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
        sdk_token: Optional[str] = None,
    ) -> HubService:
        if email is None and password is None and sdk_token is None:
            session_file = Path(
                self._app.system.openbb_directory, ".sdk_hub_session.json"
            )
            if not session_file.exists():
                raise OpenBBError("Session not found.")

            with open(session_file) as f:
                session_dict = json.load(f)

            hub_session = HubSession(**session_dict)
            hs = HubService(hub_session)
        else:
            hs = HubService()
            hs.connect(email, password, sdk_token)
        return hs

    def login(
        self,
        email: Optional[str] = None,
        password: Optional[str] = None,
        sdk_token: Optional[str] = None,
        remember_me: bool = False,
    ) -> UserSettings:
        """Login to hub.

        Parameters
        ----------
        email : Optional[str], optional
            Email address, by default None
        password : Optional[str], optional
            Password, by default None
        sdk_token : Optional[str], optional
            SDK token, by default None
        remember_me : bool, optional
            Remember me, by default False

        Returns
        -------
        UserSettings
            User settings: profile, credentials, preferences
        """
        hs = self.create_hub_service(email, password, sdk_token)
        incoming = hs.pull()
        updated = UserService.update_default(incoming)
        self._app._command_runner_session = CommandRunnerSession(user_settings=updated)
        if remember_me:
            Path(self._app.system.openbb_directory).mkdir(parents=False, exist_ok=True)
            session_file = Path(
                self._app.system.openbb_directory, ".sdk_hub_session.json"
            )
            with open(session_file, "w") as f:
                if not hs.session:
                    raise OpenBBError("Not connected to hub.")

                json.dump(hs.session.dict(), f, indent=4)

        return self._app._command_runner_session.user_settings

    def save(self) -> UserSettings:
        """Save user settings.

        Returns
        -------
        UserSettings
            User settings: profile, credentials, preferences
        """
        hub_session = (
            self._app._command_runner_session.user_settings.profile.hub_session
        )
        if not hub_session:
            UserService.write_default_user_settings(
                self._app._command_runner_session.user_settings
            )
        else:
            hs = HubService(hub_session)
            hs.push(self._app._command_runner_session.user_settings)
        return self._app._command_runner_session.user_settings

    def refresh(self) -> UserSettings:
        """Refresh user settings.

        Returns
        -------
        UserSettings
            User settings: profile, credentials, preferences
        """
        hub_session = (
            self._app._command_runner_session.user_settings.profile.hub_session
        )
        if not hub_session:
            self._app._command_runner_session = CommandRunnerSession()
        else:
            hs = HubService(hub_session)
            incoming = hs.pull()
            updated = UserService.update_default(incoming)
            updated.id = self._app._command_runner_session.user_settings.id
            self._app._command_runner_session = CommandRunnerSession(
                user_settings=updated
            )
        return self._app._command_runner_session.user_settings

    def logout(self) -> UserSettings:
        """Logout from hub.

        Returns
        -------
        UserSettings
            User settings: profile, credentials, preferences
        """
        hub_session = (
            self._app._command_runner_session.user_settings.profile.hub_session
        )
        if not hub_session:
            raise OpenBBError("Not connected to hub.")

        hs = HubService(hub_session)
        hs.disconnect()

        session_file = Path(self._app.system.openbb_directory, ".sdk_hub_session.json")
        if session_file.exists():
            session_file.unlink()

        self._app._command_runner_session = CommandRunnerSession()
        return self._app._command_runner_session.user_settings
