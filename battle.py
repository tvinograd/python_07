#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    """Create base and evolved creatures with description and attack."""
    print("\nTesting factory...")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
        factory_a: CreatureFactory,
        factory_b: CreatureFactory
) -> None:
    """Make base creatures of two factories fight."""
    print("\nTesting battle...")
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()
    print(f"{creature_a.describe()}\n vs.\n{creature_b.describe()}\n fight!")
    print(creature_a.attack())
    print(creature_b.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    try:
        test_factory(flame_factory)
        test_factory(aqua_factory)
        test_battle(flame_factory, aqua_factory)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
