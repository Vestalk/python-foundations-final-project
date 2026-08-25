from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error

class ShowBirthdayCommand(Command):
    """show-birthday [name] - show the birthday of a contact."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if not args:
            raise ValueError("Usage: show-birthday [name]")

        name = args[0]
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        if record.birthday is None:
            return f"Birthday for {name} is not set."

        return f"{name}'s birthday: {record.birthday}"
