from homework02.fabrics.item_fabric import ItemFabric
from homework02.products.elixir import Elixir


class ElixirGenerator(ItemFabric):
    chance = 10

    def create_item(self):
        return Elixir()
