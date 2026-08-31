from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class AddEmailCommand(Command):
    """add-email [name] [email] - add or update an email for a contact."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if len(args) < 2:
            raise ValueError("Usage: add-email [name] [email]")

        name, email = args[:2]
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        record.add_email(email)
        return f"Email added for {name}."
