from typing import Dict

from pydantic import Field
from pydantic.dataclasses import dataclass

from openbb_terminal.core.models.base_model import BaseModel

# pylint: disable=too-many-instance-attributes, disable=no-member, useless-parent-delegation


@dataclass(config=dict(validate_assignment=True))
class SourcesModel(BaseModel):
    """Model for sources."""

    sources: Dict = Field(default_factory=dict)

    def __repr__(self):
        return super().__repr__()
