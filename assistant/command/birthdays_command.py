from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class BirthdaysCommand(Command):
    """birthdays [days] - show birthdays during the next specified number of days."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
        if len(args) != 1:
            raise ValueError("Usage: birthdays [days]")

        try:
            days = int(args[0])
        except ValueError:
            raise ValueError("Days must be an integer")

        if days < 0:
            raise ValueError("Days cannot be negative")

        upcoming_birthdays = book.get_upcoming_birthdays(days)

        if not upcoming_birthdays:
            return f"No birthdays in the next {days} days."

        result = [
            f"Here is the list of birthdays for the next {days} days:"
        ]

        for item in upcoming_birthdays:
            birthday_date = item["birthday_date"]
            result.append(
                f"{item['name']}: {birthday_date.strftime('%d.%m.%Y')}"
            )

        return "\n".join(result)