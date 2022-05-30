# @property is the preferred pythonic way of writing code, because it makes the code more
# readable and easier to understand. Its use results in simpler and shorter code.

class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 0 < new_price < 1000:
            self._price = new_price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if 0 < new_size < 1000:
            self._size = new_size

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_brand):
        if 0 < new_brand < 1000:
            self._brand = new_brand


class BouncyBall2:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, new_price):
        if isinstance(new_price, int):
            self._price = new_price

    price = property(get_price, set_price)

    def get_size(self):
        return self._size

    def set_size(self, new_size):
        if isinstance(new_size, float):
            self._size = new_size

    size = property(get_size, set_size)

    def get_brand(self):
        return self._brand

    def set_brand(self, new_brand):
        if isinstance(new_brand, str):
            self._brand = new_brand

    brand = property(get_brand, set_brand)


ball_1 = BouncyBall(120, 12, 'Shop')
ball_2 = BouncyBall2(190, 15, 'Ship')

print(ball_1.price)
print(ball_1.size)
print(ball_1.brand)

print(ball_2.price)
print(ball_2.size)
print(ball_2.brand)

# test