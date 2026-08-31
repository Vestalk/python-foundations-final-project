
from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class DeleteNoteCommand(Command):
    """delete-note [name] [number] - delete a note."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if len(args) < 2:
            raise ValueError(
                "Usage: delete-note [name] [number]"
            )

        name = args[0]
        note_number = int(args[1])

        record = book.find(name)

        if record is None:
            raise ValueError(f"Contact {name} not found.")

        record.delete_note(note_number)

        return "Note deleted."
