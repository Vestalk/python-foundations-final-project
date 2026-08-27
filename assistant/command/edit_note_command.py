from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class EditNoteCommand(Command):
    """edit-note [name] [number] "new text" [tags...] - edit a note."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) < 3:
            raise ValueError(
                'Usage: edit-note [name] [number] "new text" [tags...]'
            )

        name = args[0]
        note_number = int(args[1])
        text = args[2]
        tags = args[3:]

        record = book.find(name)

        if record is None:
            raise ValueError(f"Contact {name} not found.")

        record.edit_note(note_number, text, tags)

        return "Note updated."
