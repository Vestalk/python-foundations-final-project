from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error

class RemovePhoneCommand(Command):
    """remove-phone [name] [phone] - remove a phone number from a contact."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) < 2:
            raise ValueError("Usage: remove-phone [name] [phone]")

        name, phone = args[:2]
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        if record.remove_phone(phone):
            return f"Phone number removed from {name}."
        return f"Phone number {phone} not found for {name}."
