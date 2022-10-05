import random


class Die:
    
    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:
    
    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1
        
    def roll_die(self):
        return self._die.roll()


class DiceGame:
    
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("=============================================")
        print("Welcome to the newest version of Dice Game!")
        print("=============================================")
        while True:
            self._play_round()
            # break out of the loop if any player gets to 0(he wins)
            if self._computer.counter == 0:
                print("The computer won the game.")
                break
            elif self._player.counter == 0:
                print("You won the game. Congratulations!")
                break

    def _play_round(self):
        print("\n\t\tNew Round!\t\t")
        input("Press Enter or any key to continue...\n")

        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")

        if player_value > computer_value:
            self._player.decrement_counter()
            self._computer.increment_counter()
            print("You won this round!")
        elif computer_value > player_value:
            self._computer.decrement_counter()
            self._player.increment_counter()
            print("The computer won this round.")
        else:
            print("It's a Tie!")

        print(f"Your counter: {self._player.counter}")
        print(f"Computer's counter: {self._computer.counter}")


game = DiceGame(Player(Die(), is_computer=False), Player(Die(), is_computer=True))
game.play()
