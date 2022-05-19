class Clothes:
    _available_items = {'Shirt': 35,
                        'T-Shirt': 25,
                        'Jacket': 85,
                        'Scarf': 15,
                        'Hat': 12,
                        'Trousers': 29,
                        'Jeans': 59,
                        'Socks': 3,
                        }
    shopping_items = []
    total_price = 0

    def __init__(self, customer):
        self.customer = customer
        items = [item for item in Clothes._available_items.keys()]
        print(f"\tHello, {self.customer}!\n"
              f"\tHere are the products our store offers: ")
        for item in items:
            print(f'- {item}')
        print(f"\tPlease choose 'Buy /item/' to add items to your cart, 'Return /item/' to return an item to the shop\n\t"
              f" or 'Total' to exit and take your receipt: ")

    def buy(self, item):
        # Buy items and add them, and their total price to the cart
        Clothes.shopping_items.append(item)
        price = Clothes._available_items[item]
        Clothes.total_price += price

    def return_item(self, item):
        # Receive an item from the customer and pay pack the money
        Clothes.total_price -= Clothes._available_items[item]

    def total(self):
        # If there are items in the cart - visualize them, and display the money they have to give or receive
        if Clothes.shopping_items:
            print("Your items -> ", end='')
            print(', '.join(Clothes.shopping_items))
        if Clothes.total_price >= 0:
            print(f'Total price -> {Clothes.total_price}$')
        else:
            print(f'The shop owes you {abs(Clothes.total_price)}$')


start = input("Please enter you name: ")
user = Clothes(start)

while True:
    choice = input().split()
    action = choice[0]
    if action == 'Total':
        user.total()
        break
    item = choice[1]
    if action == 'Buy':
        user.buy(item)
        print(f'Current items in the cart: {Clothes.shopping_items}')
    elif action == 'Return':
        user.return_item(item)
        print(f"Choose your next operation: ")
