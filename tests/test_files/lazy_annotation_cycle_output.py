"""A forward reference in a lazy annotation must not forge a dependency cycle."""

from __future__ import annotations


class _Base:
    """A shared base class."""


class Apple(_Base):
    """References the Instr alias only in a lazy annotation."""

    nxt: list[Instr]


class User:
    """Uses the Instr alias in a lazy annotation."""

    items: list[Instr]


class Zebra(_Base):
    """Another member of the Instr union."""


Instr = Apple | Zebra
