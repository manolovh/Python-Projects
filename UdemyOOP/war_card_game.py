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


# TEST
deck1 = Deck(True)
deck1.build()
deck1.shuffle()
deck1.show()
