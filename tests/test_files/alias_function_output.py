"""An assignment that aliases a method stays after the method it references."""


class SomeClass:
    """A class whose alias assignment must follow its target, not float ahead of it."""

    def aaa_first(self):
        """A method that sorts first alphabetically."""
        return 2

    def zzz_target(self, *args, **kwargs):
        """The aliased method, which sorts last alphabetically."""
        ...

    alias_func = zzz_target
