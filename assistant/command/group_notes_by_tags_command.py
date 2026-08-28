from collections import defaultdict

from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error
from assistant.colors import title


class GroupNotesByTagsCommand(Command):
    """group-notes-tags - show notes grouped by tags."""
    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        grouped_notes = defaultdict(list)

        for record in book.data.values():
            for note in record.notes:
                for tag in note.tags:
                    grouped_notes[tag.lower()].append(
                        (record.name.value, note)
                    )

        if not grouped_notes:
            return "No notes found."

        results = []

        for tag in sorted(grouped_notes.keys()):
            results.append(title(f"{tag}:"))

            notes = sorted(
                grouped_notes[tag],
                key=lambda item: item[0].lower()
            )

            for contact_name, note in notes:
                results.append(
                    f"  {contact_name}: {note}"
                )

        return "\n".join(results)
