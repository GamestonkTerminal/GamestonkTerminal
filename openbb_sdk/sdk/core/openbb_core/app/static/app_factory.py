# pylint: disable=W0231:super-init-not-called

from openbb_core.app.command_runner import CommandRunnerSession
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.static.account import Account
from openbb_core.app.static.coverage import Coverage


def create_app():
    try:
        from openbb_core.app.static.package.root import (  # pylint: disable=import-outside-toplevel
            Root,
        )
    except ImportError as e:
        raise Exception(
            "If you are seeing this exception, you should probably be doing: "
            "from openbb_core.app.static.package_builder import PackageBuilder\n"
            "PackageBuilder.build()"
        ) from e

    class App(Root):
        """App class."""

        def __init__(self, command_runner_session):
            self._command_runner_session = command_runner_session
            self._account = Account(self)
            self._coverage = Coverage()

        @property
        def account(self) -> Account:
            return self._account

        @property
        def settings(self) -> UserSettings:
            return self._command_runner_session.user_settings

        @property
        def system(self) -> SystemSettings:
            return self._command_runner_session.command_runner.system_settings

        @property
        def coverage(self) -> Coverage:
            return self._coverage

    return App(command_runner_session=CommandRunnerSession())
