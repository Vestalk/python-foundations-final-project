from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error

class DeleteContactCommand(Command):
    """delete [name] - delete a contact from the address book."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if not args:
            raise ValueError("Usage: delete [name]")

        name = args[0]
        if book.delete(name):
            return f"Contact '{name}' deleted."
        return f"Contact '{name}' not found."
