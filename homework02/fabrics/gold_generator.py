from ..fabrics.item_fabric import ItemFabric
from ..products.gold import Gold


class GoldGenerator(ItemFabric):
    chance = 3

    def create_item(self):
        return Gold()
