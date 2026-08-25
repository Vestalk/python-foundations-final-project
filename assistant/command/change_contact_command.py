from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error

class ChangeContactCommand(Command):
    """change [name] [old phone] [new phone] - change an existing phone number."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) < 3:
            raise ValueError("Usage: change [name] [old phone] [new phone]")

        name, old_phone, new_phone = args[:3]
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        record.edit_phone(old_phone, new_phone)
        return "Phone number changed."
