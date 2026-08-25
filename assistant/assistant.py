
from assistant.command.registry import COMMANDS
from assistant.command.help_utils import get_help_info
from assistant.storage import load_data, save_data

def main():
    book = load_data()

    help_info_msg = get_help_info();

    print("Welcome to the assistant bot!")
    print(help_info_msg)

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
            print(help_info_msg)
        elif command in COMMANDS:
            print(COMMANDS[command].execute(args, book))
        else:
            print("Invalid command. Type 'help' for the list of commands.")


def parse_input(user_input: str):
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args


if __name__ == "__main__":
    main()
