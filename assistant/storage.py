import pickle
from pathlib import Path

from assistant.entity.address_book import AddressBook

DEFAULT_FILENAME = "addressbook.pkl"
DEFAULT_FILEPATH = Path.home() / DEFAULT_FILENAME


def save_data(
    book: AddressBook,
    filename: str | Path = DEFAULT_FILEPATH,
) -> None:
    path = Path(filename).expanduser()
    with path.open("wb") as f:
        pickle.dump(book, f)


def load_data(filename: str | Path = DEFAULT_FILEPATH) -> AddressBook:
    path = Path(filename).expanduser()
    if not path.exists():
        return AddressBook()

    try:
        with path.open("rb") as f:
            book = pickle.load(f)
    except Exception as error:
        print(f"Warning: could not load '{path}': {error}")
        return AddressBook()

    return book
