from abc import ABC, abstractmethod
from .creature import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    """Abstract factory for creating creature families."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create base form of the family."""

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create evolved form of the family."""


class FlameFactory(CreatureFactory):
    """Factory for Fire family."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    """Factory for Water family."""

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
