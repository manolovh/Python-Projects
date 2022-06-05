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

    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)

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

backpack1.add_multiple_items(['notebook', 'macbook', 'paper sheets'])
backpack1.show_items()


# METHOD CHAINING
class Burger:

    ingredients = ['bun']

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self

    def display_ingredients(self):
        print("\tIngredients:")
        for ing in self.ingredients:
            print(f"- {ing}")


best_burger = Burger()
best_burger.add_ingredient('beef burger')\
    .add_ingredient('grilled bacon')\
    .add_ingredient('caramelized onion')\
    .add_ingredient('tomato')\
    .add_ingredient('fries')\
    .display_ingredients()
