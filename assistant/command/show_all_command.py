from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class ShowAllCommand(Command):
    """all - show all contacts in the address book."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if not book.data:
            return "Address book is empty."

        return "\n".join(str(record) for record in book.data.values())
