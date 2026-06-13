from abc import ABC, abstractmethod


# Base classes
class Animal(ABC):
    """Base class for all animals."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        """Make a sound."""

    def get_info(self):
        """Get animal information."""
        return f"{self.name} is {self.age} years old"


class Mammal(Animal):
    """Base class for mammals."""

    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        """Make a mammal sound."""
        return "Generic mammal sound"

    def get_fur_info(self):
        """Get fur information."""
        return f"Fur color: {self.fur_color}"


class Dog(Mammal):
    """Dog class."""

    def __init__(self, name, age, fur_color, breed):
        super().__init__(name, age, fur_color)
        self.breed = breed

    def make_sound(self):
        """Make a dog sound."""
        return "Woof!"

    def fetch(self):
        """Fetch behavior."""
        return f"{self.name} is fetching"

    def get_breed_info(self):
        """Get breed information."""
        return f"Breed: {self.breed}"


class Cat(Mammal):
    """Cat class."""

    def __init__(self, name, age, fur_color, is_indoor):
        super().__init__(name, age, fur_color)
        self.is_indoor = is_indoor

    def make_sound(self):
        """Make a cat sound."""
        return "Meow!"

    def purr(self):
        """Purr behavior."""
        return f"{self.name} is purring"

    def get_lifestyle_info(self):
        """Get lifestyle information."""
        return f"Indoor cat: {self.is_indoor}"
