from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class FindNotesByTagCommand(Command):
    """find-notes-tags - find notes by tags."""
    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) < 1:
            raise ValueError("Usage: find-notes-tag [tag]")

        tag = args[0].lower()

        results = []

        for record in book.data.values():
            notes = record.find_notes_by_tag(tag)

            for note in notes:
                results.append(
                    f"{record.name.value}: {note}"
                )

        if not results:
            return f"No notes found with tag '{tag}'."

        return "\n".join(results)
