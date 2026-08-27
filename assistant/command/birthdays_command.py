from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error

class BirthdaysCommand(Command):
    """birthdays [days] - show contacts whose birthdays fall within the given number of days (default 7)."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
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
            result.append(f"{item['name']}: {item['birthday_date'].strftime('%d.%m.%Y')}")

        return "\n".join(result)
