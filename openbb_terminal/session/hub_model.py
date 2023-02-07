from typing import Dict, Optional

import requests

from openbb_terminal.rich_config import console

BASE_URL = "https://payments.openbb.dev/"
TIMEOUT = 15


def create_session(
    email: str, password: str, base_url: str = BASE_URL, timeout: int = TIMEOUT
) -> Optional[requests.Response]:
    """Create a session.

    Parameters
    ----------
    email : str
        The email.
    password : str
        The password.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the login request.
    """
    try:
        data = {
            "email": email,
            "password": password,
            "remember": True,
        }
        return requests.post(url=base_url + "login", json=data, timeout=timeout)
    except requests.exceptions.ConnectionError:
        console.print("\n[red]Connection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("\n[red]Connection timeout.[/red]")
        return None
    except Exception:
        console.print("\n[red]Failed to request login info.[/red]")
        return None


def create_session_from_token(
    token: str, base_url: str = BASE_URL, timeout: int = TIMEOUT
):
    """Create a session from token.

    Parameters
    ----------
    token : str
        The token.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT
    """
    try:
        data = {
            "token": token,
        }
        return requests.post(url=base_url + "sdk/login", json=data, timeout=timeout)
    except requests.exceptions.ConnectionError:
        console.print("\n[red]Connection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("\n[red]Connection timeout.[/red]")
        return None
    except Exception:
        console.print("\n[red]Failed to request login info.[/red]")
        return None


def delete_session(
    auth_header: str, token: str, base_url: str = BASE_URL, timeout: int = TIMEOUT
) -> Optional[requests.Response]:
    """Delete the session.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    token : str
        The token to delete.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the logout request.
    """
    try:
        response = requests.post(
            url=base_url + "logout",
            headers={"Authorization": auth_header},
            json={"token": token},
            timeout=timeout,
        )
        if response.status_code != 200:
            console.print("[red]Failed to delete server session.[/red]")
        return response
    except requests.exceptions.ConnectionError:
        console.print("[red]Connection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("[red]\nConnection timeout.[/red]")
        return None
    except Exception:
        console.print("[red]Failed to delete server session.[/red]")
        return None


def process_session_response(response: requests.Response) -> dict:
    """Process the response from the login request.

    Parameters
    ----------
    response : requests.Response
        The response from the login request.

    Returns
    -------
    dict
        The login info.
    """
    if response.status_code == 200:
        login = response.json()
        return login
    if response.status_code == 401:
        console.print("\n[red]Wrong credentials.[/red]")
        return {}
    if response.status_code == 403:
        console.print("\n[red]Unverified email.[/red]")
        return {}
    console.print("\n[red]Failed to login.[/red]")
    return {}


def get_session(email: str, password: str) -> dict:
    """Get the session info.

    Parameters
    ----------
    email : str
        The email.
    password : str
        The password.

    Returns
    -------
    dict
        The session info.
    """
    response = create_session(email, password)
    if response is None:
        return {}
    return process_session_response(response)


def get_session_from_token(token: str) -> dict:
    """Get the session info from token.

    Parameters
    ----------
    token : str
        The token.

    Returns
    -------
    dict
        The session info.
    """
    response = create_session_from_token(token)
    if response.status_code == 200:
        return response.json()
    return {}


def fetch_user_configs(
    session: dict, base_url: str = BASE_URL, timeout: int = TIMEOUT
) -> Optional[requests.Response]:
    """Fetch user configurations.

    Parameters
    ----------
    session : dict
        The session info.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the get request.
    """

    token_type = session.get("token_type", "")
    token = session.get("access_token", "")

    try:
        response = requests.get(
            url=base_url + "terminal/user",
            headers={"Authorization": f"{token_type.title()} {token}"},
            timeout=timeout,
        )
        if response.status_code != 200:
            console.print("[red]\nFailed to fetch configurations.[/red]")
        return response
    except requests.exceptions.ConnectionError:
        console.print("[red]\nConnection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("[red]\nConnection timeout.[/red]")
        return None
    except Exception:
        console.print("[red]\nFailed to fetch configurations.[/red]")
        return None


def patch_user_configs(
    key: str,
    value: str,
    type_: str,
    auth_header: str,
    base_url: str = BASE_URL,
    timeout: int = TIMEOUT,
) -> Optional[requests.Response]:
    """Patch user configurations to the server.

    Parameters
    ----------
    key : str
        The key to patch.
    value : str
        The value to patch.
    type_ : str
        The type of the patch, either "keys" or "settings".
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the patch request.
    """

    if type_ not in ["keys", "settings"]:
        console.print("[red]\nInvalid patch type.[/red]")
        return None

    data = {"key": f"features_{type_}.{key}", "value": value}

    try:
        response = requests.patch(
            url=base_url + "terminal/user",
            headers={"Authorization": auth_header},
            json=data,
            timeout=timeout,
        )
        if response.status_code == 200:
            console.print("[green]Saved remotely.[/green]")
        else:
            console.print("[red]Failed to save remotely.[/red]")
        return response
    except requests.exceptions.ConnectionError:
        console.print("[red]Connection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("[red]\nConnection timeout.[/red]")
        return None
    except Exception:
        console.print("[red]Failed to save remotely.[/red]")
        return None


def clear_user_configs(
    auth_header: str, base_url: str = BASE_URL, timeout: int = TIMEOUT
) -> Optional[requests.Response]:
    """Clear user configurations to the server.

    Parameters
    ----------
    auth_header : str
        The authorization header, e.g. "Bearer <token>".
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT

    Returns
    -------
    Optional[requests.Response]
        The response from the put request.
    """
    data: Dict[str, dict] = {"features_keys": {}, "features_settings": {}}

    try:
        response = requests.put(
            url=base_url + "terminal/user",
            headers={"Authorization": auth_header},
            json=data,
            timeout=timeout,
        )
        if response.status_code == 200:
            console.print("[green]Cleared configurations.[/green]")
        else:
            console.print("[red]Failed to clear configurations.[/red]")
        return response
    except requests.exceptions.ConnectionError:
        console.print("[red]Connection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("[red]\nConnection timeout.[/red]")
        return None
    except Exception:
        console.print("[red]Failed to clear configurations.[/red]")
        return None


def upload_routine(
    auth_header: str,
    name: str = "",
    routine: str = "",
    base_url=BASE_URL,
    timeout: int = TIMEOUT,
) -> Optional[requests.Response]:
    """Send a routine to the server.

    Parameters
    ----------
    auth_header : str

    name : str
        The name of the routine.
    routine : str
        The routine.
    base_url : str
        The base url, by default BASE_URL
    timeout : int
        The timeout, by default TIMEOUT
    """

    data = {"name": name, "script": routine}

    try:
        response = requests.post(
            headers={"Authorization": auth_header},
            url=base_url + "terminal/script",
            json=data,
            timeout=timeout,
        )
        if response.status_code == 200:
            console.print("[green]Successfully uploaded your routine.[/green]")
        else:
            console.print("[red]Error uploading your routine.[/red]")
        return response
    except requests.exceptions.ConnectionError:
        console.print("[red]Connection error.[/red]")
        return None
    except requests.exceptions.Timeout:
        console.print("[red]\nConnection timeout.[/red]")
        return None
    except Exception:
        console.print("[red]Failed to upload your routine.[/red]")
        return None


def download_routine() -> Optional[requests.Response]:
    """Download a routine from the server."""

    # TODO: Implement test on `test_hub_model.py` when this is implemented.

    console.print("[red]Not implemented yet.[/red]")
    return None
