from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f"Error: {error}"
        except IndexError:
            return "Error: Please provide all required arguments."
        except KeyError:
            return "Error: Contact not found."

    return inner
