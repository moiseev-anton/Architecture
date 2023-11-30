from random import choices

from homework02.fabrics.amulet_generator import AmuletGenerator
from homework02.fabrics.bonus_points_generator import BonusPointsGenerator
from homework02.fabrics.bronze_generator import BronzeGenerator
from homework02.fabrics.elixir_generator import ElixirGenerator
from homework02.fabrics.gem_generator import GemGenerator
from homework02.fabrics.gold_generator import GoldGenerator
from homework02.fabrics.silver_generator import SilverGenerator

if __name__ == '__main__':
    generators = [GemGenerator(),
                  GoldGenerator(),
                  SilverGenerator(),
                  BronzeGenerator(),
                  ElixirGenerator(),
                  AmuletGenerator(),
                  BonusPointsGenerator()
                  ]

    # создаем список с соответствуюими вероятностями выпадения [1,3,10,10,10,10,10]
    chances = [item.chance for item in generators]

    gem_count = gold_count = 0
    for _ in range(100):
        # выбираем элемент в соответсвии с вероятностями
        chosen_item = choices(generators, chances)[0]
        chosen_item.create_item().open()

        # посчитаем сколько раз выпадут Gem и Gold
        gem_count += 1 if isinstance(chosen_item, GemGenerator) else 0
        gold_count += 1 if isinstance(chosen_item, GoldGenerator) else 0

    print(f"Gem выпало {gem_count} раз")
    print(f"Gold выпало {gold_count} раз")
