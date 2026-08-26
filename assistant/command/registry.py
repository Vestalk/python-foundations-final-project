from assistant.command.add_address_command import AddAddressCommand
from assistant.command.add_birthday_command import AddBirthdayCommand
from assistant.command.add_contact_command import AddContactCommand
from assistant.command.add_email_command import AddEmailCommand
from assistant.command.birthdays_command import BirthdaysCommand
from assistant.command.change_contact_command import ChangeContactCommand
from assistant.command.command import Command
from assistant.command.delete_contact_command import DeleteContactCommand
from assistant.command.remove_phone_command import RemovePhoneCommand
from assistant.command.search_by_name_command import SearchByNameCommand
from assistant.command.show_all_command import ShowAllCommand
from assistant.command.show_birthday_command import ShowBirthdayCommand
from assistant.command.show_phone_command import ShowPhoneCommand


COMMANDS: dict[str, type[Command]] = {
    "add": AddContactCommand,
    "change": ChangeContactCommand,
    "remove-phone": RemovePhoneCommand,
    "phone": ShowPhoneCommand,
    "all": ShowAllCommand,
    "delete": DeleteContactCommand,
    "add-birthday": AddBirthdayCommand,
    "show-birthday": ShowBirthdayCommand,
    "birthdays": BirthdaysCommand,
    "add-address": AddAddressCommand,
    "add-email": AddEmailCommand,
    "search": SearchByNameCommand,
}
