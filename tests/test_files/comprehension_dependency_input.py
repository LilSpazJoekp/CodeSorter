"""A module-level comprehension references a function eagerly, so it depends on it."""


def lazy():
    """A comprehension here is deferred, so it imposes no ordering."""
    return [build(name) for name in ["c", "d"]]


def build(name):
    """Used eagerly by the module-level comprehension below."""
    return f"value-{name}"


placeholders = {name: build(name) for name in ["a", "b"]}
