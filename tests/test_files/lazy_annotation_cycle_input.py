"""A forward reference in a lazy annotation must not forge a dependency cycle."""

from __future__ import annotations


class Apple(_Base):
    """References the Instr alias only in a lazy annotation."""

    nxt: list[Instr]


class _Base:
    """A shared base class."""


class Zebra(_Base):
    """Another member of the Instr union."""


Instr = Apple | Zebra


class User:
    """Uses the Instr alias in a lazy annotation."""

    items: list[Instr]
