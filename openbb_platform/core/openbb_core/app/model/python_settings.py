"""Python configuration settings model."""

from typing import List, Optional

from pydantic import BaseModel, Field


class PythonSettings(BaseModel):
    """Settings model for Python interface configuration."""

    docstring_sections: List[str] = Field(
        default_factory=lambda: ["description", "parameters", "returns", "examples"]
    )
    docstring_max_length: Optional[int] = Field(
        default=None, description="Length of autogenerated docstrings."
    )

    def __repr__(self) -> str:
        """Return a string representation of the model."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )
