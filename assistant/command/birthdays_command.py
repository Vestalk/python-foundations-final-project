from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error

class BirthdaysCommand(Command):
    """birthdays - show contacts whose birthdays are coming in the next 7 days."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        upcoming = book.get_upcoming_birthdays()
        if not upcoming:
            return "No upcoming birthdays in the next 7 days."

        result = ["Upcoming birthdays:"]
        for item in upcoming:
            result.append(f"{item['name']}: {item['congratulation_date']}")

        return "\n".join(result)
