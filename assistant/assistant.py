import shlex

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory

from assistant.command.registry import COMMANDS
from assistant.command.help_utils import get_help_info
from assistant.storage import load_data, save_data


def main():
    book = load_data()

    help_info_msg = get_help_info()

    command_completer = WordCompleter(
        [*COMMANDS.keys(), "help", "close", "exit"],
        ignore_case=True,
        sentence=True,
    )
    session = PromptSession(history=InMemoryHistory())

    print("Welcome to the assistant bot!")
    print(help_info_msg)

    while True:
        user_input = session.prompt(
            "Enter a command: ",
            completer=command_completer,
            complete_while_typing=True,
        )

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
    cmd, *args = shlex.split(user_input)
    return cmd.lower(), args


if __name__ == "__main__":
    main()
