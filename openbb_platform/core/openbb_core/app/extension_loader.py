"""Extension Loader."""

from enum import Enum
from functools import lru_cache
from typing import Any, Dict

from importlib_metadata import EntryPoints, entry_points

from openbb_core.app.model.abstract.singleton import SingletonMeta
from openbb_core.app.model.extension import Extension

# from openbb_core.app.router import Router
from openbb_core.provider.abstract.provider import Provider

# GroupType = TypeVar("GroupType", Router, Provider, Extension)


class OpenBBGroups(Enum):
    """OpenBB Extension Groups."""

    core = "openbb_core_extension"
    provider = "openbb_provider_extension"
    obbject = "openbb_obbject_extension"


class ExtensionLoader(metaclass=SingletonMeta):
    """Extension loader class."""

    def __init__(
        self,
    ) -> None:
        """Initialize the extension loader."""
        self._obbject_entry_points = self._sorted_entry_points(
            group=OpenBBGroups.obbject.value
        )
        self._core_entry_points = self._sorted_entry_points(
            group=OpenBBGroups.core.value
        )
        self._provider_entry_points = self._sorted_entry_points(
            group=OpenBBGroups.provider.value
        )
        self._obbject_objects: Dict[str, Extension] = {}
        self._core_objects: Dict[str, Any] = {}
        self._provider_objects: Dict[str, Provider] = {}

    @property
    def obbject_entry_points(self) -> EntryPoints:
        """Return a dictionary of obbject extension entry points."""
        return self._obbject_entry_points

    @property
    def core_entry_points(self) -> EntryPoints:
        """Return a dictionary of core extension entry points."""
        return self._core_entry_points

    @property
    def provider_entry_points(self) -> EntryPoints:
        """Return a dictionary of provider extension entry points."""
        return self._provider_entry_points

    @property
    @lru_cache
    def obbject_objects(self) -> Dict[str, Extension]:
        """Return a dict of obbject extension objects."""
        self._obbject_objects = self._load_entry_points(
            self._obbject_entry_points, OpenBBGroups.obbject
        )
        return self._obbject_objects

    @property
    @lru_cache
    def core_objects(self) -> Dict[str, Any]:
        """Return a dict of core extension objects."""
        self._core_objects = self._load_entry_points(
            self._core_entry_points, OpenBBGroups.core
        )
        return self._core_objects

    @property
    @lru_cache
    def provider_objects(self) -> Dict[str, Provider]:
        """Return a dict of provider extension objects."""
        self._provider_objects = self._load_entry_points(
            self._provider_entry_points, OpenBBGroups.provider
        )
        return self._provider_objects

    def _sorted_entry_points(self, group: str) -> EntryPoints:
        """Return a sorted dictionary of entry points."""
        return sorted(entry_points(group=group))  # type: ignore

    def _load_entry_points(
        self, entry_points_: EntryPoints, group: OpenBBGroups
    ) -> Dict[str, Any]:
        """Return a dict of objects matching the entry points."""

        def load_obbject(eps: EntryPoints) -> Dict[str, Extension]:
            """
            Return a dictionary of obbject objects.

            Keys are entry point names and values are instances of the Extension class.
            """
            return {
                ep.name: entry
                for ep in eps
                if isinstance((entry := ep.load()), Extension)
            }

        def load_core(eps: EntryPoints) -> Dict[str, Any]:
            """Return a dictionary of core objects."""
            # TODO : this should filter out using the `Router` class, which causes a circular import error
            # return {
            #     ep.name: entry for ep in eps if isinstance((entry := ep.load()), Router)
            # }
            return {ep.name: ep.load() for ep in eps}

        def load_provider(eps: EntryPoints) -> Dict[str, Provider]:
            """
            Return a dictionary of provider objects.

            Keys are entry point names and values are instances of the Provider class.
            """
            return {
                ep.name: entry
                for ep in eps
                if isinstance((entry := ep.load()), Provider)
            }

        func = {
            OpenBBGroups.obbject: load_obbject,
            OpenBBGroups.core: load_core,
            OpenBBGroups.provider: load_provider,
        }
        return func[group](entry_points_)
