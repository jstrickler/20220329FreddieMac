from carddeck import CardDeck

class JokerDeck(CardDeck):
    J1 = "1", "** JOKER **"
    J2 = "2", "** JOKER **"

    def _make_deck(self):
        super()._make_deck() # look for method in ancestors
        self._cards.append(self.J1)
        self._cards.append(self.J2)