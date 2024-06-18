"""Container class."""

from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, Optional, Tuple

from requests import get

from openbb_core.app.command_runner import CommandRunner
from openbb_core.app.constants import REPOSITORY_URL
from openbb_core.app.model.abstract.error import OpenBBError
from openbb_core.app.model.obbject import OBBject


class Container:
    """Container class for the command runner session."""

    _openbb_providers: Dict[str, str] = {}
    _executor = ThreadPoolExecutor()

    @classmethod
    def _initialize_providers(cls):
        """Fetch providers maintained in OpenBB repository and cache them."""
        try:
            response = get(
                url=f"{REPOSITORY_URL}/main/assets/extensions/provider.json", timeout=5
            )
            if response.status_code == 200:
                result = response.json()
                cls._openbb_providers = {
                    r["packageName"][7:].replace("-", "_"): r["packageName"]
                    for r in result
                }
        except Exception:  # noqa: S110
            pass

    @classmethod
    def initialize_providers(cls):
        """Initialize providers in a background thread."""
        cls._executor.submit(cls._initialize_providers)

    def __init__(self, command_runner: CommandRunner) -> None:
        """Initialize the container."""
        self._command_runner = command_runner
        OBBject._user_settings = command_runner.user_settings
        OBBject._system_settings = command_runner.system_settings

    def _run(self, *args, **kwargs) -> Any:
        """Run a command in the container."""
        obbject = self._command_runner.sync_run(*args, **kwargs)
        output_type = self._command_runner.user_settings.preferences.output_type
        if output_type == "OBBject":
            return obbject
        return getattr(obbject, "to_" + output_type)()

    def _check_credentials(self, provider: str) -> Optional[bool]:
        """Check required credentials are populated."""
        credentials = self._command_runner.user_settings.credentials
        if provider not in credentials.origins:
            return None
        required = credentials.origins.get(provider)
        return all(getattr(credentials, r, None) for r in required)

    def _get_provider(
        self, choice: Optional[str], command: str, default_priority: Tuple[str, ...]
    ) -> str:
        """Get the provider to use in execution.

        If no choice is specified, the configured priority list is used. A provider is used
        when all of its required credentials are populated.

        Parameters
        ----------
        choice: Optional[str]
            The provider choice, for example 'fmp'.
        command: str
            The command to get the provider for, for example 'equity.price.historical'
        default_priority: Tuple[str, ...]
            A tuple of available providers for the given command to use as default priority list.

        Returns
        -------
        str
            The provider to use in the command.

        Raises
        ------
        OpenBBError
            Raises error when all the providers in the priority list failed.
        """
        if choice is None:
            commands = self._command_runner.user_settings.defaults.commands
            providers = (
                commands.get(command, {}).get("provider", []) or default_priority
            )
            tries = []
            for p in providers:
                result = self._check_credentials(p)
                if result:
                    return p
                if result is False:
                    tries.append((p, "missing credentials"))
                elif pkg_name := self._openbb_providers.get(p):
                    tries.append((p, f"not installed, please install {pkg_name}"))
                else:
                    tries.append((p, "not found"))

            msg = "\n  ".join([f"* '{pair[0]}' -> {pair[1]}" for pair in tries])
            raise OpenBBError(f"Provider fallback failed.\n" f"[Providers]\n  {msg}")
        return choice


Container.initialize_providers()
