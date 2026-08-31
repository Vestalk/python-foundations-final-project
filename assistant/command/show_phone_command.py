from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class ShowPhoneCommand(Command):
    """phone [name] - show all phone numbers for a contact."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if not args:
            raise ValueError("Usage: phone [name]")

        name = args[0]
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        if not record.phones:
            return f"Contact '{name}' has no phone numbers."

        phones = "; ".join(phone.value for phone in record.phones)
        return f"{name}: {phones}"
