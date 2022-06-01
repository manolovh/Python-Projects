class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=5):
        self.x += change

    def move_left(self, change=5):
        self.x -= change


player_1 = Player(10, 15)
player_1.move_up()
player_1.move_left()
player_1.move_down(15)

print(player_1.x)
print(player_1.y)
