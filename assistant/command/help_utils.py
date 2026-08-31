import inspect

from assistant.command.command import Command


CLOSE_ENTRY = "close / exit - Save the address book and close the assistant bot."


def get_help_info() -> str:
    commands = sorted(_find_all_commands(), key=lambda cls: cls.__name__)
    entries = [_describe(command_cls) for command_cls in commands] + [CLOSE_ENTRY]
    commands_str = "  ->  " + "\n  ->  ".join(entries)
    return "\nAvailable commands:\n" + commands_str + "\n"


def _find_all_commands() -> list[type[Command]]:
    found = []
    to_visit = list(Command.__subclasses__())

    while to_visit:
        command_cls = to_visit.pop()
        to_visit.extend(command_cls.__subclasses__())
        if not inspect.isabstract(command_cls):
            found.append(command_cls)

    return found


def _describe(command_cls: type[Command]) -> str:
    return (command_cls.__doc__ or "").strip().splitlines()[0]
