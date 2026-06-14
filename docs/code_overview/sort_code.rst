###########
 Sort Code
###########

The :class:`.SortCodeCommand` is the libcst codemod that performs the reordering. It is
applied by the CLI, but can also be used directly as a libcst codemod (for example via
``python -m libcst.tool codemod codesorter.sort_code.SortCodeCommand``).

.. autoclass:: codesorter.sort_code.SortCodeCommand

The following enumerations define the secondary sort keys used to order members within a
class body.

.. autoclass:: codesorter.sort_code.MethodType

.. autoclass:: codesorter.sort_code.FixtureType

.. autoclass:: codesorter.sort_code.PropertyType
