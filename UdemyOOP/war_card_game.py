import random


class Suit:
    SUIT_SYMBOLS = {'clubs': '♣',
                    'diamonds': '♦',
                    'hearts': '♥',
                    'spades': '♠', }

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SUIT_SYMBOLS[description.lower()]

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self._symbol


class Card:
    SPECIAL_VALUES = {11: 'Jack',
                      12: 'Queen',
                      13: 'King',
                      14: 'Ace', }

    def __init__(self, suit, value):
        self._suit = Suit(suit)
        self._value = value

    @property
    def suit(self):
        return self._suit.description

    @property
    def value(self):
        return self._value

    def is_special(self):
        # the same as -> return self._value >= 11
        return True if self.value >= 11 else False

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        card_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_VALUES[card_value]
            print(f"{card_description} of {card_suit} {card_symbol}")
        else:
            print(f"{card_value} of {card_suit} {card_symbol}")


class Deck:

    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, is_empty=False):
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUITS:
            for value in range(2, 15):
                self._cards.append(Card(suit, value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            # when specifying the first value to be returned,
            # you should address the opposite as well, in this case - None
            return None

    def add(self, card):
        self._cards.insert(0, card)


class Player:

    def __init__(self, name, deck, is_computer=False):
        self.name = name
        self._deck = deck
        self._is_computer = is_computer

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def deck(self):
        return self._deck

    def has_empty_deck(self):
        # same as -> return self._deck.size == 0
        return True if self._deck.size == 0 else False

    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        self._deck.add(card)


class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck

        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):

        print("\nLet the game begin...\n")

        player_card = self._player.draw_card()
        computer_card = self._computer.draw_card()

        print("Your card: ")
        player_card.show()

        print("\nComputer card: ")
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner == WarCardGame.PLAYER:
            print("\nYou won the round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner == WarCardGame.COMPUTER:
            print("\nThe computer won the round.")
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\n Tie! This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, computer_card, previous_cards):
        if previous_cards:
            return [player_card, computer_card] + previous_cards
        else:
            return [player_card, computer_card]

    def add_cards_to_character(self, character, list_of_cards):
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_card = self._player.draw_card()
            computer_card = self._computer.draw_card()

            player_cards.append(player_card)
            computer_cards.append(computer_card)

        print("Six hidden cards: XXX XXX")

        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print("-----------------------")
            print("|      Game Over      |")
            print("-----------------------")
            print("You lost - the computer won...")
            return True
        elif self._computer.has_empty_deck():
            print("-----------------------")
            print("|      Game Over      |")
            print("-----------------------")
            print(f"Congratulations, {self._player.name}! You WON!!")
            return True
        else:
            return False

    def print_stats(self):
        print("\n------")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"The computer has {self._computer.deck.size} cards on his deck.")
        print("------")

    def print_welcome_message(self):
        print("=========================")
        print("|     WAR CARD GAME     |")
        print("=========================")


# TEST
deck1 = Deck(True)
deck1.build()
deck1.shuffle()
deck1.show()
