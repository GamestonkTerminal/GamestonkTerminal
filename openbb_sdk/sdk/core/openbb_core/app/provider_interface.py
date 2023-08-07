from dataclasses import dataclass, make_dataclass
from typing import Any, Dict, List, Literal, Optional, Tuple, Type, Union

from fastapi import Query
from openbb_provider.query_executor import QueryExecutor
from openbb_provider.registry_map import MapType, RegistryMap
from pydantic import ConfigDict, BaseModel, Field, create_model
from pydantic.fields import FieldInfo


@dataclass
class DataclassField:
    """Dataclass field."""

    name: str
    type_: Any
    default: Any


@dataclass
class StandardParams:
    """Standard params dataclass."""


@dataclass
class ExtraParams:
    """Extra params dataclass."""


class StandardData(BaseModel):
    """Standard data model."""


class ExtraData(BaseModel):
    """Extra data model."""


@dataclass
class ProviderChoices:
    """Provider choices dataclass."""

    provider: Literal  # type: ignore


class ProviderInterface:
    """Provider interface class. Provides access to 'openbb_provider' package information.

    Properties
    ----------
    map : MapType
        Dictionary of provider information.
    required_credentials: List[str]
        List of required_credentials.
    model_providers : Dict[str, ProviderChoices]
        Dictionary of provider choices by model.
    params : Dict[str, Dict[str, Union[StandardParams, ExtraParams]]]
        Dictionary of params by model.
    return_schema : Dict[str, Type[BaseModel]]
        Dictionary of return data schema by model.
    providers_literal : type
        Literal of provider names.
    provider_choices : ProviderChoices
        Dataclass with literal of provider names.
    models : List[str]
        List of model names.

    Methods
    -------
    create_executor : QueryExecutor
        Create a query executor
    """

    def __init__(
        self,
        registry_map: Optional[RegistryMap] = None,
        query_executor: Optional[QueryExecutor] = None,
    ) -> None:
        """Initialize provider interface."""
        self._registry_map = registry_map or RegistryMap()
        self._query_executor = query_executor or QueryExecutor

        self._map = self._registry_map.map
        # TODO: Try these 4 methods in a single iteration
        self._model_providers_map = self._generate_model_providers_dc(self._map)
        self._params = self._generate_params_dc(self._map)
        self._data = self._generate_data_dc(self._map)
        self._return_schema = self._generate_return_schema(self._data)

        self._providers_literal = self._get_provider_literal(
            self._registry_map.available_providers
        )
        self._provider_choices = self._get_provider_choices(self._providers_literal)

    @property
    def map(self) -> MapType:
        """Dictionary of provider information."""
        return self._map

    @property
    def required_credentials(self) -> List[str]:
        """Dictionary of required credentials by provider."""
        return self._registry_map.required_credentials

    @property
    def model_providers(self) -> Dict[str, ProviderChoices]:
        """Dictionary of provider choices by model."""
        return self._model_providers_map

    @property
    def params(self) -> Dict[str, Dict[str, Union[StandardParams, ExtraParams]]]:
        """Dictionary of params by model."""
        return self._params

    @property
    def data(self) -> Dict[str, Dict[str, Union[StandardData, ExtraData]]]:
        """Dictionary of data by model."""
        return self._data

    @property
    def return_schema(self) -> Dict[str, Type[BaseModel]]:
        """Dictionary of data by model merged."""
        return self._return_schema

    @property
    def providers_literal(self) -> type:
        """Literal of provider names."""
        return self._providers_literal

    @property
    def provider_choices(self) -> type:
        """Dataclass with literal of provider names."""
        return self._provider_choices

    @property
    def models(self) -> List[str]:
        """List of model names."""
        return self._registry_map.models

    @property
    def return_map(self) -> Dict[str, Dict[str, Any]]:
        """Return map."""
        return self._registry_map.return_map

    def create_executor(self) -> QueryExecutor:
        """Get query executor."""
        return self._query_executor(self._registry_map.registry)  # type: ignore

    @staticmethod
    def _merge_fields(
        current: DataclassField, incoming: DataclassField, query: bool = False
    ) -> DataclassField:
        current_name = current.name
        current_type = current.type_
        incoming_type = incoming.type_

        if query:
            merged_default = Query(
                default=current.default.default,
                title=f"{current.default.title}, {incoming.default.title}",
            )
        else:
            merged_default = current.default

        merged_type = (
            Union[current_type, incoming_type]
            if current_type != incoming_type
            else current_type
        )

        return DataclassField(
            name=current_name,
            type_=merged_type,
            default=merged_default,
        )

    @staticmethod
    def _create_field(
        name: str,
        field: FieldInfo,
        provider_name: Optional[str] = None,
        query: bool = False,
        force_optional: bool = False,
    ) -> DataclassField:
        new_name = name.replace(".", "_")
        # field.type_ don't work for nested types
        # field.outer_type_ don't work for Optional nested types
        type_ = field.annotation
        description = field.description

        # if not field.exclude and field.default is None:
        if not field.exclude:
            if force_optional:
                type_ = Optional[type_]  # type: ignore
                default = None
            else:
                default = ...
        else:
            default = field.default

        if query:
            # We need to use query if we want the field description to show up in the
            # swagger, it's a fastapi limitation
            default = Query(
                default=default, title=provider_name, description=description
            )
        elif provider_name:
            default = Field(
                default=default, title=provider_name, description=description
            )

        return DataclassField(new_name, type_, default)

    @classmethod
    def _extract_params(
        cls,
        providers: Any,
    ) -> Tuple[Dict[str, Tuple[str, type, Any]], Dict[str, Tuple[str, type, Any]]]:
        """Extract parameters from map."""
        standard: Dict[str, Tuple[str, Any, Any]] = {}
        extra: Dict[str, Tuple[str, Any, Any]] = {}

        for provider_name, model_details in providers.items():
            for name, field in model_details["QueryParams"]["fields"].items():
                if provider_name == "openbb":
                    incoming = cls._create_field(name, field, query=True)

                    standard[incoming.name] = (
                        incoming.name,
                        incoming.type_,
                        incoming.default,
                    )
                elif name not in providers["openbb"]["QueryParams"]["fields"]:
                    incoming = cls._create_field(
                        name, field, provider_name, query=True, force_optional=True
                    )

                    if incoming.name in extra:
                        current = DataclassField(*extra[incoming.name])
                        updated = cls._merge_fields(current, incoming, query=True)
                    else:
                        updated = incoming

                    if not updated.default.title.startswith("Available for providers:"):
                        updated.default.title = (
                            f"Available for providers: {updated.default.title}"
                        )

                    extra[updated.name] = (
                        updated.name,
                        updated.type_,
                        updated.default,
                    )

        return standard, extra

    @classmethod
    def _extract_data(
        cls,
        providers: Any,
    ) -> Tuple[Dict[str, Tuple[str, type, Any]], Dict[str, Tuple[str, type, Any]]]:
        standard: Dict[str, Tuple[str, Any, Any]] = {}
        extra: Dict[str, Tuple[str, Any, Any]] = {}

        for provider_name, model_details in providers.items():
            for name, field in model_details["Data"]["fields"].items():
                if provider_name == "openbb":
                    incoming = cls._create_field(name, field, "openbb")

                    standard[incoming.name] = (
                        incoming.name,
                        incoming.type_,
                        incoming.default,
                    )
                elif name not in providers["openbb"]["Data"]["fields"]:
                    incoming = cls._create_field(
                        name, field, provider_name, force_optional=True
                    )

                    if incoming.name in extra:
                        current = DataclassField(*extra[incoming.name])
                        updated = cls._merge_fields(current, incoming)
                    else:
                        updated = incoming

                    extra[updated.name] = (
                        updated.name,
                        updated.type_,
                        updated.default,
                    )

        return standard, extra

    def _generate_params_dc(
        self, map_: MapType
    ) -> Dict[str, Dict[str, Union[StandardParams, ExtraParams]]]:
        """Generate dataclasses for params.

        This creates a dictionary of dataclasses that can be injected as a FastAPI
        dependency.

        Example:
        -------
        @dataclass
        class StockNews(StandardParams):
            symbols: str = Query(...)
            page: int = Query(default=1)

        @dataclass
        class StockNews(ExtraParams):
            pageSize: int = Query(default=15, title="benzinga")
            displayOutput: int = Query(default="headline", title="benzinga")
            ...
            sort: str = Query(default=None, title="benzinga, polygon")
        """
        result: Dict = {}

        # TODO: Consider multiprocessing this loop to speed startup
        for model_name, providers in map_.items():
            standard, extra = self._extract_params(providers)

            result[model_name] = {
                "standard": make_dataclass(  # type: ignore
                    cls_name=model_name,
                    fields=list(standard.values()),
                    bases=(StandardParams,),
                ),
                "extra": make_dataclass(  # type: ignore
                    cls_name=model_name,
                    fields=list(extra.values()),
                    bases=(ExtraParams,),
                ),
            }
        return result

    def _generate_model_providers_dc(self, map_: MapType) -> Dict[str, ProviderChoices]:
        """Generate dataclasses for provider choices by model.

        This creates a dictionary that maps model names to dataclasses that can be
        injected as a FastAPI dependency.

        Example:
        -------
        @dataclass
        class StockNews(ProviderChoices):
            provider: Literal["benzinga", "polygon"]
        """
        result: Dict = {}

        for model_name, providers in map_.items():
            choices = list(providers.keys())
            if "openbb" in choices:
                choices.remove("openbb")

            result[model_name] = make_dataclass(  # type: ignore
                cls_name=model_name,
                fields=[("provider", Literal[tuple(choices)])],  # type: ignore
                bases=(ProviderChoices,),
            )

        return result

    def _generate_data_dc(
        self, map_: MapType
    ) -> Dict[str, Dict[str, Union[StandardData, ExtraData]]]:
        """Generate dataclasses for data.

        This creates a dictionary of dataclasses.

        Example:
        -------
        class StockEODData(StandardData):
            date: date
            open: PositiveFloat
            high: PositiveFloat
            low: PositiveFloat
            close: PositiveFloat
            adj_close: Optional[PositiveFloat]
            volume: PositiveFloat
        """
        result: Dict = {}

        for model_name, providers in map_.items():
            standard, extra = self._extract_data(providers)
            result[model_name] = {
                "standard": make_dataclass(  # type: ignore
                    cls_name=model_name,
                    fields=list(standard.values()),
                    bases=(StandardData,),
                ),
                "extra": make_dataclass(  # type: ignore
                    cls_name=model_name,
                    fields=list(extra.values()),
                    bases=(ExtraData,),
                ),
            }

        return result

    def _generate_return_schema(
        self,
        data: Dict[str, Dict[str, Union[StandardData, ExtraData]]],
    ) -> Dict[str, Type[BaseModel]]:
        """Merge standard data with extra data into a single BaseModel to be injected as FastAPI dependency."""
        result: Dict = {}
        for model_name, dataclasses in data.items():
            standard = dataclasses["standard"]
            extra = dataclasses["extra"]

            fields = standard.__fields__.copy()
            fields.update(extra.__fields__)

            fields_dict: Dict[str, Tuple[Any, Any]] = {
                name: (
                    field.annotation,
                    Field(
                        default=field.default,
                        title=field.title,
                        description=field.description,
                    ),
                )
                for name, field in fields.items()
            }

            model_config = ConfigDict(extra="allow")

            result[model_name] = create_model(  # type: ignore
                model_name,
                __config__=model_config,
                **fields_dict,  # type: ignore
            )

        return result

    def _get_provider_literal(self, available_providers: List[str]) -> type:
        return Literal[tuple(available_providers)]  # type: ignore

    def _get_provider_choices(self, providers_literal: type) -> type:
        return make_dataclass(
            cls_name="ProviderChoices",
            fields=[("provider", providers_literal)],
            bases=(ProviderChoices,),
        )


__provider_interface = ProviderInterface()


def get_provider_interface() -> ProviderInterface:
    """Get the provider interface, this only needs to be created once."""
    return __provider_interface
