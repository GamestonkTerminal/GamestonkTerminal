import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd

import openbb_terminal.core.session.hub_service as HubService
from openbb_terminal.core.config.rich_config import console
from openbb_terminal.core.session.current_user import (
    get_platform_user,
)


# created dictionaries for personal and default routines with the structure
# {"file_name" :["script","personal/default"]}
# and stored dictionaries in list
def download_routines(auth_header: str, silent: bool = False) -> list:
    """Download default and personal routines.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    silent : bool
        Whether to silence the console output, by default False

    Returns
    -------
    Dict[str, str]
        The routines.
    """
    personal_routines_dict = {}
    default_routines_dict = {}

    try:
        response = HubService.get_default_routines(silent=silent)
        if response and response.status_code == 200:
            content = response.json()
            data = content.get("data", [])
            for routine in data:
                name = routine.get("name", "")
                if name:
                    default_routines_dict[name] = [routine.get("script", ""), "default"]
    except Exception:
        console.print("[red]\nFailed to download default routines.[/red]")

    try:
        # Number of routines downloaded is limited to 100
        response = HubService.list_routines(
            auth_header=auth_header,
            fields=["name", "script"],
            page=1,
            size=100,
            base_url=HubService.BackendEnvironment.BASE_URL,
            silent=silent,
        )
        if response and response.status_code == 200:
            content = response.json()
            items = content.get("items", [])
            for routine in items:
                name = routine.get("name", "")
                if name:
                    personal_routines_dict[name] = [
                        routine.get("script", ""),
                        "personal",
                    ]
    except Exception:
        console.print("[red]\nFailed to download personal routines.[/red]")

    return [personal_routines_dict, default_routines_dict]


# created new directory structure to account for personal and default routines
def save_routine(
    file_name: str,
    routine: list,
    folder: Optional[Path] = None,
    force: bool = False,
    silent: bool = False,
) -> Union[Optional[Path], str]:
    """Save the routine.

    Parameters
    ----------
    file_name : str
        The routine.
    routine : str
        The routine.
    folder : Path
        The routines folder.
    force : bool
        Force the save.
    silent : bool
        Whether to silence the console output, by default False

    Returns
    -------
    Optional[Path, str]
        The path to the routine or None.
    """
    console_print = console.print if not silent else lambda *args, **kwargs: None

    current_user = get_platform_user()
    if folder is None:
        folder = Path(current_user.preferences.export_directory, "routines")

    try:
        user_folder = folder / "hub"
        if routine[1] == "default":
            user_folder = folder / "hub" / "default"
        elif routine[1] == "personal":
            user_folder = folder / "hub" / "personal"

        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        file_path = user_folder / file_name
        if os.path.exists(file_path) and not force:
            return "File already exists"
        with open(file_path, "w") as f:
            f.write(routine[0])
        return user_folder / file_name
    except Exception:
        console_print("[red]\nFailed to save routine.[/red]")
        return None


def get_default_routines_info(routines: List[Dict[str, str]]) -> pd.DataFrame:
    """Get the routines list.

    Parameters
    ----------
    response : requests.Response
        The response.

    Returns
    -------
    Tuple[pd.DataFrame, int, int]
        The routines list, the current page and the total number of pages.
    """
    df = pd.DataFrame()
    if routines:
        df = pd.DataFrame(routines)
        if all(
            c in df.columns for c in ["name", "description", "version", "date_updated"]
        ):
            df = df[["name", "description", "version", "date_updated"]]
            df.index = np.arange(1, len(df) + 1)
    return df


def get_personal_routines_info(response) -> Tuple[pd.DataFrame, int, int]:
    """Get the routines list.

    Parameters
    ----------
    response : requests.Response
        The response.

    Returns
    -------
    Tuple[pd.DataFrame, int, int]
        The routines list, the current page and the total number of pages.
    """
    df = pd.DataFrame()
    page = 1
    pages = 1
    if response and response.status_code == 200:
        data = response.json()
        page = data.get("page", 1)
        pages = data.get("pages", 1)
        items = data.get("items", [])
        if items:
            df = pd.DataFrame(items)
            df.index = np.arange(1, len(df) + 1)

    return df, page, pages
