from collections import UserDict
from datetime import date, timedelta

from assistant.entity.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> bool:
        if name in self.data:
            del self.data[name]
            return True
        return False

    def get_upcoming_birthdays(self, days: int) -> list[dict]:
        if days < 0:
            raise ValueError("Days cannot be negative")

        start_date = date.today()
        end_date = start_date + timedelta(days=days)
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            original_birthday = record.birthday.value

            for year in range(start_date.year, end_date.year + 1):
                try:
                    birthday_date = original_birthday.replace(year=year)
                except ValueError:
                    # February 29 becomes February 28 in a non-leap year.
                    birthday_date = original_birthday.replace(
                        year=year,
                        day=28,
                    )

                if start_date <= birthday_date <= end_date:
                    upcoming_birthdays.append(
                        {
                            "name": record.name.value,
                            "birthday_date": birthday_date,
                        }
                    )

        upcoming_birthdays.sort(
            key=lambda item: (
                item["birthday_date"],
                item["name"].lower(),
            )
        )

        return upcoming_birthdays