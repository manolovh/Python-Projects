class Clothes:
    _available_items = {'Shirt': 35,
                        'T-Shirt': 25,
                        'Jacket': 85,
                        'Scarf': 15,
                        'Hat': 12,
                        'Trousers': 29,
                        'Jeans': 59,
                        'Socks(Pair)': 3,
                        }
    shopping_items = []
    shopping_prices = []

    def __init__(self, customer):
        self.customer = customer

    def buy(self, item):
        self.item = item
        # buy items and add them to the cart so the final price and their names can be
        # visualized when then program finishes
        Clothes.shopping_items.append(self.item)
        price = Clothes._available_items[self.item]
        Clothes.shopping_prices.append(price)

    def sell(self):
        # use the sell option to sell an item to the store for 20% less than the actual price
        # and add it to _available_items
        pass

    def total(self):
        print("Your items -> ", end='')
        print(', '.join(Clothes.shopping_items))
        print(f'Total price -> {sum(Clothes.shopping_prices)}')

Gosho = Clothes('Gosho')
Gosho.buy('T-Shirt')
Gosho.buy('Shirt')
Gosho.buy('Scarf')
Gosho.total()