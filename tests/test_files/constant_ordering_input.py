"""Constants sort before variables; each group is lexicographic with ``_`` first."""

ZEBRA = 26
DERIVED = ZEBRA + 1
APPLE = 1
_INTERNAL = 0
config = "c"
_cache = {}
__version__ = "1.0"


def helper():
    """A module-level function sorts after the classes."""
    return None


class Container:
    """Within a class: constants, then variables, then nested classes, then methods."""

    name = "x"
    OFFSET = 10
    SCALE = OFFSET * 2
    _hidden = None

    def compute(self):
        """An instance method."""
        return self.SCALE

    class Inner:
        """A nested class sorts after attributes but before methods."""

    def __init__(self):
        """Methods sort by kind and name after the attributes and nested classes."""
        self.value = 0
