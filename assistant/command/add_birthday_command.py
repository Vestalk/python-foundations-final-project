from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class AddBirthdayCommand(Command):
    """add-birthday [name] [DD.MM.YYYY] - add or update a birthday for a contact."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if len(args) < 2:
            raise ValueError("Usage: add-birthday [name] [DD.MM.YYYY]")

        name, birthday = args[:2]
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        record.add_birthday(birthday)
        return f"Birthday added for {name}."
