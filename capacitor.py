#!/usr/bin/env python3
from ex0 import CreatureFactory
from ex1 import (
    HealCapability,
    HealingCreatureFactory,
    TransformCapability,
    TransformCreatureFactory,
)


def test_healing(factory: CreatureFactory) -> None:
    """Create base and evolved creatures and test heal capability."""
    print("\nTesting Creature with healing capability...")
    for label, creature in (
        ("- base", factory.create_base()),
        ("- evolved", factory.create_evolved()),
    ):
        print(f"\n{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())
        else:
            print(f"{creature.name} cannot heal")


def test_transforming(factory: CreatureFactory) -> None:
    """Create base and evolved creatures and test transform capability."""
    print("\nTesting Creature with transform capability...")
    for label, creature in (
        ("- base", factory.create_base()),
        ("- evolved", factory.create_evolved()),
    ):
        print(f"\n{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            print(f"{creature.name} cannot transform")


def main() -> None:
    try:
        test_healing(HealingCreatureFactory())
        test_transforming(TransformCreatureFactory())
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
