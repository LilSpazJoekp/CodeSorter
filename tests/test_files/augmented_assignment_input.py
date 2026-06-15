"""Augmented assignments stay anchored to the constant they augment."""

import enum
import json

ZEBRA = 1
__version__ = "1.0"
__all__ = ["Widget"]
__all__ += json.__all__
__all__ += enum.__all__
APPLE = 2


class Widget:
    """A class that sorts after the module-level assignments."""


class Gadget:
    """Another class."""
