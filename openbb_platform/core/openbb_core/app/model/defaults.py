"""Defaults model."""

from typing import Dict, List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class Defaults(BaseModel):
    """Defaults."""

    model_config = ConfigDict(validate_assignment=True)

    commands: Dict[str, Dict[str, Optional[Union[str, List[str]]]]] = Field(
        default_factory=dict,
        alias="routes",  # routes was deprecated in favor of commands
    )

    def __repr__(self) -> str:
        """Return string representation."""
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.model_dump().items()
        )
