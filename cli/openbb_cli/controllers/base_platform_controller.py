"""Platform Equity Controller."""

import os
from functools import partial, update_wrapper
from types import MethodType
from typing import Dict, List, Optional

import pandas as pd
from openbb import obb
from openbb_charting.core.openbb_figure import OpenBBFigure
from openbb_cli.argparse_translator.argparse_class_processor import (
    ArgparseClassProcessor,
)
from openbb_cli.config.menu_text import MenuText
from openbb_cli.controllers.base_controller import BaseController
from openbb_cli.controllers.utils import export_data, print_rich_table
from openbb_cli.session import Session
from openbb_core.app.model.obbject import OBBject

session = Session()


class DummyTranslation:
    """Dummy Translation for testing."""

    def __init__(self):
        """Construct a Dummy Translation Class."""
        self.paths = {}
        self.translators = {}


class PlatformController(BaseController):
    """Platform Controller Base class."""

    CHOICES_GENERATION = True

    def __init__(
        self,
        name: str,
        parent_path: List[str],
        platform_target: Optional[type] = None,
        queue: Optional[List[str]] = None,
        translators: Optional[Dict] = None,
    ):
        """Construct a Platform based Controller."""
        self.PATH = f"/{'/'.join(parent_path)}/{name}/" if parent_path else f"/{name}/"
        super().__init__(queue)
        self._name = name

        if not (platform_target or translators):
            raise ValueError("Either platform_target or translators must be provided.")

        self._translated_target = (
            ArgparseClassProcessor(
                target_class=platform_target, reference=obb.reference["paths"]  # type: ignore
            )
            if platform_target
            else DummyTranslation()
        )
        self.translators = (
            translators
            if translators is not None
            else getattr(self._translated_target, "translators", {})
        )
        self.paths = getattr(self._translated_target, "paths", {})

        if self.translators:
            self._link_obbject_to_data_processing_commands()
            self._generate_commands()
            self._generate_sub_controllers()
            self.update_completer(self.choices_default)

    def _link_obbject_to_data_processing_commands(self):
        """Link data processing commands to OBBject registry."""
        for _, trl in self.translators.items():
            for action in trl._parser._actions:  # pylint: disable=protected-access
                if action.dest == "data":
                    action.choices = range(len(session.obbject_registry.obbjects))
                    action.type = int
                    action.nargs = None

    def _intersect_data_processing_commands(self, ns_parser):
        """Intersect data processing commands and change the obbject id into an actual obbject."""
        if hasattr(ns_parser, "data") and ns_parser.data in range(
            len(session.obbject_registry.obbjects)
        ):
            obbject = session.obbject_registry.get(ns_parser.data)
            setattr(ns_parser, "data", obbject.results)

        return ns_parser

    def _generate_sub_controllers(self):
        """Handle paths."""
        for path, value in self.paths.items():
            if value == "path":
                continue

            sub_menu_translators = {}
            choices_commands = []

            for translator_name, translator in self.translators.items():
                if f"{self._name}_{path}" in translator_name:
                    new_name = translator_name.replace(f"{self._name}_{path}_", "")
                    sub_menu_translators[new_name] = translator
                    choices_commands.append(new_name)

                    if translator_name in self.CHOICES_COMMANDS:
                        self.CHOICES_COMMANDS.remove(translator_name)

            # Create the sub controller as a new class
            class_name = f"{self._name.capitalize()}{path.capitalize()}Controller"
            SubController = type(
                class_name,
                (PlatformController,),
                {
                    "CHOICES_GENERATION": True,
                    # "CHOICES_MENUS": [],
                    "CHOICES_COMMANDS": choices_commands,
                },
            )

            self._generate_controller_call(
                controller=SubController,
                name=path,
                parent_path=self.path,
                translators=sub_menu_translators,
            )

    def _generate_commands(self):
        """Generate commands."""
        for name, translator in self.translators.items():
            # Prepare the translator name to create a command call in the controller
            new_name = name.replace(f"{self._name}_", "")

            self._generate_command_call(name=new_name, translator=translator)

    def _generate_command_call(self, name, translator):
        """Generate command call."""

        def method(self, other_args: List[str], translator=translator):
            """Call the translator."""
            parser = translator.parser

            if ns_parser := self.parse_known_args_and_warn(
                parser=parser,
                other_args=other_args,
                export_allowed="raw_data_and_figures",
            ):
                try:
                    ns_parser = self._intersect_data_processing_commands(ns_parser)

                    obbject = translator.execute_func(parsed_args=ns_parser)
                    df: pd.DataFrame = None
                    fig: OpenBBFigure = None
                    title = f"{self.PATH}{translator.func.__name__}"

                    if obbject:
                        max_obbjects_exceeded = (
                            len(session.obbject_registry.obbjects)
                            >= session.settings.N_TO_KEEP_OBBJECT_REGISTRY
                        )
                        if max_obbjects_exceeded:
                            session.obbject_registry.remove()

                        # use the obbject to store the command so we can display it later on results
                        obbject.extra["command"] = f"{title} {' '.join(other_args)}"

                        session.obbject_registry.register(obbject)
                        # we need to force to re-link so that the new obbject
                        # is immediately available for data processing commands
                        self._link_obbject_to_data_processing_commands()
                        # also update the completer
                        self.update_completer(self.choices_default)

                        if session.settings.SHOW_MSG_OBBJECT_REGISTRY and isinstance(
                            obbject, OBBject
                        ):
                            session.console.print("Added OBBject to registry.")

                    if hasattr(ns_parser, "chart") and ns_parser.chart:
                        obbject.show()
                        fig = obbject.chart.fig
                        if hasattr(obbject, "to_dataframe"):
                            df = obbject.to_dataframe()
                        elif isinstance(obbject, dict):
                            df = pd.DataFrame.from_dict(obbject, orient="index")
                        else:
                            df = None

                    elif hasattr(obbject, "to_dataframe"):
                        df = obbject.to_dataframe()
                        if isinstance(df.columns, pd.RangeIndex):
                            df.columns = [str(i) for i in df.columns]
                        print_rich_table(df=df, show_index=True, title=title)

                    elif isinstance(obbject, dict):
                        df = pd.DataFrame.from_dict(obbject, orient="index")
                        print_rich_table(df=df, show_index=True, title=title)

                    elif obbject:
                        session.console.print(obbject)

                    if hasattr(ns_parser, "export") and ns_parser.export:
                        sheet_name = getattr(ns_parser, "sheet_name", None)
                        export_data(
                            export_type=ns_parser.export,
                            dir_path=os.path.dirname(os.path.abspath(__file__)),
                            func_name=translator.func.__name__,
                            df=df,
                            sheet_name=sheet_name,
                            figure=fig,
                        )

                    if max_obbjects_exceeded:
                        session.console.print(
                            "[yellow]\nMaximum number of OBBjects reached. The oldest entry was removed.[yellow]"
                        )

                except Exception as e:
                    session.console.print(f"[red]{e}[/]\n")
                    return

        # Bind the method to the class
        bound_method = MethodType(method, self)

        # Update the wrapper and set the attribute
        bound_method = update_wrapper(  # type: ignore
            partial(bound_method, translator=translator), method
        )
        setattr(self, f"call_{name}", bound_method)

    def _generate_controller_call(self, controller, name, parent_path, translators):
        """Generate controller call."""

        def method(self, _, controller, name, parent_path, translators):
            """Call the controller."""
            self.queue = self.load_class(
                class_ins=controller,
                name=name,
                parent_path=parent_path,
                translators=translators,
                queue=self.queue,
            )

        # Bind the method to the class
        bound_method = MethodType(method, self)

        # Update the wrapper and set the attribute
        bound_method = update_wrapper(  # type: ignore
            partial(
                bound_method,
                name=name,
                parent_path=parent_path,
                translators=translators,
                controller=controller,
            ),
            method,
        )
        setattr(self, f"call_{name}", bound_method)

    def _get_command_description(self, command: str) -> str:
        """Get command description."""
        command_description = (
            obb.reference["paths"]  # type: ignore
            .get(f"{self.PATH}{command}", {})
            .get("description", "")
        )

        if not command_description:
            trl = self.translators.get(
                f"{self._name}_{command}"
            ) or self.translators.get(command)
            if trl and hasattr(trl, "parser"):
                command_description = trl.parser.description

        return command_description.split(".")[0].lower()

    def _get_menu_description(self, menu: str) -> str:
        """Get menu description."""

        def _get_sub_menu_commands():
            """Get sub menu commands."""
            sub_path = f"{self.PATH[1:].replace('/','_')}{menu}"
            commands = []
            for trl in self.translators:
                if sub_path in trl:
                    commands.append(trl.replace(f"{sub_path}_", ""))
            return commands

        menu_description = (
            obb.reference["routers"]  # type: ignore
            .get(f"{self.PATH}{menu}", {})
            .get("description", "")
        ) or ""
        if menu_description:
            return menu_description.split(".")[0].lower()

        # If no description is found, return the sub menu commands
        return ", ".join(_get_sub_menu_commands())

    def print_help(self):
        """Print help."""
        mt = MenuText(self.PATH)

        if self.CHOICES_MENUS:
            for menu in self.CHOICES_MENUS:
                description = self._get_menu_description(menu)
                mt.add_menu(name=menu, description=description)

            if self.CHOICES_COMMANDS:
                mt.add_raw("\n")

        if self.CHOICES_COMMANDS:
            for command in self.CHOICES_COMMANDS:
                command_description = self._get_command_description(command)
                mt.add_cmd(
                    name=command.replace(f"{self._name}_", ""),
                    description=command_description,
                )

        if session.obbject_registry.obbjects:
            mt.add_section("Cached Results:\n", leading_new_line=True)
            for key, value in session.obbject_registry.all.items():
                mt.add_raw(f"\tOBB{key}: {value['command']}\n")

        session.console.print(text=mt.menu_text, menu=self.PATH)

        settings = session.settings
        dev_mode = settings.DEBUG_MODE or settings.TEST_MODE
        if mt.warnings and dev_mode:
            session.console.print("")
            for w in mt.warnings:
                w_str = str(w).replace("{", "").replace("}", "").replace("'", "")
                session.console.print(f"[yellow]{w_str}[/yellow]")
            session.console.print("")
