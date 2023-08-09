"""Journal service."""
from typing import Optional

from openbb_core.app.repository.abstract.journal_entry_repository import (
    JournalEntryRepository as AbstractJournalEntryRepository,
)
from openbb_core.app.repository.abstract.journal_repository import (
    JournalRepository as AbstractJournalRepository,
)
from openbb_core.app.repository.in_memory.journal_entry_repository import (
    JournalEntryRepository as InMemoryJournalEntryRepository,
)
from openbb_core.app.repository.in_memory.journal_repository import (
    JournalRepository as InMemoryJournalRepository,
)
from openbb_core.app.repository.mongodb.journal_entry_repository import (
    JournalEntryRepository as MongoDBJournalEntryRepository,
)
from openbb_core.app.repository.mongodb.journal_repository import (
    JournalRepository as MongoDBJournalRepository,
)
from pymongo.mongo_client import MongoClient


class JournalService:
    """Journal service."""

    @staticmethod
    def valid_client(mongodb_client: Optional[MongoClient] = None) -> bool:
        """Check if the client is valid."""
        if mongodb_client is None:
            return False

        try:
            # Check if the connection is established
            server_info = mongodb_client.server_info()
        except Exception:
            server_info = None

        return bool(server_info)

    @staticmethod
    def build_journal_entry_repository(
        valid_client: bool,
        mongodb_client: Optional[MongoClient] = None,
        journal_entry_repository: Optional[AbstractJournalEntryRepository] = None,
    ) -> AbstractJournalEntryRepository:
        """Build journal entry repository."""
        if journal_entry_repository:
            pass
        elif mongodb_client and valid_client:
            journal_entry_repository = MongoDBJournalEntryRepository(
                client=mongodb_client
            )
        else:
            journal_entry_repository = InMemoryJournalEntryRepository()
        return journal_entry_repository

    @staticmethod
    def build_journal_repository(
        valid_client: bool,
        mongodb_client: Optional[MongoClient] = None,
        journal_repository: Optional[AbstractJournalRepository] = None,
    ) -> AbstractJournalRepository:
        """Build journal repository."""
        if journal_repository:
            pass
        elif mongodb_client and valid_client:
            journal_repository = MongoDBJournalRepository(client=mongodb_client)
        else:
            journal_repository = InMemoryJournalRepository()
        return journal_repository

    def __init__(
        self,
        mongodb_client: Optional[MongoClient] = None,
        journal_entry_repository: Optional[AbstractJournalEntryRepository] = None,
        journal_repository: Optional[AbstractJournalRepository] = None,
    ):
        valid_client = self.valid_client(mongodb_client=mongodb_client)

        self._mongodb_client = mongodb_client
        self._journal_entry_repository = self.build_journal_entry_repository(
            mongodb_client=mongodb_client,
            journal_entry_repository=journal_entry_repository,
            valid_client=valid_client,
        )
        self._journal_repository = self.build_journal_repository(
            mongodb_client=mongodb_client,
            journal_repository=journal_repository,
            valid_client=valid_client,
        )

    @property
    def mongodb_client(self) -> Optional[MongoClient]:
        """Return mongodb client."""
        return self._mongodb_client

    @property
    def journal_entry_repository(self) -> AbstractJournalEntryRepository:
        """Return journal entry repository."""
        return self._journal_entry_repository

    @property
    def journal_repository(self) -> AbstractJournalRepository:
        """Return journal repository."""
        return self._journal_repository
