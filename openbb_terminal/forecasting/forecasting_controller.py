"""Forecasting Controller Module"""
__docformat__ = "numpy"

# pylint: disable=too-many-lines, too-many-branches, inconsistent-return-statements

import argparse
import logging
from itertools import chain
import os
from pathlib import Path
from typing import List, Dict, Any

import torch
import pandas as pd
from prompt_toolkit.completion import NestedCompleter

from openbb_terminal import feature_flags as obbff
from openbb_terminal.decorators import log_start_end
from openbb_terminal.helper_funcs import (
    check_positive,
    check_positive_float,
    NO_EXPORT,
    EXPORT_ONLY_FIGURES_ALLOWED,
    EXPORT_ONLY_RAW_DATA_ALLOWED,
    export_data,
    log_and_raise,
)
from openbb_terminal.helper_funcs import (
    print_rich_table,
    check_list_values,
)
from openbb_terminal.menu import session
from openbb_terminal.parent_classes import BaseController
from openbb_terminal.rich_config import console, MenuText
from openbb_terminal.forecasting import (
    TCN_view,
    forecasting_model,
    forecasting_view,
    expo_model,
    expo_view,
    theta_model,
    theta_view,
    rnn_view,
    NBEATS_view,
    brnn_view,
    linear_regression_view,
    regression_view,
    tft_view,
)

logger = logging.getLogger(__name__)

# pylint: disable=R0902


def check_greater_than_one(value) -> int:
    """Argparse type to check positive int above 1"""
    new_value = int(value)
    if new_value <= 1:
        log_and_raise(
            argparse.ArgumentTypeError(
                f"{value} is an invalid positive int value. Must be greater than 1."
            )
        )
    return new_value


# setting device on GPU if available, else CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
console.print(f"[green]Using device: {device} [/green]")


class ForecastingController(BaseController):
    """Forecasting class"""

    CHOICES_COMMANDS: List[str] = [
        "load",
        "show",
        "plot",
        "clean",
        "combine",
        "delete",
        "export",
        "ema",
        "sto",
        "rsi",
        "roc",
        "mom",
        "expo",
        "theta",
        "rnn",
        "brnn",
        "nbeats",
        "tcn",
        "regr",
        "linregr",
        "trans",
        "tft",
    ]
    # CHOICES_MENUS: List[str] = ["qa", "pred"]
    pandas_plot_choices = [
        "line",
        "scatter",
        "bar",
        "barh",
        "hist",
        "box",
        "kde",
        "area",
        "pie",
        "hexbin",
    ]
    PATH = "/forecasting/"

    loaded_dataset_cols = "\n"
    list_dataset_cols: List = list()

    def __init__(self, queue: List[str] = None):
        """Constructor"""
        super().__init__(queue)
        self.files: List[str] = list()
        self.datasets: Dict[str, pd.DataFrame] = dict()

        self.DATA_TYPES: List[str] = ["int", "float", "str", "bool", "category", "date"]

        self.signs: Dict[Any, Any] = {
            "div": "/",
            "mul": "*",
            "add": "+",
            "sub": "-",
            "mod": "%",
            "pow": "**",
        }
        self.file_types = ["csv", "xlsx"]
        self.DATA_FILES = {
            filepath.name: filepath
            for file_type in self.file_types
            for filepath in chain(
                Path(obbff.EXPORT_FOLDER_PATH).rglob(f"*.{file_type}"),
                Path("custom_imports").rglob(f"*.{file_type}"),
            )
            if filepath.is_file()
        }

        if session and obbff.USE_PROMPT_TOOLKIT:
            choices: dict = {c: {} for c in self.controller_choices}
            choices["load"] = {c: None for c in self.DATA_FILES.keys()}
            choices["show"] = {c: None for c in self.files}

            for feature in ["export", "show"]:
                choices[feature] = {c: None for c in self.files}

            for feature in ["plot"]:
                choices[feature] = dict()

            self.choices = choices

            # To link to the support HTML
            choices["support"] = self.SUPPORT_CHOICES

            self.completer = NestedCompleter.from_nested_dict(choices)

    def update_runtime_choices(self):
        if session and obbff.USE_PROMPT_TOOLKIT:
            dataset_columns = {
                f"{dataset}.{column}": {column: None, dataset: None}
                for dataset, dataframe in self.datasets.items()
                for column in dataframe.columns
            }

            for feature in [
                "plot",
                "delete",
            ]:
                self.choices[feature] = dataset_columns

            for feature in [
                "export",
                "show",
                "clean",
                "ema",
                "sto",
                "rsi",
                "roc",
                "mom",
                # "index",
                # "remove",
                "combine",
                # "rename",
                "expo",
                "theta",
                "rnn",
                "brnn",
                "nbeats",
                "tcn",
                "regr",
                "linregr",
                "trans",
                "tft",
            ]:
                self.choices[feature] = {c: None for c in self.files}

            # self.choices["type"] = {
            #     c: None for c in self.files + list(dataset_columns.keys())
            # }
            # self.choices["desc"] = {
            #     c: None for c in self.files + list(dataset_columns.keys())
            # }

            pairs_timeseries = list()
            for dataset_col in list(dataset_columns.keys()):
                pairs_timeseries += [
                    f"{dataset_col},{dataset_col2}"
                    for dataset_col2 in list(dataset_columns.keys())
                    if dataset_col != dataset_col2
                ]

            self.completer = NestedCompleter.from_nested_dict(self.choices)

    def print_help(self):
        """Print help"""
        mt = MenuText("forecasting/")
        mt.add_param(
            "_data_loc",
            f"\n\t{obbff.EXPORT_FOLDER_PATH}\n\t{Path('custom_imports').resolve()}",
        )
        mt.add_raw("\n")
        mt.add_cmd("load")
        mt.add_raw("\n")
        mt.add_param("_loaded", self.loaded_dataset_cols)
        mt.add_info("_exploration_")
        mt.add_cmd("show", "", self.files)
        mt.add_cmd("plot", "", self.files)
        mt.add_cmd("clean", "", self.files)
        mt.add_cmd("combine", "", self.files)
        mt.add_cmd("delete", "", self.files)
        mt.add_cmd("export", "", self.files)
        mt.add_info("_feateng_")
        mt.add_cmd("ema", "", self.files)
        mt.add_cmd("sto", "", self.files)
        mt.add_cmd("rsi", "", self.files)
        mt.add_cmd("roc", "", self.files)
        mt.add_cmd("mom", "", self.files)
        mt.add_info("_tsforecasting_")
        mt.add_cmd("expo", "", self.files)
        mt.add_cmd("theta", "", self.files)
        mt.add_cmd("linregr", "", self.files)
        mt.add_cmd("regr", "", self.files)
        mt.add_cmd("rnn", "", self.files)
        mt.add_cmd("brnn", "", self.files)
        mt.add_cmd("nbeats", "", self.files)
        mt.add_cmd("tcn", "", self.files)
        mt.add_cmd("tft", "", self.files)
        mt.add_info("_comingsoon_")
        mt.add_cmd("trans", "", self.files)

        console.print(text=mt.menu_text, menu="Forecasting")

    def custom_reset(self):
        """Class specific component of reset command"""
        if self.files:
            load_files = [f"load {file}" for file in self.files]
            return ["forecasting"] + load_files
        return []

    @log_start_end(log=logger)
    def call_load(self, other_args: List[str]):
        """Process load"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="load",
            description="Load custom dataset (from previous export, custom imports).",
        )
        parser.add_argument(
            "-f",
            "--file",
            help="File to load data in (can be custom import, may have been exported before.)",
            type=str,
        )
        parser.add_argument(
            "-a",
            "--alias",
            help="Alias name to give to the dataset",
            type=str,
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-f")
        ns_parser = self.parse_known_args_and_warn(parser, other_args)

        if ns_parser:
            if ns_parser.file:
                file = ns_parser.file
                if ns_parser.alias:
                    alias = ns_parser.alias
                else:
                    if "." in ns_parser.file:
                        alias = ".".join(ns_parser.file.split(".")[:-1])
                    else:
                        alias = ns_parser.file

                # check if this dataset has been added already
                if alias in self.files:
                    console.print(
                        "[red]The file/dataset selected has already been loaded.[/red]\n"
                    )
                    return

                data = forecasting_model.load(file, self.file_types, self.DATA_FILES)

                if not data.empty:
                    data.columns = data.columns.map(
                        lambda x: x.lower().replace(" ", "_")
                    )

                    self.files.append(alias)
                    self.datasets[alias] = data

                    self.update_runtime_choices()

                    # Process new datasets to be updated
                    self.list_dataset_cols = list()
                    maxfile = max(len(file) for file in self.files)
                    self.loaded_dataset_cols = "\n"
                    for dataset, data in self.datasets.items():
                        self.loaded_dataset_cols += (
                            f"  {dataset} {(maxfile - len(dataset)) * ' '}: "
                            f"{', '.join(data.columns)}\n"
                        )

                        for col in data.columns:
                            self.list_dataset_cols.append(f"{dataset}.{col}")

                    console.print()

    # Show selected dataframe on console
    @log_start_end(log=logger)
    def call_show(self, other_args: List[str]):
        """Process show command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="show",
            description="Show a portion of the DataFrame",
        )
        parser.add_argument(
            "-n",
            "--name",
            type=str,
            choices=self.files,
            dest="name",
            help="The name of the database you want to show data for",
        )
        parser.add_argument(
            "-s",
            "--sortcol",
            help="Sort based on a column in the DataFrame",
            nargs="+",
            type=str,
            dest="sortcol",
            default="",
        )
        parser.add_argument(
            "-a",
            "--ascend",
            help="Use this argument to sort in a descending order",
            action="store_true",
            default=False,
            dest="ascend",
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-n")
        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, EXPORT_ONLY_RAW_DATA_ALLOWED, limit=10
        )

        if ns_parser:
            if not ns_parser.name:
                dataset_names = list(self.datasets.keys())
            else:
                dataset_names = [ns_parser.name]

            for name in dataset_names:
                df = self.datasets[name]

                if name in self.datasets and self.datasets[name].empty:
                    return console.print(
                        f"[red]No data available for {ns_parser.name}.[/red]\n"
                    )
                if ns_parser.sortcol:
                    sort_column = " ".join(ns_parser.sortcol)
                    if sort_column not in self.datasets[name].columns:
                        console.print(
                            f"[red]{sort_column} not a valid column. Showing without sorting.\n[/red]"
                        )
                    else:
                        df = df.sort_values(by=sort_column, ascending=ns_parser.ascend)

                # print shape of dataframe
                console.print(
                    f"[green]{name} has following shape (rowxcolumn): {df.shape}[/green]"
                )
                print_rich_table(
                    df.head(ns_parser.limit),
                    headers=list(df.columns),
                    show_index=True,
                    title=f"Dataset {name} | Showing {ns_parser.limit} of {len(df)} rows",
                )

                export_data(
                    ns_parser.export,
                    os.path.dirname(os.path.abspath(__file__)),
                    f"{ns_parser.name}_show",
                    df.head(ns_parser.limit),
                )

    @log_start_end(log=logger)
    def call_plot(self, other_args: List[str]):
        """Process plot command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="plot",
            description="Plot data based on the index",
        )
        parser.add_argument(
            "-v",
            "--values",
            help="Dataset.column values to be displayed in a plot",
            dest="values",
            type=check_list_values(self.choices["plot"]),
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-v")
        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser and ns_parser.values:
            data: Dict = {}
            for datasetcol in ns_parser.values:
                dataset, col = datasetcol.split(".")
                data[datasetcol] = self.datasets[dataset][col]

            forecasting_view.display_plot(
                data,
                ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_combine(self, other_args: List[str]):
        """Process combine"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="combine",
            description="The columns you want to add to a dataset. The first argument is the dataset to add columns in"
            "and the remaining could be: <datasetX.column2>,<datasetY.column3>",
        )
        parser.add_argument(
            "-d",
            "--dataset",
            help="Dataset to add columns to",
            dest="dataset",
            choices=self.choices["combine"],
        )
        parser.add_argument(
            "-c",
            "--columns",
            help="The columns we want to add <dataset.column>,<datasetb.column2>",
            dest="columns",
            type=check_list_values(self.choices["delete"]),
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-d")
        ns_parser = self.parse_known_args_and_warn(parser, other_args, NO_EXPORT)

        if ns_parser:
            if ns_parser.dataset not in self.datasets:
                console.print(
                    f"Not able to find the dataset {ns_parser.dataset}. Please choose one of "
                    f"the following: {', '.join(self.datasets)}"
                )
                return

            data = self.datasets[ns_parser.dataset]

            for option in ns_parser.columns:
                dataset, column = option.split(".")

                if dataset not in self.datasets:
                    console.print(
                        f"Not able to find the dataset {dataset}. Please choose one of "
                        f"the following: {', '.join(self.datasets)}"
                    )
                elif column not in self.datasets[dataset]:
                    console.print(
                        f"Not able to find the column {column}. Please choose one of "
                        f"the following: {', '.join(self.datasets[dataset].columns)}"
                    )
                else:
                    data[f"{dataset}_{column}"] = self.datasets[dataset][column]

            self.update_runtime_choices()
        console.print()

    @log_start_end(log=logger)
    def call_clean(self, other_args: List[str]):
        """Process clean"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="clean",
            description="Clean a dataset by filling and dropping NaN values.",
        )
        parser.add_argument(
            "-n",
            "--name",
            help="The name of the dataset you want to clean up",
            dest="name",
            type=str,
            choices=list(self.datasets.keys()),
        )
        parser.add_argument(
            "-f",
            "--fill",
            help="The method of filling NaNs. This has options to fill rows (rfill, rbfill, rffill) or fill "
            "columns (cfill, cbfill, cffill). Furthermore, it has the option to forward fill and backward fill "
            "(up to --limit) which refer to how many rows/columns can be set equal to the last non-NaN value",
            dest="fill",
            choices=["rfill", "cfill", "rbfill", "cbfill", "rffill", "bffill"],
            default="",
        )
        parser.add_argument(
            "-d",
            "--drop",
            help="The method of dropping NaNs. This either has the option rdrop (drop rows that contain NaNs) "
            "or cdrop (drop columns that contain NaNs)",
            dest="drop",
            choices=["rdrop", "cdrop"],
            default="",
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-n")
        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, NO_EXPORT, limit=5
        )
        if ns_parser:
            console.print(
                f"[green] {ns_parser.name} original shape (rowxcolumn) = {self.datasets[ns_parser.name].shape}"
            )
            self.datasets[ns_parser.name], clean_status = forecasting_model.clean(
                self.datasets[ns_parser.name],
                ns_parser.fill,
                ns_parser.drop,
                ns_parser.limit,
            )
            if not clean_status:
                console.print(
                    f"[green] Successfully cleaned '{ns_parser.name}' dataset[/green]"
                )
                console.print()
                console.print(
                    f"[green] {ns_parser.name} new shape after cleaning \
                        (rowxcolumn) = {self.datasets[ns_parser.name].shape}"
                )
            else:
                console.print(f"[red]{ns_parser.name} still contains NaNs.[/red]")

        console.print()

    @log_start_end(log=logger)
    def call_ema(self, other_args: List[str]):
        """Process EMA"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="ema",
            description="Add exponential moving average to dataset based on specific column.",
        )
        parser.add_argument(
            "--target-dataset",
            help="The name of the dataset you want to add the EMA to",
            dest="target_dataset",
            type=str,
            choices=list(self.datasets.keys()),
        )
        parser.add_argument(
            "--target-column",
            help="The name of the specific column you want to calculate EMA for.",
            dest="target_column",
            type=str,
            default="close",
        )

        parser.add_argument(
            "--period",
            help="The period to calculate EMA with.",
            dest="period",
            type=check_greater_than_one,
            default=10,
        )
        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, NO_EXPORT, limit=5
        )
        if ns_parser:
            self.datasets[ns_parser.target_dataset] = forecasting_model.add_ema(
                self.datasets[ns_parser.target_dataset],
                ns_parser.target_column,
                ns_parser.period,
            )
            console.print(
                f"Successfully added 'EMA_{ns_parser.period}' to '{ns_parser.target_dataset}' dataset"
            )
        console.print()

    @log_start_end(log=logger)
    def call_sto(self, other_args: List[str]):
        """Process Stoch Oscill"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="sto",
            description="Add in Stochastic Oscillator %K and %D",
        )
        parser.add_argument(
            "--target-dataset",
            help="The name of the dataset to use.",
            dest="target_dataset",
            type=str,
            choices=list(self.datasets.keys()),
        )
        parser.add_argument(
            "--period",
            help="The name of the specific column you want to calculate STO for.",
            dest="period",
            type=check_greater_than_one,
            default=10,
        )
        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, NO_EXPORT, limit=5
        )
        if ns_parser:
            self.datasets[ns_parser.target_dataset] = forecasting_model.add_sto(
                self.datasets[ns_parser.target_dataset],
                ns_parser.period,
            )
            console.print(
                f"Successfully added 'STOK&D_{ns_parser.period}' to '{ns_parser.target_dataset}' dataset"
            )
        console.print()

    @log_start_end(log=logger)
    def call_delete(self, other_args: List[str]):
        """Process add"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="delete",
            description="The column you want to delete from a dataset.",
        )
        parser.add_argument(
            "-d",
            "--delete",
            help="The columns you want to delete from a dataset. Use format: <dataset.column> or"
            " multiple with <dataset.column>,<datasetb.column2>",
            dest="delete",
            type=check_list_values(self.choices["delete"]),
        )
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-d")
        ns_parser = self.parse_known_args_and_warn(parser, other_args, NO_EXPORT)

        if ns_parser:
            for option in ns_parser.delete:
                dataset, column = option.split(".")

                if dataset not in self.datasets:
                    console.print(
                        f"Not able to find the dataset {dataset}. Please choose one of "
                        f"the following: {', '.join(self.datasets)}"
                    )
                elif column not in self.datasets[dataset]:
                    console.print(
                        f"Not able to find the column {column}. Please choose one of "
                        f"the following: {', '.join(self.datasets[dataset].columns)}"
                    )
                else:
                    del self.datasets[dataset][column]

            self.update_runtime_choices()
        console.print()

    @log_start_end(log=logger)
    def call_rsi(self, other_args: List[str]):
        """Process RSI"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="rsi",
            description="Add rsi to dataset based on specific column.",
        )
        parser.add_argument(
            "--target-dataset",
            help="The name of the dataset you want to add the RSI to",
            dest="target_dataset",
            type=str,
            choices=list(self.datasets.keys()),
        )
        parser.add_argument(
            "--target-column",
            help="The name of the specific column you want to calculate RSI for.",
            dest="target_column",
            type=str,
            default="close",
        )

        parser.add_argument(
            "--period",
            help="The period to calculate RSI with.",
            dest="period",
            type=check_greater_than_one,
            default=10,
        )
        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, NO_EXPORT, limit=5
        )
        if ns_parser:
            self.datasets[ns_parser.target_dataset] = forecasting_model.add_rsi(
                self.datasets[ns_parser.target_dataset],
                ns_parser.target_column,
                ns_parser.period,
            )
            console.print(
                f"Successfully added 'RSI_{ns_parser.period}' to '{ns_parser.target_dataset}' dataset"
            )
        console.print()

    @log_start_end(log=logger)
    def call_roc(self, other_args: List[str]):
        """Process ROC"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="roc",
            description="Add rate of change to dataset based on specific column.",
        )
        parser.add_argument(
            "--target-dataset",
            help="The name of the dataset you want to add the ROC to",
            dest="target_dataset",
            type=str,
            choices=list(self.datasets.keys()),
        )
        parser.add_argument(
            "--target-column",
            help="The name of the specific column you want to calculate ROC for.",
            dest="target_column",
            type=str,
            default="close",
        )

        parser.add_argument(
            "--period",
            help="The period to calculate ROC with.",
            dest="period",
            type=check_greater_than_one,
            default=10,
        )
        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, NO_EXPORT, limit=5
        )
        if ns_parser:
            self.datasets[ns_parser.target_dataset] = forecasting_model.add_roc(
                self.datasets[ns_parser.target_dataset],
                ns_parser.target_column,
                ns_parser.period,
            )
            console.print(
                f"Successfully added 'ROC_{ns_parser.period}' to '{ns_parser.target_dataset}' dataset"
            )
        console.print()

    @log_start_end(log=logger)
    def call_mom(self, other_args: List[str]):
        """Process Momentum"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="mom",
            description="Add momentum to dataset based on specific column.",
        )
        parser.add_argument(
            "--target-dataset",
            help="The name of the dataset you want to add the Momentum to",
            dest="target_dataset",
            type=str,
            choices=list(self.datasets.keys()),
        )
        parser.add_argument(
            "--target-column",
            help="The name of the specific column you want to calculate Momentum for.",
            dest="target_column",
            type=str,
            default="close",
        )

        parser.add_argument(
            "--period",
            help="The period to calculate Momentum with.",
            dest="period",
            type=check_greater_than_one,
            default=10,
        )
        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, NO_EXPORT, limit=5
        )
        if ns_parser:
            self.datasets[ns_parser.target_dataset] = forecasting_model.add_momentum(
                self.datasets[ns_parser.target_dataset],
                ns_parser.target_column,
                ns_parser.period,
            )
            console.print(
                f"Successfully added 'Momentum_{ns_parser.period}' to '{ns_parser.target_dataset}' dataset"
            )
        console.print()

    @log_start_end(log=logger)
    def call_export(self, other_args: List[str]):
        """Process export command"""
        parser = argparse.ArgumentParser(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            prog="export",
            description="Export dataset to Excel",
        )

        parser.add_argument(
            "-n",
            "--name",
            dest="name",
            help="The name of the dataset you wish to export",
            type=str,
        )

        parser.add_argument(
            "-t",
            "--type",
            help="The file type you wish to export to",
            dest="type",
            choices=self.file_types,
            type=str,
            default="xlsx",
        )

        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "-n")
        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=NO_EXPORT
        )

        if ns_parser:
            if not ns_parser.name or ns_parser.name not in self.datasets:
                console.print("Please enter a valid dataset.")
            else:
                export_data(
                    ns_parser.type,
                    os.path.dirname(os.path.abspath(__file__)),
                    ns_parser.name,
                    self.datasets[ns_parser.name],
                )

        console.print()

    # EXPO Model
    @log_start_end(log=logger)
    def call_expo(self, other_args: List[str]):
        """Process expo command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="expo",
            description="""
                Perform Probabilistic Exponential Smoothing forecast
                Trend: N: None, A: Additive, M: Multiplicative
                Seasonality: N: None, A: Additive, M: Multiplicative
                Dampen: T: True, F: False
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--trend",
            action="store",
            dest="trend",
            choices=expo_model.TRENDS,
            default="A",
            help="Trend: N: None, A: Additive, M: Multiplicative.",
        )
        parser.add_argument(
            "-s",
            "--seasonal",
            action="store",
            dest="seasonal",
            choices=expo_model.SEASONS,
            default="A",
            help="Seasonality: N: None, A: Additive, M: Multiplicative.",
        )
        parser.add_argument(
            "-p",
            "--periods",
            action="store",
            dest="seasonal_periods",
            type=check_positive,
            default=7,
            help="Seasonal periods: 4: Quarterly, 7: Daily",
        )
        parser.add_argument(
            "-d",
            "--dampen",
            action="store",
            dest="dampen",
            default="F",
            help="Dampening",
        )
        parser.add_argument(
            "-w",
            "--window",
            action="store",
            dest="start_window",
            default=0.85,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )
        # TODO Convert this to multi series
        if ns_parser:

            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(ns_parser.target_col)
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            expo_view.display_expo_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                trend=ns_parser.trend,
                seasonal=ns_parser.seasonal,
                seasonal_periods=ns_parser.seasonal_periods,
                dampen=ns_parser.dampen,
                start_window=ns_parser.start_window,
                forecast_horizon=ns_parser.forecast_horizon,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_theta(self, other_args: List[str]):
        """Process theta command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="theta",
            description="""
                Perform Theta forecast
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "-s",
            "--seasonal",
            action="store",
            dest="seasonal",
            choices=theta_model.SEASONS,
            default="M",
            help="Seasonality: N: None, A: Additive, M: Multiplicative.",
        )
        parser.add_argument(
            "-p",
            "--periods",
            action="store",
            dest="seasonal_periods",
            type=check_positive,
            default=7,
            help="Seasonal periods: 4: Quarterly, 7: Daily",
        )
        parser.add_argument(
            "-w",
            "--window",
            action="store",
            dest="start_window",
            default=0.85,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            theta_view.display_theta_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                seasonal=ns_parser.seasonal,
                seasonal_periods=ns_parser.seasonal_periods,
                start_window=ns_parser.start_window,
                forecast_horizon=ns_parser.forecast_horizon,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_rnn(self, other_args: List[str]):
        """Process RNN command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="rnn",
            description="""
                Perform RNN forecast (Vanilla RNN, LSTM, GRU)
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        # RNN Hyperparameters
        parser.add_argument(
            "--model-type",
            type=str,
            action="store",
            dest="model_type",
            default="LSTM",
            help='Either a string specifying the RNN module type ("RNN", "LSTM" or "GRU")',
        )
        parser.add_argument(
            "--hidden-dim",
            action="store",
            dest="hidden_dim",
            default=20,
            type=check_positive,
            help="Size for feature maps for each hidden RNN layer (h_n)",
        )
        parser.add_argument(
            "--dropout",
            action="store",
            dest="dropout",
            default=0,
            type=check_positive_float,
            help="Fraction of neurons afected by Dropout.",
        )
        parser.add_argument(
            "--batch-size",
            action="store",
            dest="batch_size",
            default=32,
            type=check_positive,
            help="Number of time series (input and output sequences) used in each training pass",
        )
        parser.add_argument(
            "--n-epochs",
            action="store",
            dest="n_epochs",
            default=100,
            type=check_positive,
            help="Number of epochs over which to train the model.",
        )
        parser.add_argument(
            "--learning-rate",
            action="store",
            dest="learning_rate",
            default=1e-3,
            type=check_positive_float,
            help="Learning rate during training.",
        )
        parser.add_argument(
            "--model-save-name",
            type=str,
            action="store",
            dest="model_save_name",
            default="rnn_model",
            help="Name of the model to save.",
        )
        parser.add_argument(
            "--training_length",
            action="store",
            dest="training_length",
            default=20,
            type=check_positive,
            help="""The length of both input (target and covariates) and output (target) time series used during training.
            Generally speaking, training_length should have a higher value than input_chunk_length because otherwise
            during training the RNN is never run for as many iterations as it will during training.""",
        )
        parser.add_argument(
            "--input_chunk_size",
            action="store",
            dest="input_chunk_size",
            default=14,
            type=check_positive,
            help="Number of past time steps that are fed to the forecasting module at prediction time.",
        )
        parser.add_argument(
            "--force-reset",
            action="store",
            dest="force_reset",
            default=True,
            type=bool,
            help="""If set to True, any previously-existing model with the same name will be reset
                    (all checkpoints will be discarded).""",
        )
        parser.add_argument(
            "--save-checkpoints",
            action="store",
            dest="save_checkpoints",
            default=True,
            type=bool,
            help="Whether or not to automatically save the untrained model and checkpoints from training.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            rnn_view.display_rnn_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                model_type=ns_parser.model_type,
                hidden_dim=ns_parser.hidden_dim,
                dropout=ns_parser.dropout,
                batch_size=ns_parser.batch_size,
                n_epochs=ns_parser.n_epochs,
                learning_rate=ns_parser.learning_rate,
                model_save_name=ns_parser.model_save_name,
                training_length=ns_parser.training_length,
                input_chunk_size=ns_parser.input_chunk_size,
                force_reset=ns_parser.force_reset,
                save_checkpoints=ns_parser.save_checkpoints,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_nbeats(self, other_args: List[str]):
        """Process NBEATS command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="rnn",
            description="""
                Perform NBEATS forecast (Neural Bayesian Estimation of Time Series).
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--past-covariates",
            action="store",
            dest="past_covariates",
            default=None,
            type=str,
            help="Past covariates(columns/features) in same dataset that may effect price. Comma separated.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        # NBEATS Hyperparameters
        parser.add_argument(
            "--input-chunk-length",
            action="store",
            dest="input_chunk_length",
            default=14,
            type=check_positive,
            help="The length of the input sequence fed to the model.",
        )
        parser.add_argument(
            "--output-chunk-length",
            action="store",
            dest="output_chunk_length",
            default=5,
            type=check_positive,
            help="The length of the forecast of the model.",
        )
        parser.add_argument(
            "--num_stacks",
            action="store",
            dest="num_stacks",
            default=10,
            type=check_positive_float,
            help="The number of stacks that make up the whole model.",
        )
        parser.add_argument(
            "--num_blocks",
            action="store",
            dest="num_blocks",
            default=3,
            type=check_positive,
            help="The number of blocks making up every stack.",
        )
        parser.add_argument(
            "--num_layers",
            action="store",
            dest="num_layers",
            default=4,
            type=check_positive,
            help="""The number of fully connected layers preceding the final forking layers
            in each block of every stack.""",
        )
        parser.add_argument(
            "--layer_widths",
            action="store",
            dest="layer_widths",
            default=512,
            type=check_positive,
            help="""Determines the number of neurons that make up each fully connected layer
                in each block of every stack""",
        )
        parser.add_argument(
            "--batch-size",
            action="store",
            dest="batch_size",
            default=800,
            type=check_positive,
            help="Number of time series (input and output sequences) used in each training pass.",
        )
        parser.add_argument(
            "--n-epochs",
            action="store",
            dest="n_epochs",
            default=100,
            type=check_positive,
            help="Number of epochs over which to train the model.",
        )
        parser.add_argument(
            "--learning-rate",
            action="store",
            dest="learning_rate",
            default=1e-3,
            type=check_positive_float,
            help="Learning rate during training.",
        )
        parser.add_argument(
            "--model-save-name",
            type=str,
            action="store",
            dest="model_save_name",
            default="nbeats_model",
            help="Name of the model to save.",
        )
        parser.add_argument(
            "--force-reset",
            action="store",
            dest="force_reset",
            default=True,
            type=bool,
            help="""If set to True, any previously-existing model with the same name will be reset
            (all checkpoints will be discarded).""",
        )
        parser.add_argument(
            "--save-checkpoints",
            action="store",
            dest="save_checkpoints",
            default=True,
            type=bool,
            help="Whether or not to automatically save the untrained model and checkpoints from training.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            NBEATS_view.display_nbeats_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                past_covariates=ns_parser.past_covariates,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                input_chunk_length=ns_parser.input_chunk_length,
                output_chunk_length=ns_parser.output_chunk_length,
                num_stacks=ns_parser.num_stacks,
                num_blocks=ns_parser.num_blocks,
                num_layers=ns_parser.num_layers,
                layer_widths=ns_parser.layer_widths,
                batch_size=ns_parser.batch_size,
                n_epochs=ns_parser.n_epochs,
                learning_rate=ns_parser.learning_rate,
                model_save_name=ns_parser.model_save_name,
                force_reset=ns_parser.force_reset,
                save_checkpoints=ns_parser.save_checkpoints,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_tcn(self, other_args: List[str]):
        """Process TCN command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="rnn",
            description="""
                Perform TCN forecast.
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--past-covariates",
            action="store",
            dest="past_covariates",
            default=None,
            type=str,
            help="Past covariates(columns/features) in same dataset that may effect price. Comma separated.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        # TCN Hyperparameters
        parser.add_argument(
            "--input-chunk-length",
            action="store",
            dest="input_chunk_length",
            default=14,
            type=check_positive,
            help="The length of the input sequence fed to the model.",
        )
        parser.add_argument(
            "--output-chunk-length",
            action="store",
            dest="output_chunk_length",
            default=5,
            type=check_positive,
            help="The length of the forecast of the model.",
        )
        parser.add_argument(
            "--dropout",
            action="store",
            dest="dropout",
            default=0.1,
            type=check_positive_float,
            help="The dropout rate for every convolutional layer.",
        )
        parser.add_argument(
            "--num-filters",
            action="store",
            dest="num_filters",
            default=3,
            type=check_positive,
            help="The number of filters in a convolutional layer of the TCN",
        )
        parser.add_argument(
            "--weight-norm",
            action="store",
            dest="weight_norm",
            default=True,
            type=bool,
            help="Boolean value indicating whether to use weight normalization.",
        )
        parser.add_argument(
            "--dilation-base",
            action="store",
            dest="dilation_base",
            default=2,
            type=check_positive,
            help="The base of the exponent that will determine the dilation on every level.",
        )
        parser.add_argument(
            "--batch-size",
            action="store",
            dest="batch_size",
            default=32,
            type=check_positive,
            help="Number of time series (input and output sequences) used in each training pass.",
        )
        parser.add_argument(
            "--n-epochs",
            action="store",
            dest="n_epochs",
            default=100,
            type=check_positive,
            help="Number of epochs over which to train the model.",
        )
        parser.add_argument(
            "--learning-rate",
            action="store",
            dest="learning_rate",
            default=1e-3,
            type=check_positive_float,
            help="Learning rate during training.",
        )
        parser.add_argument(
            "--model-save-name",
            type=str,
            action="store",
            dest="model_save_name",
            default="tcn_model",
            help="Name of the model to save.",
        )
        parser.add_argument(
            "--force-reset",
            action="store",
            dest="force_reset",
            default=True,
            type=bool,
            help="""If set to True, any previously-existing model with the same name will be reset
                (all checkpoints will be discarded).""",
        )
        parser.add_argument(
            "--save-checkpoints",
            action="store",
            dest="save_checkpoints",
            default=True,
            type=bool,
            help="Whether or not to automatically save the untrained model and checkpoints from training.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            TCN_view.display_tcn_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                past_covariates=ns_parser.past_covariates,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                input_chunk_length=ns_parser.input_chunk_length,
                output_chunk_length=ns_parser.output_chunk_length,
                dropout=ns_parser.dropout,
                num_filters=ns_parser.num_filters,
                weight_norm=ns_parser.weight_norm,
                dilation_base=ns_parser.dilation_base,
                batch_size=ns_parser.batch_size,
                n_epochs=ns_parser.n_epochs,
                learning_rate=ns_parser.learning_rate,
                model_save_name=ns_parser.model_save_name,
                force_reset=ns_parser.force_reset,
                save_checkpoints=ns_parser.save_checkpoints,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_regr(self, other_args: List[str]):
        """Process REGR command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="linregr",
            description="""
                Perform a regression forecast
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--past-covariates",
            action="store",
            dest="past_covariates",
            default=None,
            type=str,
            help="Past covariates(columns/features) in same dataset that may effect price. Comma separated.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        parser.add_argument(
            "--output-chunk-length",
            action="store",
            dest="output_chunk_length",
            default=5,
            type=check_positive,
            help="The length of the forecast of the model.",
        )
        parser.add_argument(
            "--lags",
            action="store",
            dest="lags",
            type=check_greater_than_one,
            default=72,
            help="Lagged target values used to predict the next time step.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            regression_view.display_regression(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                past_covariates=ns_parser.past_covariates,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                output_chunk_length=ns_parser.output_chunk_length,
                lags=ns_parser.lags,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_linregr(self, other_args: List[str]):
        """Process LINREGR command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="linregr",
            description="""
                Perform a linear regression forecast
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--past-covariates",
            action="store",
            dest="past_covariates",
            default=None,
            type=str,
            help="Past covariates(columns/features) in same dataset that may effect price. Comma separated.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        parser.add_argument(
            "--output-chunk-length",
            action="store",
            dest="output_chunk_length",
            default=5,
            type=check_positive,
            help="The length of the forecast of the model.",
        )
        parser.add_argument(
            "--lags",
            action="store",
            dest="lags",
            type=check_greater_than_one,
            default=72,
            help="Lagged target values used to predict the next time step.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            linear_regression_view.display_linear_regression(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                past_covariates=ns_parser.past_covariates,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                output_chunk_length=ns_parser.output_chunk_length,
                lags=ns_parser.lags,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_brnn(self, other_args: List[str]):
        """Process BRNN command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="brnn",
            description="""
                Perform BRNN forecast (Vanilla RNN, LSTM, GRU)
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--past-covariates",
            action="store",
            dest="past_covariates",
            default=None,
            type=str,
            help="Past covariates(columns/features) in same dataset that may effect price. Comma separated.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        # BRNN Hyperparameters
        parser.add_argument(
            "--input-chunk-length",
            action="store",
            dest="input_chunk_length",
            default=14,
            type=check_positive,
            help="The length of the input sequence fed to the model.",
        )
        parser.add_argument(
            "--output-chunk-length",
            action="store",
            dest="output_chunk_length",
            default=5,
            type=check_positive,
            help="The length of the forecast of the model.",
        )
        parser.add_argument(
            "--model-type",
            type=str,
            action="store",
            dest="model_type",
            default="LSTM",
            help='Either a string specifying the RNN module type ("RNN", "LSTM" or "GRU")',
        )
        parser.add_argument(
            "--n-rnn-layers",
            action="store",
            dest="n_rnn_layers",
            default=1,
            type=check_positive,
            help="Number of layers in the RNN module.",
        )
        parser.add_argument(
            "--hidden-size",
            action="store",
            dest="hidden_size",
            default=10,
            type=check_positive,
            help="Size for feature maps for each hidden RNN layer (h_n)",
        )
        parser.add_argument(
            "--dropout",
            action="store",
            dest="dropout",
            default=0,
            type=check_positive_float,
            help="Fraction of neurons afected by Dropout.",
        )
        parser.add_argument(
            "--batch-size",
            action="store",
            dest="batch_size",
            default=32,
            type=check_positive,
            help="Number of time series (input and output sequences) used in each training pass",
        )
        parser.add_argument(
            "--n-epochs",
            action="store",
            dest="n_epochs",
            default=100,
            type=check_positive,
            help="Number of epochs over which to train the model.",
        )
        parser.add_argument(
            "--learning-rate",
            action="store",
            dest="learning_rate",
            default=1e-3,
            type=check_positive_float,
            help="Learning rate during training.",
        )
        parser.add_argument(
            "--model-save-name",
            type=str,
            action="store",
            dest="model_save_name",
            default="brnn_model",
            help="Name of the model to save.",
        )
        parser.add_argument(
            "--force-reset",
            action="store",
            dest="force_reset",
            default=True,
            type=bool,
            help="""If set to True, any previously-existing model with the same name will be reset
                    (all checkpoints will be discarded).""",
        )
        parser.add_argument(
            "--save-checkpoints",
            action="store",
            dest="save_checkpoints",
            default=True,
            type=bool,
            help="Whether or not to automatically save the untrained model and checkpoints from training.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            brnn_view.display_brnn_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                past_covariates=ns_parser.past_covariates,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                input_chunk_length=ns_parser.input_chunk_length,
                output_chunk_length=ns_parser.output_chunk_length,
                model_type=ns_parser.model_type,
                n_rnn_layers=ns_parser.n_rnn_layers,
                hidden_size=ns_parser.hidden_size,
                dropout=ns_parser.dropout,
                batch_size=ns_parser.batch_size,
                n_epochs=ns_parser.n_epochs,
                learning_rate=ns_parser.learning_rate,
                model_save_name=ns_parser.model_save_name,
                force_reset=ns_parser.force_reset,
                save_checkpoints=ns_parser.save_checkpoints,
                export=ns_parser.export,
            )

    @log_start_end(log=logger)
    def call_trans(self, other_args: List[str]):
        console.print("[green]Coming soon!\n[/green]")

    @log_start_end(log=logger)
    def call_tft(self, other_args: List[str]):
        """Process TFT command"""
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            add_help=False,
            prog="rnn",
            description="""
                Perform TFT forecast (Temporal Fusion Transformer).
            """,
        )
        parser.add_argument(
            "--target-dataset",
            type=str,
            choices=self.files,
            dest="target_dataset",
            help="Dataset name",
        )
        parser.add_argument(
            "-n",
            "--n-days",
            action="store",
            dest="n_days",
            type=check_greater_than_one,
            default=5,
            help="prediction days.",
        )
        parser.add_argument(
            "--target-forecast-column",
            action="store",
            dest="target_col",
            default="close",
            type=str,
            help="target column.",
        )
        parser.add_argument(
            "--past-covariates",
            action="store",
            dest="past_covariates",
            default=None,
            type=str,
            help="Past covariates(columns/features) in same dataset that may effect price. Comma separated.",
        )
        parser.add_argument(
            "--train-split",
            action="store",
            dest="train_split",
            default=0.85,
            type=check_positive_float,
            help="Start point for rolling training and forecast window. 0.0-1.0",
        )
        parser.add_argument(
            "--forecast-horizon",
            action="store",
            dest="forecast_horizon",
            default=5,
            type=check_greater_than_one,
            help="Days/Points to forecast when training and performing historical back-testing",
        )
        parser.add_argument(
            "--input-chunk-length",
            action="store",
            dest="input_chunk_length",
            default=14,
            type=check_positive,
            help="The length of the input sequence fed to the model.",
        )
        parser.add_argument(
            "--output-chunk-length",
            action="store",
            dest="output_chunk_length",
            default=5,
            type=check_positive,
            help="The length of the forecast of the model.",
        )
        parser.add_argument(
            "--hidden-size",
            action="store",
            dest="hidden_size",
            default=16,
            type=check_positive,
            help="Hidden state size of the TFT.",
        )
        parser.add_argument(
            "--lstm-layers",
            action="store",
            dest="lstm_layers",
            default=1,
            type=check_positive,
            help="Number of LSTM layers.",
        )
        parser.add_argument(
            "--num-attention-heads",
            action="store",
            dest="num_attention_heads",
            default=4,
            type=check_positive,
            help="Number of attention heads.",
        )
        parser.add_argument(
            "--full-attention",
            action="store_true",
            dest="full_attention",
            default=False,
            help="Whether to apply a multi-head attention query.",
        )
        parser.add_argument(
            "--dropout",
            action="store",
            dest="dropout",
            default=0.1,
            type=check_positive_float,
            help="Fraction of neurons affected by dropout.",
        )
        parser.add_argument(
            "--hidden-continuous-size",
            action="store",
            dest="hidden_continuous_size",
            default=8,
            type=check_positive,
            help="Default hidden size for processing continuous variables.",
        )
        parser.add_argument(
            "--n-epochs",
            action="store",
            dest="n_epochs",
            default=100,
            type=check_positive,
            help="Number of epochs over which to train the model.",
        )
        parser.add_argument(
            "--batch-size",
            action="store",
            dest="batch_size",
            default=32,
            type=check_positive,
            help="Number of time series (input and output sequences) used in each training pass",
        )
        parser.add_argument(
            "--model-save-name",
            type=str,
            action="store",
            dest="model_save_name",
            default="tft_model",
            help="Name of the model to save.",
        )
        parser.add_argument(
            "--force-reset",
            action="store",
            dest="force_reset",
            default=True,
            type=bool,
            help="""If set to True, any previously-existing model with the same name will be reset
            (all checkpoints will be discarded).""",
        )
        parser.add_argument(
            "--save-checkpoints",
            action="store",
            dest="save_checkpoints",
            default=True,
            type=bool,
            help="Whether or not to automatically save the untrained model and checkpoints from training.",
        )

        # if user does not put in --target-dataset
        if other_args and "-" not in other_args[0][0]:
            other_args.insert(0, "--target-dataset")

        ns_parser = self.parse_known_args_and_warn(
            parser, other_args, export_allowed=EXPORT_ONLY_FIGURES_ALLOWED
        )

        if ns_parser:
            # check proper file name is provided
            if not ns_parser.target_dataset:
                console.print("[red]Please enter valid dataset.\n[/red]")
                return

            # must check that target col is within target series
            if (
                ns_parser.target_col
                not in self.datasets[ns_parser.target_dataset].columns
            ):
                console.print(
                    f"[red]The target column {ns_parser.target_col} does not exist in dataframe.\n[/red]"
                )
                return

            tft_view.display_tft_forecast(
                data=self.datasets[ns_parser.target_dataset],
                ticker_name=ns_parser.target_dataset,
                n_predict=ns_parser.n_days,
                target_col=ns_parser.target_col,
                past_covariates=ns_parser.past_covariates,
                train_split=ns_parser.train_split,
                forecast_horizon=ns_parser.forecast_horizon,
                input_chunk_length=ns_parser.input_chunk_length,
                output_chunk_length=ns_parser.output_chunk_length,
                hidden_size=ns_parser.hidden_size,
                lstm_layers=ns_parser.lstm_layers,
                num_attention_heads=ns_parser.num_attention_heads,
                full_attention=ns_parser.full_attention,
                dropout=ns_parser.dropout,
                hidden_continuous_size=ns_parser.hidden_continuous_size,
                n_epochs=ns_parser.n_epochs,
                batch_size=ns_parser.batch_size,
                model_save_name=ns_parser.model_save_name,
                force_reset=ns_parser.force_reset,
                save_checkpoints=ns_parser.save_checkpoints,
                export=ns_parser.export,
            )
