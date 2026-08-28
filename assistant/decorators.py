from functools import wraps
from assistant.colors import error
from functools import wraps
from assistant.colors import error


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ValueError as err:
            return error(f"Error: {err}")

        except IndexError:
            return error(
                "Error: Please provide all required arguments."
            )

        except KeyError:
            return error("Error: Contact not found.")

    return inner
