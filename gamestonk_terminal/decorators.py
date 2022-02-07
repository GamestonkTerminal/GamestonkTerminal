"""Decorators"""
__docformat__ = "numpy"
import functools
import logging
import os
import pandas as pd

from gamestonk_terminal.rich_config import console

logger = logging.getLogger(__name__)


def log_start_end(func=None, log=None):
    """Wrap function to add a log entry at execution start and end.

    Parameters
    ----------
    func : optional
        Function, by default None
    log : optional
        Logger, by default None

    Returns
    -------
        Wrapped function
    """
    assert callable(func) or func is None  # nosec

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            logging_name = ""

            args_passed_in_function = [
                repr(a) for a in args if isinstance(a, (pd.DataFrame, pd.Series)) or a
            ]

            if len(args) == 2 and (
                "__main__.TerminalController" in args_passed_in_function[0]
                or (
                    "gamestonk_terminal." in args_passed_in_function[0]
                    and "_controller" in args_passed_in_function[0]
                )
            ):
                logging_name = args_passed_in_function[0].split()[0][1:]
                args_passed_in_function = args_passed_in_function[1:]

            logger_used = logging.getLogger(logging_name) if logging_name else log

            # view files have parameters that are usually small given they are input by the user
            if "_view" in log.name or "_controller" in log.name:
                kwargs_passed_in_function = kwargs

            # other files can have as parameters big variables, therefore adds logic to only add small ones
            else:
                kwargs_passed_in_function = {
                    key: (
                        value
                        if ((type(value) in (int, float)) or (key == "export"))
                        else type(value)
                    )
                    for key, value in kwargs.items()
                }

            if not kwargs_passed_in_function:
                kwargs_passed_in_function = ""

            args_passed_in_function = (
                " ".join(args_passed_in_function) if args_passed_in_function else ""
            )

            logger_used.info(
                f"START|{args_passed_in_function}|{str(kwargs_passed_in_function)}|",
                extra={"func_name_override": func.__name__},
            )

            if os.environ.get("DEBUG_MODE") == "true":
                value = func(*args, **kwargs)
                log.info("END", extra={"func_name_override": func.__name__})
                return value
            try:
                value = func(*args, **kwargs)
                logger_used.info("END|||", extra={"func_name_override": func.__name__})
                return value
            except Exception as e:
                console.print(f"[red]Error: {e}\n[/red]")
                logger_used.exception(
                    "Exception|||%s",
                    str(e),
                    extra={"func_name_override": func.__name__},
                )
                return []

        return wrapper

    return decorator(func) if callable(func) else decorator
