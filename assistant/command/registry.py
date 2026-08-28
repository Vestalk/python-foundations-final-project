from assistant.command.add_birthday_command import AddBirthdayCommand
from assistant.command.add_contact_command import AddContactCommand
from assistant.command.birthdays_command import BirthdaysCommand
from assistant.command.change_contact_command import ChangeContactCommand
from assistant.command.command import Command
from assistant.command.delete_contact_command import DeleteContactCommand
from assistant.command.remove_phone_command import RemovePhoneCommand
from assistant.command.show_all_command import ShowAllCommand
from assistant.command.show_birthday_command import ShowBirthdayCommand
from assistant.command.show_phone_command import ShowPhoneCommand
from assistant.command.add_note_command import AddNoteCommand
from assistant.command.show_note_command import ShowNotesCommand
from assistant.command.find_notes_by_tag_command import FindNotesByTagCommand
from assistant.command.edit_note_command import EditNoteCommand
from assistant.command.delete_note_command import DeleteNoteCommand
from assistant.command.group_notes_by_tags_command import GroupNotesByTagsCommand
from assistant.command.clear_command import ClearCommand

COMMANDS: dict[str, type[Command]] = {
    "add": AddContactCommand,
    "change": ChangeContactCommand,
    "remove-phone": RemovePhoneCommand,
    "phone": ShowPhoneCommand,
    "all": ShowAllCommand,
    "delete": DeleteContactCommand,
    "edit-note": EditNoteCommand,
    "delete-note": DeleteNoteCommand,
    "add-birthday": AddBirthdayCommand,
    "show-birthday": ShowBirthdayCommand,
    "show-notes": ShowNotesCommand,
    "find-notes-tag": FindNotesByTagCommand,
    "clear": ClearCommand,
    "group-notes-tags": GroupNotesByTagsCommand,
    "add-note": AddNoteCommand,
    "birthdays": BirthdaysCommand
}
