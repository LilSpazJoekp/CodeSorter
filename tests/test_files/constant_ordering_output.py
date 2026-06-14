"""Constants sort before variables; each group is lexicographic with ``_`` first."""

_INTERNAL = 0
APPLE = 1

ZEBRA = 26
DERIVED = ZEBRA + 1
__version__ = "1.0"
_cache = {}
config = "c"


class Container:
    """Within a class: constants, then variables, then nested classes, then methods."""

    OFFSET = 10
    SCALE = OFFSET * 2
    _hidden = None

    name = "x"

    class Inner:
        """A nested class sorts after attributes but before methods."""

    def __init__(self):
        """Methods sort by kind and name after the attributes and nested classes."""
        self.value = 0

    def compute(self):
        """An instance method."""
        return self.SCALE


def helper():
    """A module-level function sorts after the classes."""
    return None
