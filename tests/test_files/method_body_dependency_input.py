from __future__ import annotations


class FlairTemplates:
    """Base class for flair templates."""

    def add(self):
        """Add a template."""
        return "added"


class Flair:
    """Depends on LinkTemplates, which is defined later in the module."""

    @property
    def link_templates(self) -> LinkTemplates:
        """Return an instance of a class defined later in the module."""
        return LinkTemplates(self)


class LinkTemplates(FlairTemplates):
    """Subclass of FlairTemplates that Flair depends on."""

    def reorder(self):
        """Reorder the templates."""
        return "reordered"
