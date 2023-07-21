import inspect
import multiprocessing
import warnings
from contextlib import nullcontext
from copy import deepcopy
from datetime import datetime
from inspect import Parameter, signature
from time import perf_counter_ns
from typing import (
    Any,
    Callable,
    ContextManager,
    Dict,
    List,
    Optional,
    Tuple,
    Union,
)

from pydantic import BaseConfig, Extra, create_model

from openbb_core.app.charting_manager import ChartingManager
from openbb_core.app.logs.logging_manager import LoggingManager
from openbb_core.app.model.abstract.warning import cast_warning
from openbb_core.app.model.charts.chart import Chart
from openbb_core.app.model.command_context import CommandContext
from openbb_core.app.model.command_output import CommandOutput, Error
from openbb_core.app.model.journal import Journal
from openbb_core.app.model.journal_entry import JournalEntry
from openbb_core.app.model.journal_query import JournalQuery
from openbb_core.app.model.system_settings import SystemSettings
from openbb_core.app.model.user_settings import UserSettings
from openbb_core.app.router import CommandMap
from openbb_core.app.service.journal_service import JournalService
from openbb_core.app.service.system_service import SystemService
from openbb_core.app.service.user_service import UserService


class ExecutionContext:
    def __init__(
        self,
        command_map: CommandMap,
        route: str,
        system_settings: SystemSettings,
        user_settings: UserSettings,
        journal: Optional[Journal] = None,
        journal_service: Optional[JournalService] = None,
    ) -> None:
        self.command_map = command_map
        self.journal = journal or Journal()
        self.route = route
        self.system_settings = system_settings
        self.journal_service = journal_service or JournalService()
        self.user_settings = user_settings


class ParametersBuilder:
    @staticmethod
    def get_polished_parameter_list(func: Callable) -> List[Parameter]:
        sig = signature(func)
        parameter_list = list(sig.parameters.values())

        return parameter_list

    @staticmethod
    def get_polished_func(func: Callable) -> Callable:
        func = deepcopy(func)
        sig = signature(func)
        parameter_map = dict(sig.parameters)

        if "__authenticated_user_settings" in parameter_map:
            parameter_map.pop("__authenticated_user_settings")

        parameter_list = list(parameter_map.values())
        new_signature = signature(func).replace(parameters=parameter_list)

        func.__signature__ = new_signature  # type: ignore
        func.__annotations__ = parameter_map

        return func

    @classmethod
    def merge_args_and_kwargs(
        cls,
        func: Callable,
        args: Tuple[Any],
        kwargs: Dict[str, Any],
    ) -> Dict[str, Any]:
        args = deepcopy(args)
        kwargs = deepcopy(kwargs)
        parameter_list = cls.get_polished_parameter_list(func=func)
        parameter_map = {}

        for index, parameter in enumerate(parameter_list):
            if index < len(args):
                parameter_map[parameter.name] = args[index]
            elif parameter.name in kwargs:
                parameter_map[parameter.name] = kwargs[parameter.name]
            elif parameter.default is not parameter.empty:
                parameter_map[parameter.name] = parameter.default
            else:
                parameter_map[parameter.name] = None

        return parameter_map

    @classmethod
    def update_journal_query(
        cls,
        kwargs: Dict[str, Any],
        journal: Journal,
        journal_service: JournalService,
    ) -> Dict[str, Any]:
        for parameter_name, parameter_value in kwargs.items():
            if isinstance(parameter_value, JournalQuery):
                journal_query = parameter_value
                journal_entry_id = journal_query.journal_entry_id

                journal_entry = journal_service.journal_entry_repository.read(
                    filter_list=[("_id", journal_entry_id)],
                )

                if journal_entry and journal_entry.journal_id == journal.id:
                    kwargs[parameter_name] = journal_entry.output.results
                else:
                    raise AttributeError(
                        f"Cannot find JournalEntry for the JournalQuery: {journal_query}.\n"
                        f"parameter_name  = {parameter_name}\n"
                        f"parameter_value = {parameter_value}\n"
                    )

        return kwargs

    @staticmethod
    def update_command_context(
        func: Callable,
        kwargs: Dict[str, Any],
        system_settings: SystemSettings,
        user_settings: UserSettings,
    ) -> Dict[str, Any]:
        argcount = func.__code__.co_argcount
        if "cc" in func.__code__.co_varnames[:argcount]:
            kwargs["cc"] = CommandContext(
                user_settings=user_settings,
                system_settings=system_settings,
            )

        return kwargs

    @staticmethod
    def update_provider_choices(
        command_map: CommandMap,
        route: str,
        kwargs: Dict[str, Any],
        user_settings: UserSettings,
    ) -> Dict[str, Any]:
        provider_choices = kwargs.get("provider_choices", None)
        if provider_choices and isinstance(provider_choices, dict):
            provider = provider_choices.get("provider", None)
            if provider is None:
                route_defaults = user_settings.defaults.routes.get(route, None)
                random_choice = command_map.command_coverage[route][0]
                provider = (
                    random_choice
                    if route_defaults is None
                    or route_defaults.get("provider", None) is None
                    else route_defaults.get("provider", random_choice)
                )
                kwargs["provider_choices"] = {"provider": provider}
        return kwargs

    @classmethod
    def validate_kwargs(
        cls,
        func: Callable,
        kwargs: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Validate kwargs and if possible coerce to the correct type"""

        class Config(BaseConfig):
            arbitrary_types_allowed = True
            extra = Extra.allow

        sig = inspect.signature(func)
        fields = {
            n: (
                p.annotation,
                ... if p.default is Parameter.empty else p.default,
            )
            for n, p in sig.parameters.items()
        }
        ValidationModel = create_model(func.__name__, __config__=Config, **fields)  # type: ignore
        model = ValidationModel(**kwargs)
        result = dict(model)

        return result

    @classmethod
    def build(
        cls,
        args: Tuple[Any],
        execution_context: ExecutionContext,
        func: Callable,
        route: str,
        kwargs: Dict[str, Any],
    ) -> Dict[str, Any]:
        func = cls.get_polished_func(func=func)
        journal = execution_context.journal
        system_settings = execution_context.system_settings
        user_settings = execution_context.user_settings
        journal_service = execution_context.journal_service
        command_map = execution_context.command_map

        kwargs = cls.merge_args_and_kwargs(
            func=func,
            args=args,
            kwargs=kwargs,
        )
        kwargs = cls.update_journal_query(
            kwargs=kwargs,
            journal=journal,
            journal_service=journal_service,
        )
        kwargs = cls.update_command_context(
            func=func,
            kwargs=kwargs,
            system_settings=system_settings,
            user_settings=user_settings,
        )
        kwargs = cls.update_provider_choices(
            command_map=command_map,
            route=route,
            kwargs=kwargs,
            user_settings=user_settings,
        )
        kwargs = cls.validate_kwargs(func=func, kwargs=kwargs)
        return kwargs


class StaticCommandRunner:
    logging_manager = LoggingManager()
    charting_manager = ChartingManager()

    @staticmethod
    def __run_in_isolation(func, args=None, kwargs=None) -> CommandOutput:
        args = args or ()
        kwargs = kwargs or {}

        with multiprocessing.Pool(processes=1) as pool:
            result = pool.apply(func=func, args=args, kwds=kwargs)

        return result

    @classmethod
    def __execute(
        cls, system_settings: SystemSettings, func: Callable, kwargs: Dict[str, Any]
    ) -> CommandOutput:
        try:
            context_manager: Union[warnings.catch_warnings, ContextManager[None]] = (
                warnings.catch_warnings(record=True)
                if not system_settings.debug_mode
                else nullcontext()
            )

            with context_manager as warning_list:
                if system_settings.run_in_isolation:
                    command_output = cls.__run_in_isolation(func=func, kwargs=kwargs)
                else:
                    command_output = func(**kwargs)

                command_output.provider = getattr(
                    kwargs.get("provider_choices", None), "provider", None
                )

                if warning_list:
                    command_output.warnings = list(map(cast_warning, warning_list))

        except Exception as e:
            command_output = CommandOutput(
                error=Error(message=str(e), error_kind=e.__class__.__name__)
            )
            if system_settings.debug_mode:
                raise

        return command_output

    @classmethod
    def __chart(
        cls,
        command_output: CommandOutput,
        user_settings: UserSettings,
        system_settings: SystemSettings,
        route: str,
        **kwargs,
    ) -> None:
        try:
            command_output.chart = cls.charting_manager.chart(
                user_settings=user_settings,
                system_settings=system_settings,
                route=route,
                command_output_item=command_output.results,
                **kwargs,
            )
        except Exception as e:
            command_output.chart = Chart(error=Error(message=str(e)))
            if system_settings.debug_mode:
                raise

    @classmethod
    def __execute_func(
        cls,
        route: str,
        args: Tuple[Any],
        execution_context: ExecutionContext,
        func: Callable,
        kwargs: Dict[str, Any],
    ) -> CommandOutput:
        user_settings = execution_context.user_settings
        system_settings = execution_context.system_settings

        # If we're on Jupyter we need to pop here because we will lose "chart" after
        # ParametersBuilder.build. This needs to be fixed in a way that chart is not
        # is added to the function signature and shared for jupyter and api
        # We can check in the router decorator if the given function has a chart
        # in the charting extension then we add it there. This way we can remove
        # the chart parameter from the commands.py and packagebuilder, it will be
        # added to the function signature in the router decorator
        chart = kwargs.pop("chart", False)

        kwargs = ParametersBuilder.build(
            args=args,
            execution_context=execution_context,
            func=func,
            route=route,
            kwargs=kwargs,
        )

        # If we're on the api we need to remove "chart" here because the parameter is added on
        # commands.py and the function signature does not expect "chart"
        kwargs.pop("chart", None)

        command_output = cls.__execute(
            system_settings=system_settings,
            func=func,
            kwargs=kwargs,
        )

        if chart and command_output.results:
            cls.__chart(
                command_output=command_output,
                user_settings=user_settings,
                system_settings=system_settings,
                route=route,
                **kwargs,
            )

        cls.logging_manager.log(
            user_settings=user_settings,
            system_settings=system_settings,
            command_output=command_output,
            route=route,
            func=func,
            kwargs=kwargs,
        )

        return command_output

    @classmethod
    def __update_managers_settings(
        cls, system_settings: SystemSettings, user_settings: UserSettings
    ):
        cls.logging_manager.logging_settings = (system_settings, user_settings)
        cls.charting_manager.charting_settings = (system_settings, user_settings)

    @classmethod
    def run(
        cls,
        execution_context: ExecutionContext,
        /,
        *args,
        **kwargs,
    ) -> JournalEntry:
        timestamp = datetime.now()
        start_ns = perf_counter_ns()

        command_map = execution_context.command_map
        journal = execution_context.journal
        route = execution_context.route
        journal_service = execution_context.journal_service

        cls.__update_managers_settings(
            execution_context.system_settings, execution_context.user_settings
        )

        func = command_map.get_command(route=route)

        if func:
            command_output = cls.__execute_func(
                route=route,
                args=args,  # type: ignore
                execution_context=execution_context,
                func=func,
                kwargs=kwargs,
            )
        else:
            raise AttributeError(f"Invalid command : route={route}")

        duration = perf_counter_ns() - start_ns

        journal_entry = JournalEntry(
            journal_id=journal.id,
            arguments=kwargs,
            duration=duration,
            output=command_output,
            route=route,
            timestamp=timestamp,
        )

        journal_service.journal_entry_repository.create(model=journal_entry)

        return journal_entry


class CommandRunner:
    def __init__(
        self,
        command_map: Optional[CommandMap] = None,
        system_settings: Optional[SystemSettings] = None,
        journal_service: Optional[JournalService] = None,
    ) -> None:
        self._command_map = command_map or CommandMap()
        self._system_settings = (
            system_settings or SystemService.read_default_system_settings()
        )
        self._journal_service = journal_service or JournalService()

    @property
    def command_map(self) -> CommandMap:
        return self._command_map

    @property
    def system_settings(self) -> SystemSettings:
        return self._system_settings

    @property
    def journal_service(self) -> JournalService:
        return self._journal_service

    def run(
        self,
        journal: Journal,
        user_settings: UserSettings,
        route: str,
        /,
        *args,
        **kwargs,
    ) -> JournalEntry:
        command_map = self._command_map
        # Getting the most updated system settings to allow debug_mode without reload
        system_settings = self._system_settings
        journal_service = self._journal_service

        execution_context = ExecutionContext(
            command_map=command_map,
            journal=journal,
            route=route,
            system_settings=system_settings,
            journal_service=journal_service,
            user_settings=user_settings,
        )

        journal_entry = StaticCommandRunner.run(
            execution_context,
            *args,
            **kwargs,
        )

        return journal_entry

    def run_once(
        self,
        user_settings: UserSettings,
        route: str,
        /,
        *args,
        **kwargs,
    ) -> JournalEntry:
        command_map = self._command_map
        system_settings = self._system_settings

        execution_context = ExecutionContext(
            command_map=command_map,
            route=route,
            system_settings=system_settings,
            user_settings=user_settings,
        )

        journal_entry = StaticCommandRunner.run(
            execution_context,
            *args,
            **kwargs,
        )

        return journal_entry


class CommandRunnerSession:
    def __init__(
        self,
        command_runner: Optional[CommandRunner] = None,
        journal: Optional[Journal] = None,
        user_settings: Optional[UserSettings] = None,
    ) -> None:
        self._command_runner = command_runner or CommandRunner()
        self._journal = journal or Journal()
        self._user_settings = user_settings or UserService.read_default_user_settings()

    @property
    def command_runner(self) -> CommandRunner:
        return self._command_runner

    @command_runner.setter
    def command_runner(self, command_runner: CommandRunner) -> None:
        self._command_runner = command_runner

    @property
    def journal(self) -> Journal:
        return self._journal

    @journal.setter
    def journal(self, journal: Journal) -> None:
        self._journal = journal

    @property
    def user_settings(self) -> UserSettings:
        return self._user_settings

    @user_settings.setter
    def user_settings(self, user_settings: UserSettings) -> None:
        self._user_settings = user_settings

    def run(self, route: str, /, *args, **kwargs) -> JournalEntry:
        command_runner = self._command_runner
        journal = self._journal
        user_settings = self._user_settings

        journal_entry = command_runner.run(
            journal,
            user_settings,
            route,
            *args,
            **kwargs,
        )

        return journal_entry
