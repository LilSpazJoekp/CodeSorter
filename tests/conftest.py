"""Shared pytest fixtures for the codesorter test suite."""

from pathlib import Path

import pytest


@pytest.fixture
def test_files(request):
    """Load test input and expected output files."""
    test_files_dir = Path(__file__).parent / "test_files"

    name = request.node.name.removeprefix("test_")
    input_file = test_files_dir / f"{name}_input.py"
    expected_file = test_files_dir / f"{name}_output.py"

    if not input_file.exists() or not expected_file.exists():
        pytest.fail(f"Test files not found for {request.node.name}")

    input_code = input_file.read_text()
    expected_code = expected_file.read_text()

    if input_code == expected_code:
        pytest.fail(f"Input and expected files are identical for {request.node.name}")

    # strip empty lines as CodeSorter doesn't preserve them or enforce a specific style
    return strip_empty_lines(input_code), strip_empty_lines(expected_code)


def strip_empty_lines(code: str) -> str:
    return "\n".join([line for line in code.splitlines() if line.strip()]) + "\n"
