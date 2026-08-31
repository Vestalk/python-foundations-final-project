from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class BirthdaysCommand(Command):
    """birthdays [days] - show upcoming birthdays (default 7 days)."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        days = 7
        if args:
            try:
                days = int(args[0])
            except ValueError:
                raise ValueError("Number of days must be an integer.")

        upcoming = book.get_upcoming_birthdays(days)
        if not upcoming:
            return f"No upcoming birthdays in the next {days} days."

        result = [f"Upcoming birthdays in the next {days} days:"]
        for item in upcoming:
            birthday_date = item["birthday_date"].strftime("%d.%m.%Y")
            result.append(f"{item['name']}: {birthday_date}")

        return "\n".join(result)
