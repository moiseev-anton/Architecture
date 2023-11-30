from homework02.fabrics.item_fabric import ItemFabric
from homework02.products.amulet import Amulet


class AmuletGenerator(ItemFabric):
    chance = 10

    def create_item(self):
        return Amulet()