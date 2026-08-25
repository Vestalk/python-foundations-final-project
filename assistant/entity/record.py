from assistant.fields import Birthday, Name, Phone


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None

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
