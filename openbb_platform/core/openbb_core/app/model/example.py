from abc import abstractmethod
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict


class Example(BaseModel):
    """Example model."""

    scope: str
    description: Optional[str] = None  # Should this be required? Would help to create example titles

    model_config = ConfigDict(validate_assignment=True)

    @abstractmethod
    def to_python(self, **kwargs) -> str:
        """Return a Python code representation of the example."""


class APIEx(Example):
    """API Example model."""

    scope: Literal["api"] = "api"
    parameters: Dict[str, Any]

    @property
    def provider(self) -> Optional[str]:
        """Return the provider from the parameters."""
        return self.parameters.get("provider") if self.parameters else None

    def to_python(self, **kwargs) -> str:
        """Return a Python code representation of the example."""
        indentation = kwargs.get("indentation", "")
        func_name = kwargs.get("func_name", "")
        func_params = kwargs.get("func_params", {})
        eg = ""
        if self.parameters is not None:
            if self.description:
                eg += f"{indentation}>>> # {self.description}\n"
            eg += f"{indentation}>>> obb{func_name}("

            for k, v in self.parameters.items():
                if k in func_params and (field := func_params.get(k)):
                    field_type_str = str(field.type)
                    # TODO: Handle types better, some edge cases
                    # like Union[str, List[str]] will be stringified
                    # even if the type is a list
                    if any(t in field_type_str for t in ["int", "float", "bool"]):
                        eg += f"{k}={v}, "
                    else:
                        eg += f"{k}='{v}', "
                else:
                    eg += f"{k}='{v}', "

            eg = indentation + eg.strip(", ") + ")\n"
        return eg


class PythonEx(Example):
    """Python Example model."""

    scope: Literal["python"] = "python"
    code: List[str]

    def to_python(self, **kwargs) -> str:
        """Return a Python code representation of the example."""
        indentation = kwargs.get("indentation", "")
        eg = ""
        if self.code is not None:
            for line in self.code:  # pylint: disable=not-an-iterable
                eg += f"{indentation}>>> {line}\n"

        return eg


def filter_list(
    examples: List[Example],
    providers: List[str],
) -> List[Example]:
    """Filter list of examples."""
    return [
        e
        for e in examples
        if (isinstance(e, APIEx) and (not e.provider or e.provider in providers))
        or e.scope != "api"
    ]
