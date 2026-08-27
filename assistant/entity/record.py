from assistant.entity.fields import Birthday, Name, Phone
from assistant.entity.notes import Note


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None
        self.notes: list[Note] = []

    def add_note(self, text: str, tags: list[str]) -> None:
        note = Note(text, tags)
        self.notes.append(note)

    def find_notes_by_tag(self, tag: str) -> list[Note]:
        tag = tag.lower()

        result = []

        for note in self.notes:
            if tag in note.tags:
                result.append(note)

        return result

    def add_phone(self, phone_number: str) -> None:
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number: str) -> bool:
        phone_to_remove = self.find_phone(phone_number)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            return True
        return False

    def edit_phone(self, old_phone_number: str, new_phone_number: str) -> None:
        phone_obj = self.find_phone(old_phone_number)
        if not phone_obj:
            raise ValueError(f"Phone number {old_phone_number} not found.")

        new_phone = Phone(new_phone_number)
        index = self.phones.index(phone_obj)
        self.phones[index] = new_phone

    def find_phone(self, phone_number: str) -> Phone | None:
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def __str__(self) -> str:
        phones = "; ".join(phone.value for phone in self.phones)
        birthday = str(self.birthday) if self.birthday else "not set"
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}, "
            f"birthday: {birthday}"
        )

    def edit_note(
            self,
            note_number: int,
            text: str,
            tags: list[str]) -> None:

        if note_number < 1 or note_number > len(self.notes):
            raise ValueError("Invalid note number.")

        self.notes[note_number - 1] = Note(text, tags)

    def delete_note(self, note_number: int) -> None:
        if note_number < 1 or note_number > len(self.notes):
            raise ValueError("Invalid note number.")

        self.notes.pop(note_number - 1)
