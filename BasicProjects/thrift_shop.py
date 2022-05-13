class ThriftShop:
    _checkout_items = []
    _checkout_prices = []
    _item_quantity = 0
    def __init__(self, price: float, color):
        self.price = price
        self.color = color


class Shoes(ThriftShop):
    def __init__(self, size: float, price: float, color):
        self.size = size

        ThriftShop.__init__(self, price, color)


class Shirts(ThriftShop):
    def __init__(self, size: str, price: float, color):
        self.size = size

        ThriftShop.__init__(self, price, color)


class Furniture(ThriftShop):
    def __init__(self, material, room_type, price: float):
        self.material = material
        self.room_type = room_type

        ThriftShop.__init__(self, price)


class Books(ThriftShop):
    pass


class SportingEquipment(ThriftShop):
    pass
