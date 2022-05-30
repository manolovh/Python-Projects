class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        if isinstance(items, list):
            self._items = items
        else:
            print("Please enter a valid list of items.")


backpack = Backpack()
print(backpack.items)

backpack.items = ['ala', 'bala', 'foo']
print(backpack.items)

backpack.items = 122
print(backpack.items)
