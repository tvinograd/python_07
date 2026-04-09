from abc import ABC, abstractmethod
from ex0 import Creature
from ex1 import HealCapability, TransformCapability


class InvalidStrategyError(Exception):
    """Raised when a BattleStrategy is used on an incompatible Creature."""


class BattleStrategy(ABC):
    """Abstract base class for battle strategies."""

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Return True if creature is suitable for the strategy."""

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Execute the strategy's battle actions."""


class NormalStrategy(BattleStrategy):
    """Strategy suitable for any creature: attack."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy for transforming creatures: transform, attack, revert."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    """Strategy for healing creatures: attack, heal."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())
