import re
from datetime import date, datetime
from typing import Generic, TypeVar


EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
FieldValue = TypeVar("FieldValue")


class Field(Generic[FieldValue]):
    """Base class for a single record field."""

    def __init__(self, value: FieldValue) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field[str]):
    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)


class Phone(Field[str]):
    def __init__(self, value: str) -> None:
        if not (value.isdigit() and len(value) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value)


class Birthday(Field[date]):
    def __init__(self, value: str) -> None:
        try:
            parsed_value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY") from None
        super().__init__(parsed_value)

    def __str__(self) -> str:
        return self.value.strftime("%d.%m.%Y")


class Address(Field[str]):
    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError("Address cannot be empty.")
        super().__init__(value)


class Email(Field[str]):
    def __init__(self, value: str) -> None:
        if not re.fullmatch(EMAIL_PATTERN, value):
            raise ValueError("Invalid email format")
        super().__init__(value)
