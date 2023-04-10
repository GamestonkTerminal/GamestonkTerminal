from threading import Thread
from typing import Any, Type, TypeVar

from pydantic import ValidationError

from openbb_terminal.core.models import BaseModel

T = TypeVar("T", bound=BaseModel)


def load_dict_to_model(dictionary: dict, model: Type[T]) -> T:
    """Load variables to model.

    Parameters
    ----------
    dictionary : dict
        Variables dictionary.
    model : Type[T]
        Model to load.

    Returns
    -------
    T
        Model with validated data.
    """
    model_name = model.__name__.strip("Model").lower()
    try:
        return model(**dictionary)  # type: ignore
    except ValidationError as error:
        print(f"Error loading {model_name}:")
        for err in error.errors():
            loc = err.get("loc", None)
            var_name = str(loc[0]) if loc else ""
            msg = err.get("msg", "")
            var = dictionary.pop(var_name, None)
            fields: dict[str, Any] = model.get_fields()
            if var and var_name in fields:
                default = fields[var_name].default
                print(f"    {var_name}: {msg}, using default -> {default}")

        return model(**dictionary)  # type: ignore
    except Exception:
        print(f"Error loading {model_name}, using defaults.")
        return model()  # type: ignore


def run_thread(target, kwargs):
    """Run a thread.

    Parameters
    ----------
    target : function
        The target function.
    args : tuple
        The arguments.
    """
    thread = Thread(target=target, kwargs=kwargs)
    thread.start()
