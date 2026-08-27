import pickle
import shutil
from pathlib import Path

from assistant.entity.address_book import AddressBook

DEFAULT_FILENAME = "addressbook.pkl"


def save_data(book: AddressBook, filename: str = DEFAULT_FILENAME) -> None:
    with open(filename, "wb") as f:
        pickle.dump(book, f)


def load_data(filename: str = DEFAULT_FILENAME) -> AddressBook:
    path = Path(filename)
    if not path.exists():
        return AddressBook()

    try:
        with open(path, "rb") as f:
            book = pickle.load(f)
    except Exception as error:
        print(f"Warning: could not load '{path}': {error});")
        return AddressBook()

    return book

