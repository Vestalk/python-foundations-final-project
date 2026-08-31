from functools import wraps
from typing import Any, Callable


def input_error(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> str:
        try:
            return func(*args, **kwargs)

        except ValueError as err:
            return f"Error: {err}"

        except IndexError:
            return "Error: Please provide all required arguments."

        except KeyError:
            return "Error: Contact not found."

    return inner
