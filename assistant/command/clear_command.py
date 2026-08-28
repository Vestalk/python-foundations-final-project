import os

from assistant.command.command import Command


class ClearCommand(Command):
    """clear - clear the terminal screen."""

    @staticmethod
    def execute(args, book) -> str:
        os.system("cls" if os.name == "nt" else "clear")
        return ""
