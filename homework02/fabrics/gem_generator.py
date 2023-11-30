from homework02.fabrics.item_fabric import ItemFabric
from homework02.products.gem import Gem


class GemGenerator(ItemFabric):
    chance = 1

    def create_item(self):
        return Gem()