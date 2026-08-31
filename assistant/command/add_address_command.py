from assistant.command.command import Command
from assistant.entity.address_book import AddressBook
from assistant.decorators import input_error


class AddAddressCommand(Command):
    """add-address [name] [address] - add or update an address for a contact."""

    @staticmethod
    @input_error
    def execute(args: list[str], book: AddressBook) -> str:
        if len(args) < 2:
            raise ValueError("Usage: add-address [name] [address]")

        name, *address_parts = args
        record = book.find(name)
        if record is None:
            raise ValueError(f"Contact '{name}' not found.")

        address = " ".join(address_parts)
        record.add_address(address)
        return f"Address added for {name}."
