import os

from assistant.command.command import Command
from assistant.entity.address_book import AddressBook


class ClearCommand(Command):
    """clear - clear the terminal screen."""

    @staticmethod
    def execute(args: list[str], book: AddressBook) -> str:
        os.system("cls" if os.name == "nt" else "clear")
        return ""
