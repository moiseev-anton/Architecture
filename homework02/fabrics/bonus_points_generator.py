from homework02.fabrics.item_fabric import ItemFabric
from homework02.products.bonus_points import BonusPoints


class BonusPointsGenerator(ItemFabric):
    chance = 10

    def create_item(self):
        return BonusPoints()
