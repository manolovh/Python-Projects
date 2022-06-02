class Suit:
    suit_description = {'clubs': '♣',
                        'diamonds': '♦',
                        'hearts': '♥',
                        'spades': '♠', }

    def __init__(self, description):
        self.description = description
        self.symbol = self.suit_description[description]

    def get_description(self):
        return self.description

    def get_symbol(self):
        return self.symbol


class Card:
    special_values = {11: 'Jack',
                      12: 'Queen',
                      13: 'King',
                      14: 'Ace', }

    def __init__(self, suit, value):
        self.suit = Suit(suit)
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def show(self):
        if self.value < 11:
            print(f"Value: {self.value}\nSuit: {self.suit}"
                  f"\nSymbol: {Suit.suit_description[self.suit]}")
        else:
            print(f"Value: {self.special_values[self.value]}\nSuit: {self.suit}"
                  f"\nSymbol: {Suit.suit_description[self.suit]}")

    def is_special(self):
        return True if self.value >= 11 else False


class Deck:
    pass


class Player:
    pass


# TEST
card = Card('hearts', 11)
print(card.is_special())
