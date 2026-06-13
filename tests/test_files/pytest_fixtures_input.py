import pytest

# Global variables
DATABASE_URL = "sqlite:///test.db"
API_KEY = "test-key-123"


@pytest.fixture
def temp_file(tmp_path):
    """Provide a temporary file for testing."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return file_path


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment automatically."""
    global API_KEY
    API_KEY = "test-key-modified"
    yield
    API_KEY = "test-key-123"


@pytest.fixture(scope="session")
def database_connection():
    """Provide a database connection for testing."""
    return {"connected": True, "url": DATABASE_URL}


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return ["item1", "item2", "item3"]


@pytest.fixture(scope="module")
def shared_resource():
    """Provide a shared resource for module tests."""
    return {"resource": "shared"}


def test_something(database_connection, sample_data):
    """Test function using fixtures."""
    assert database_connection["connected"]
    assert len(sample_data) == 3
