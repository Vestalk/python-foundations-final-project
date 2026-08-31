import shlex
from difflib import get_close_matches

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory

from assistant.command.registry import COMMANDS
from assistant.command.help_utils import get_help_info
from assistant.colors import success, error, info, title
from assistant.storage import load_data, save_data

SUCCESS_COMMANDS = {
    "add",
    "add-address",
    "change",
    "remove-phone",
    "delete",
    "add-birthday",
    "add-email",
    "add-note",
    "edit-note",
    "delete-note",
}


def main() -> None:
    book = load_data()

    help_info_msg = get_help_info()

    command_completer = WordCompleter(
        [*COMMANDS.keys(), "help", "close", "exit"],
        ignore_case=True,
        sentence=True,
    )
    session = PromptSession(history=InMemoryHistory())

    print(title("Welcome to the assistant bot!"))
    print(info(help_info_msg))

    while True:
        user_input = session.prompt(
            "Enter a command: ",
            completer=command_completer,
            complete_while_typing=True,
        )

        if not user_input.strip():
            continue

        try:
            command, args = parse_input(user_input)
        except ValueError as parse_error:
            print(error(f"Invalid input: {parse_error}"))
            continue

        if command in ("close", "exit"):
            save_data(book)
            print(success("Good bye!"))
            break
        elif command == "help":
            print(info(help_info_msg))
        elif command in COMMANDS:
            result = COMMANDS[command].execute(args, book)

            if result.startswith("Error:"):
                print(error(result))
            elif command in SUCCESS_COMMANDS:
                print(success(result))
            else:
                print(result)
        else:
            print(error(invalid_command_message(command)))


def parse_input(user_input: str) -> tuple[str, list[str]]:
    cmd, *args = shlex.split(user_input)
    return cmd.lower(), args


def invalid_command_message(command: str) -> str:
    """Return an error message with a close command suggestion, if any."""
    available_commands = [*COMMANDS.keys(), "help", "close", "exit"]
    matches = get_close_matches(
        command,
        available_commands,
        n=1,
        cutoff=0.6,
    )

    if matches:
        return f"Invalid command. Did you mean '{matches[0]}'?"

    return "Invalid command. Type 'help' for the list of commands."


if __name__ == "__main__":
    main()
