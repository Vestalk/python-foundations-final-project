from abc import ABC, abstractmethod
from assistant.entity.address_book import AddressBook

class Command(ABC):
    """Base class for a single CLI command."""

    @staticmethod
    @abstractmethod
    def execute(args: list[str], book: AddressBook) -> str:
        raise NotImplementedError
