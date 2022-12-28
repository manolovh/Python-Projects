class Car:

    def __init__(self, engine_size, color, model):
        self.engine_size = engine_size
        self.color = color
        self.model = model

    def __lt__(self, other):
        return self.engine_size < other.engine_size

    def __le__(self, other):
        return self.engine_size <= other.engine_size

    def __gt__(self, other):
        return self.engine_size > other.engine_size

    def __ge__(self, other):
        return self.engine_size >= other.engine_size

    def __eq__(self, other):
        return (self.engine_size == other.engine_size
                and self.color == other.color
                and self.model == other.model)

    def __ne__(self, other):
        return (self.engine_size != other.engine_size
                or self.color != other.color
                or self.model != other.model)


my_mercedes = Car(2200, "Gray", "C Class")
my_bmw = Car(3500, "Black", "E60")
other_mercedes = Car(2200, "Red", "E Class")

print(my_mercedes < other_mercedes)
print(my_mercedes <= other_mercedes)
print(my_mercedes > my_bmw)
print(my_bmw >= my_mercedes)
print(my_mercedes == other_mercedes)
print(my_mercedes != other_mercedes)
