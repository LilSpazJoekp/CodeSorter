"""Definitions never cross a side-effecting statement that may depend on them."""

ZEBRA = 1
MIDDLE = 5
repr(MIDDLE)  # a barrier: a bare statement splits the surrounding definitions

BANANA = 3
APPLE = 2
