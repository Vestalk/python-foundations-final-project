from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class ShowNotesCommand(Command):
    """show-notes [name] - show all notes for a contact."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) < 1:
            raise ValueError("Usage: show-notes [name]")

        name = args[0]

        record = book.find(name)

        if record is None:
            raise ValueError(f"Contact {name} not found.")

        if not record.notes:
            return f"No notes for {name}."

        notes = "\n".join(
            f"{index}. {note}"
            for index, note in enumerate(record.notes, start=1)
        )

        return notes
