class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please enter a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, sorted_=False):
        if sorted_:
            print(sorted(self._items))
        else:
            print(self._items)


backpack1 = Backpack()
backpack1.add_item('pencil')
backpack1.add_item('pen')
backpack1.remove_item('bag')
print(backpack1.items)
print(backpack1.has_item('pen'))

backpack1.add_item('water bottle')

backpack1.show_items(True)
