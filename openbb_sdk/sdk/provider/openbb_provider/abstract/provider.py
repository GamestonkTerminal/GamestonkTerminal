"""Abstract class for providers."""

from typing import Dict, List, Optional, Type

from openbb_provider.abstract.fetcher import Fetcher


class Provider:
    """This class serves as provider extensions entry point and must be
    created by each provider."""

    def __init__(
        self,
        name: str,
        description: str,
        website: str,
        fetcher_dict: Dict[str, Type[Fetcher]],
        required_credentials: Optional[List[str]] = None,
    ) -> None:
        """Initialize the provider.

        Parameters
        ----------
        name : str
            Name of the provider.
        description : str
            Description of the provider.
        website : str
            Website of the provider.
        fetcher_dict : Dict[str, Type[Fetcher]]
            Dictionary of fetchers.
        required_credentials : Optional[List[str]], optional
            List of required credentials, by default None
        """
        self.name = name
        self.description = description
        self.website = website
        self.fetcher_dict = fetcher_dict
        if required_credentials is None:
            self.required_credentials: List = []
        else:
            self.required_credentials = []
            for rq in required_credentials:
                self.required_credentials.append(f"{self.name.lower()}_{rq}")
