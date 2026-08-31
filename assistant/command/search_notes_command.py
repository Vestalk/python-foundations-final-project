from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class SearchNotesCommand(Command):
    """search-notes [text] - find notes containing the given text."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if not args:
            raise ValueError("Usage: search-notes [text]")

        query = " ".join(args)
        results = []

        for record in book.data.values():
            notes = record.find_notes_by_text(query)

            for note in notes:
                results.append(f"{record.name.value}: {note}")

        if not results:
            return f"No notes found containing '{query}'."

        return "\n".join(results)
