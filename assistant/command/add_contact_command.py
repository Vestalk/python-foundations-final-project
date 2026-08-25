from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.entity.record import Record
from assistant.decorators import input_error

class AddContactCommand(Command):
    """add [name] [phone] - add a new contact or a phone to an existing one."""

    @staticmethod
    @input_error
    def execute(args, book: AddressBook) -> str:
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
