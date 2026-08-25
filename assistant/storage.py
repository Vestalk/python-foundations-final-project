import pickle

from assistant.entity.address_book import AddressBook

DEFAULT_FILENAME = "addressbook.pkl"


def save_data(book: AddressBook, filename: str = DEFAULT_FILENAME) -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = DEFAULT_FILENAME) -> AddressBook:
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return AddressBook()
