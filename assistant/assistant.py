from assistant.commands import (
    add_birthday,
    add_contact,
    birthdays,
    change_contact,
    delete_contact,
    remove_phone,
    show_all,
    show_birthday,
    show_help,
    show_phone)
from assistant.storage import load_data, save_data

COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "remove-phone": remove_phone,
    "phone": show_phone,
    "all": show_all,
    "delete": delete_contact,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "birthdays": birthdays,
}


def parse_input(user_input: str):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


def main():
    book = load_data()

    print("Welcome to the assistant bot!")
    print(show_help())

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            save_data(book)
            print("Good bye!")
            break
        elif command == "help":
            print(show_help())
        elif command in COMMANDS:
            print(COMMANDS[command](args, book))
        else:
            print("Invalid command. Type 'help' for the list of commands.")


if __name__ == "__main__":
    main()
