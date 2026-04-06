from abc import ABC, abstractmethod


class HealCapability(ABC):
    """Abstract capability for entities that can heal."""

    @abstractmethod
    def heal(self) -> str:
        """Return description of the heal action."""


class TransformCapability(ABC):
    """Abstract capability for entities that can transform and revert."""

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Switch into transformed state and return description."""

    @abstractmethod
    def revert(self) -> str:
        """Switch back to normal state and return description."""
