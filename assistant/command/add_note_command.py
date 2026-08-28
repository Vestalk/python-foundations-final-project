from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class AddNoteCommand(Command):
    """add-note [name] "note text" [tags...] - add a note to a contact."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) < 2:
            raise ValueError(
                'Usage: add-note [name] "note text" [tags...]'
            )

        name = args[0]
        text = args[1]

        tags = [tag.strip().strip(",") for tag in args[2:]]

        record = book.find(name)

        if record is None:
            raise ValueError(f"Contact {name} not found.")

        record.add_note(text, tags)

        return "Note added."
