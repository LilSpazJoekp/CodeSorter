"""Definitions never cross a side-effecting statement that may depend on them."""

MIDDLE = 5
ZEBRA = 1
repr(MIDDLE)  # a barrier: a bare statement splits the surrounding definitions

APPLE = 2
BANANA = 3
