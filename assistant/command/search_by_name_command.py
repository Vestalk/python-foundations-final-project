from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class SearchByNameCommand(Command):
    """search [name] - search contacts by full or partial name."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if not args:
            raise ValueError("Usage: search [name]")

        query = " ".join(args)
        found_records = book.search_by_name(query)

        if not found_records:
            return f"No contacts found for '{query}'."

        result = [f"Contacts found for '{query}':"]
        result.extend(str(record) for record in found_records)

        return "\n".join(result)
