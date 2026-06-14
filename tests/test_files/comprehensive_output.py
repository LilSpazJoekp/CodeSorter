import os
from abc import ABC, abstractmethod
from functools import wraps

import pytest

# Global variables
DATABASE_URL = "sqlite:///test.db"
API_KEY = "test-key-123"
DEBUG_MODE = os.getenv("DEBUG", "false").lower() == "true"


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment automatically."""
    global API_KEY
    API_KEY = "test-key-modified"
    yield
    API_KEY = "test-key-123"


# Pytest fixtures
@pytest.fixture(scope="session")
def database_connection():
    """Provide a database connection for testing."""
    return {"connected": True, "url": DATABASE_URL}


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return ["item1", "item2", "item3"]


# Custom decorators
def cache_result(func):
    """Cache the result of a function."""
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return wrapper


# Functions with decorators
@cache_result
def expensive_calculation(n):
    """Perform an expensive calculation."""
    return sum(i * i for i in range(n))


def regular_function():
    """A regular function without decorators."""
    return "regular"


def test_animal_inheritance():
    """Test animal inheritance."""
    dog = Dog("Buddy", 3, "brown", "Golden Retriever")
    assert dog.make_sound() == "Woof!"
    assert dog.get_breed_info() == "Breed: Golden Retriever"


def test_global_dependencies():
    """Test global dependencies."""
    db_manager = DatabaseManager()
    api_client = APIClient()

    assert db_manager.is_debug_mode() == DEBUG_MODE
    assert api_client.is_debug_mode() == DEBUG_MODE


# Test functions
def test_something(database_connection, sample_data):
    """Test function using fixtures."""
    assert database_connection["connected"]
    assert len(sample_data) == 3


def validate_input(func):
    """Validate input parameters."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg is None:
                raise ValueError("Input cannot be None")
        return func(*args, **kwargs)

    return wrapper


@validate_input
def process_data(data):
    """Process input data."""
    return [item.upper() for item in data]


class APIClient:
    """API client that uses global endpoints."""

    def __init__(self):
        self.base_url = "https://api.example.com"

    def is_debug_mode(self):
        """Check if debug mode is enabled."""
        return DEBUG_MODE

    def make_request(self, endpoint):
        """Make a request to an endpoint."""
        return f"GET {self.base_url}{endpoint}"


# Base classes with inheritance
class Animal(ABC):
    """Base class for all animals."""

    @abstractmethod
    def make_sound(self):
        """Make a sound."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """Get animal information."""
        return f"{self.name} is {self.age} years old"


# Classes with global dependencies
class DatabaseManager:
    """Manages database connections using global config."""

    def __init__(self):
        self.host = "localhost"  # Would normally use DATABASE_URL
        self.port = 5432
        self.database = "test_db"

    def connect(self):
        """Connect to database."""
        return f"Connected to {self.host}:{self.port}/{self.database}"

    def is_debug_mode(self):
        """Check if debug mode is enabled."""
        return DEBUG_MODE


class Mammal(Animal):
    """Base class for mammals."""

    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def get_fur_info(self):
        """Get fur information."""
        return f"Fur color: {self.fur_color}"

    def make_sound(self):
        """Make a mammal sound."""
        return "Generic mammal sound"


class Dog(Mammal):
    """Dog class."""

    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed

    def fetch(self):
        """Fetch behavior."""
        return f"{self.name} is fetching"

    def get_breed_info(self):
        """Get breed information."""
        return f"Breed: {self.breed}"

    def make_sound(self):
        """Make a dog sound."""
        return "Woof!"
