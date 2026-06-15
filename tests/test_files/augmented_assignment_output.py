"""Augmented assignments stay anchored to the constant they augment."""

import enum
import json

APPLE = 2
ZEBRA = 1
__all__ = ["Widget"]
__all__ += json.__all__
__all__ += enum.__all__
__version__ = "1.0"


class Gadget:
    """Another class."""


class Widget:
    """A class that sorts after the module-level assignments."""
