"""Example Python file showing unsorted code structure. This demonstrates how codesorter organizes code."""

from pathlib import Path

import pytest

# Global variables
CONFIG = {}
DEBUG = False


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment automatically."""
    global DEBUG
    DEBUG = True
    yield
    DEBUG = False


@pytest.fixture(scope="session")
def database_connection():
    """Provide a database connection for testing."""
    # Mock database connection
    return {"connected": True}


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return ["item1", "item2", "item3"]


@pytest.fixture
def temp_file(tmp_path):
    """Provide a temporary file for testing."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return file_path


class FileHandler:
    """A class for handling file operations."""

    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def write_file(self, filename: str, content: str) -> None:
        """Write content to a file."""
        file_path = self.base_path / filename
        file_path.write_text(content)

    def read_file(self, filename: str) -> str:
        """Read a file and return its contents."""
        file_path = self.base_path / filename
        return file_path.read_text()

    @staticmethod
    def is_valid_filename(filename: str) -> bool:
        """Check if filename is valid."""
        return len(filename) > 0 and not filename.startswith(".")


def load_config(config_path: str) -> dict[str, str]:
    """Load configuration from file."""
    config = {}
    if Path(config_path).exists():
        with Path(config_path).open() as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    config[key] = value
    return config


def process_data(data: list[str]) -> dict[str, int]:
    """Process the input data and return statistics."""
    result = {}
    for item in data:
        result[item] = len(item)
    return result


def save_results(results: dict[str, int], filename: str) -> None:
    """Save results to a file."""
    with Path(filename).open("w") as f:
        for key, value in results.items():
            f.write(f"{key}: {value}\n")


def validate_input(value: str) -> bool:
    """Validate the input value."""
    return value is not None and len(value) > 0


class DataProcessor:
    """A class for processing data with various methods."""

    def __init__(self, input_file: str, output_file: str, data: list[str] = None):
        if data is None:
            data = []
        self.data = data
        self.input_file = input_file
        self.output_file = output_file

    @property
    def data_count(self) -> int:
        """Get the count of data items."""
        return len(self.data)

    @data_count.deleter
    def data_count(self) -> None:
        """Delete the data count."""
        self.data.clear()

    @data_count.setter
    def data_count(self, value: int) -> None:
        """Set the data count (dummy setter)."""

    @staticmethod
    def get_file_extension(filename: str) -> str:
        """Get the file extension."""
        return Path(filename).suffix

    @classmethod
    def from_config_file(cls, config_path: str) -> "DataProcessor":
        """Create instance from config file."""
        config = load_config(config_path)
        return cls(**config)

    def save_processed_data(self, output_file: str) -> None:
        """Save processed data to output file."""
        with Path(output_file).open("w") as f:
            f.writelines(self.data)

    def validate_data(self) -> bool:
        """Validate the data."""
        return all(len(item.strip()) > 0 for item in self.data)

    def process_file(self) -> list[str]:
        """Process a file and return its contents."""
        with Path(self.input_file).open() as f:
            return f.readlines()


if __name__ == "__main__":
    processor = DataProcessor(input_file="test.txt", output_file="output.txt")
    input_data = ["hello", "world", "python"]
    output = process_data(input_data)
    print(f"Processed {len(output)} items")
