class Car:

    def __init__(self, brand, color, year, engine):
        self.brand  = brand
        self.color = color
        self.year = year
        self.engine = engine


class Mercedes(Car):

    def __init__(self, color, year, engine, model, has_extras=False, brand="Mercedes"):
        super().__init__(brand, color, year, engine)
        self.model = model
        self.has_extras = has_extras


benz = Mercedes("Blue", 2011, 2200, "C Class", True)
print(benz.brand)
print(benz.color)
print(benz.year)
print(benz.model)
print(benz.engine)
print(benz.has_extras)
