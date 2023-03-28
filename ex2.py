from functools import wraps


class InvalidTypeError(Exception):
    """Custom exception for invalid type checking."""
    pass


def type_check(correct_type):
    """
    Decorator that checks if the argument type of the wrapped function matches the correct_type.

    :param correct_type: The expected type of the argument for the wrapped function.
    :return: type_check_decorator
    """
    def type_check_decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, correct_type):
                raise InvalidTypeError(f"Expected type {correct_type}, got {type(arg)} instead.")
            return func(arg)
        return wrapper
    return type_check_decorator

@type_check(int)
def times2(num):
    return num*2

@type_check(str)
def times_double(num):
    return num*2


if __name__ == "__main__":
    try:
        print(times2(4))  # This should work.
        print(times_double("as"))  # This should work.
        print(times2(5.9))  # This should raise an InvalidTypeError.
        print(times_double(5.9))  # This should raise an InvalidTypeError, but we don't over here.
    except InvalidTypeError as e:
        print(e)
