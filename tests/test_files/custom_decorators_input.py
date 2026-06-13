from functools import wraps


# Custom decorators
def cache_result(func):
    """Cache the result of a function."""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


def regular_function():
    """A regular function without decorators."""
    return "regular"


def retry_on_failure(max_attempts=3):
    """Retry function on failure."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
            return None

        return wrapper

    return decorator


def validate_input(func):
    """Validate input parameters."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg is None:
                raise ValueError("Input cannot be None")
        return func(*args, **kwargs)

    return wrapper


@retry_on_failure(max_attempts=5)
def unreliable_operation():
    """An operation that might fail."""
    import random

    if random.random() < 0.7:
        raise Exception("Random failure")
    return "Success"


@validate_input
def process_data(data):
    """Process input data."""
    return [item.upper() for item in data]


# Functions with custom decorators
@cache_result
def expensive_calculation(n):
    """Perform an expensive calculation."""
    return sum(i * i for i in range(n))
