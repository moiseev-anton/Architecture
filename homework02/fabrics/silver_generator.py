from homework02.fabrics.item_fabric import ItemFabric
from homework02.products.siler import Silver


class SilverGenerator(ItemFabric):
    chance = 10

    def create_item(self):
        return Silver()
