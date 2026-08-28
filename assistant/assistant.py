
from assistant.command.registry import COMMANDS
from assistant.command.help_utils import get_help_info
from assistant.storage import load_data, save_data
from assistant.colors import success, error, info, title
import shlex


SUCCESS_COMMANDS = {
    "add",
    "change",
    "remove-phone",
    "delete",
    "add-birthday",
    "add-note",
    "edit-note",
    "delete-note",
}


def main():
    book = load_data()

    help_info_msg = get_help_info()

    print(title("Welcome to the assistant bot!"))
    print(info(help_info_msg))

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            save_data(book)
            print(success("Good bye!"))
            break
        elif command == "help":
            print(info(help_info_msg))
        elif command in COMMANDS:
            result = COMMANDS[command].execute(args, book)

            if command in SUCCESS_COMMANDS:
                print(success(result))
            else:
                print(result)
        else:
            print(error("Invalid command. Type 'help' for the list of commands."))


def parse_input(user_input: str):
    cmd, *args = shlex.split(user_input)
    return cmd.lower(), args


if __name__ == "__main__":
    main()
