from assistant.entity.fields import Birthday, Name, Phone, Address, Email


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday | None = None
        self.address: Address | None = None
        self.email: Email | None = None

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

    def add_address(self, address: str) -> None:
        self.address = Address(address)

    def add_email(self, email: str) -> None:
        self.email = Email(email)

    def __str__(self) -> str:
        phones = "; ".join(phone.value for phone in self.phones)
        birthday = str(self.birthday) if self.birthday else "not set"
        address = str(self.address) if self.address else "not set"
        email = str(self.email) if self.email else "not set"

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}, "
            f"birthday: {birthday}, "
            f"address: {address}, "
            f"email: {email}"
        )
