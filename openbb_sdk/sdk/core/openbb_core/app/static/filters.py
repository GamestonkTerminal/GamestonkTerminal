import builtins
import warnings

from openbb_core.app.model.abstract.warning import OpenBBWarning
from openbb_core.app.model.command_output import CommandOutput


def filter_inputs(**kwargs) -> dict:
    """Filter command inputs"""
    return kwargs


def filter_output(command_output: CommandOutput) -> CommandOutput:
    """Filter command output"""
    if command_output.warnings:
        for w in command_output.warnings:
            category = getattr(builtins, w.category, OpenBBWarning)
            warnings.warn(w.message, category)

    error = command_output.error
    if error:
        kind = error.error_kind or "CommandError"
        print(f"{kind}: {error.message}")

    chart = command_output.chart
    if chart and chart.error:
        kind = chart.error.error_kind or "ChartError"
        print(f"{kind}: {chart.error.message}")

    return command_output
