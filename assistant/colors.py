from colorama import Fore, init

init(autoreset=True)


def success(text: str) -> str:
    return Fore.GREEN + text


def error(text: str) -> str:
    return Fore.RED + text


def info(text: str) -> str:
    return Fore.CYAN + text


def warning(text: str) -> str:
    return Fore.YELLOW + text


def title(text: str) -> str:
    return Fore.MAGENTA + text
