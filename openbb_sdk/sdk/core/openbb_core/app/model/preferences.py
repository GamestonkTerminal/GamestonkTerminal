from pathlib import Path
from typing import Literal

from pydantic import BaseModel, PositiveInt


class Preferences(BaseModel):
    data_directory: str = str(Path.home() / "OpenBBUserData")
    export_directory: str = str(Path.home() / "OpenBBUserData" / "exports")
    user_styles_directory: str = str(Path.home() / "OpenBBUserData" / "styles" / "user")
    charting_extension: Literal["charting"] = "openbb_charting"
    chart_style: Literal["dark", "light"] = "dark"
    plot_enable_pywry: bool = True
    plot_pywry_width: PositiveInt = 1400
    plot_pywry_height: PositiveInt = 762
    plot_open_export: bool = (
        False  # Whether to open plot image exports after they are created
    )
    table_style: Literal["dark", "light"] = "dark"
    request_timeout: PositiveInt = 15
    metadata: bool = True

    class Config:
        validate_assignment = True

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}\n\n" + "\n".join(
            f"{k}: {v}" for k, v in self.dict().items()
        )
