from homework02.fabrics.item_fabric import ItemFabric
from homework02.products.bronze import Bronze


class BronzeGenerator(ItemFabric):
    chance = 10

    def create_item(self):
        return Bronze()
