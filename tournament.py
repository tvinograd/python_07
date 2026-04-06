#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)

Opponent = tuple[CreatureFactory, BattleStrategy]


def battle(opponents: list[Opponent]) -> None:
    """Run a tournament between the given opponents."""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                creature_a = factory_a.create_base()
                creature_b = factory_b.create_base()
                print("\n* Battle *")
                print(
                    f"{creature_a.describe()}\n vs.\n"
                    f"{creature_b.describe()}\n now fight!"
                )
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transforming = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("\nTournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggressive), (healing, defensive)])

    print("\nTournament 2 (multiple)")
    print(
        " [ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )
    battle([
        (aqua, normal),
        (healing, defensive),
        (transforming, aggressive),
    ])


if __name__ == "__main__":
    main()
