from assistant.entity.address_book import AddressBook
from assistant.other.decorators import input_error
from assistant.entity.record import Record


@input_error
def add_contact(args, book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: add [name] [phone]")

    name, phone = args[:2]
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message


@input_error
def change_contact(args, book: AddressBook) -> str:
    if len(args) < 3:
        raise ValueError("Usage: change [name] [old phone] [new phone]")

    name, old_phone, new_phone = args[:3]
    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")

    record.edit_phone(old_phone, new_phone)
    return "Phone number changed."


@input_error
def remove_phone(args, book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: remove-phone [name] [phone]")

    name, phone = args[:2]
    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")

    if record.remove_phone(phone):
        return f"Phone number removed from {name}."
    return f"Phone number {phone} not found for {name}."


@input_error
def show_phone(args, book: AddressBook) -> str:
    if not args:
        raise ValueError("Usage: phone [name]")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")

    if not record.phones:
        return f"Contact '{name}' has no phone numbers."

    phones = "; ".join(phone.value for phone in record.phones)
    return f"{name}: {phones}"


@input_error
def show_all(args, book: AddressBook) -> str:
    if not book.data:
        return "Address book is empty."

    return "\n".join(str(record) for record in book.data.values())


@input_error
def delete_contact(args, book: AddressBook) -> str:
    if not args:
        raise ValueError("Usage: delete [name]")

    name = args[0]
    if book.delete(name):
        return f"Contact '{name}' deleted."
    return f"Contact '{name}' not found."


@input_error
def add_birthday(args, book: AddressBook) -> str:
    if len(args) < 2:
        raise ValueError("Usage: add-birthday [name] [DD.MM.YYYY]")

    name, birthday = args[:2]
    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")

    record.add_birthday(birthday)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book: AddressBook) -> str:
    if not args:
        raise ValueError("Usage: show-birthday [name]")

    name = args[0]
    record = book.find(name)
    if record is None:
        raise ValueError(f"Contact '{name}' not found.")

    if record.birthday is None:
        return f"Birthday for {name} is not set."

    return f"{name}'s birthday: {record.birthday}"


@input_error
def birthdays(args, book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays in the next 7 days."

    result = ["Upcoming birthdays:"]
    for item in upcoming:
        result.append(f"{item['name']}: {item['congratulation_date']}")

    return "\n".join(result)


def show_help() -> str:
    return """
Available commands:
add [name] [phone]
    Add a new contact or add a phone number to an existing contact.

change [name] [old phone] [new phone]
    Change an existing phone number.

remove-phone [name] [phone]
    Remove a phone number from a contact.

phone [name]
    Show all phone numbers for a contact.

all
    Show all contacts in the address book.

delete [name]
    Delete a contact from the address book.

add-birthday [name] [DD.MM.YYYY]
    Add or update a birthday for a contact.

show-birthday [name]
    Show the birthday of a contact.

birthdays
    Show contacts whose birthdays are coming in the next 7 days.

help
    Show this list of available commands.

close / exit
    Save the address book and close the assistant bot.
"""
