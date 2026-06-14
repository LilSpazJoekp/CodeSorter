from dataclasses import dataclass as data_class
from enum import IntEnum as Bitmask
from typing import NamedTuple


class Color(Bitmask):
    """Enum members keep their order even when the base is imported under an alias."""

    RED = 1
    GREEN = 2
    BLUE = 3


@data_class
class Point:
    """Dataclass fields keep their order even when the decorator is aliased."""

    z: int
    a: int
    m: int = 0

    def distance(self):
        """Methods are still sorted; fields are not."""
        return self.z

    def angle(self):
        """Another method."""
        return self.a


class Pair(NamedTuple):
    """NamedTuple fields keep their order."""

    second: int
    first: int


class Regular:
    """A plain class still sorts its attributes and methods."""

    ZEBRA = 1
    APPLE = 2

    def run(self):
        """A method."""
        return None
