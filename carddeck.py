import random

# inherits from object
class CardDeck:
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    # instance method
    def __init__(self, dealer_name):
        self.dealer = dealer_name
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = rank, suit
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    # props<TAB> gives you:
    #
    # @property
    # def spam(self):
    #     return self._spam
    #
    # @spam.setter
    # def spam(self, value):
    #     self._spam = value

    def get_dealer(self):
        return self.dealer

    @property
    def dealer(self):
        return self._dealer_name

    @dealer.setter
    def dealer(self, dealer):
        if isinstance(dealer, str):
            self._dealer_name = dealer
        else:
            raise TypeError("Dealer must be a string")

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = 'CardDeck'
        return f"{my_type}: {self.dealer}, {len(self)}"

