from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Nelly')

#  shuffle, deal, etc
# naughty!
# print(d1._dealer_name)

d2 = CardDeck('Andy')
# print(d2._dealer_name)

print(d1.get_dealer()) #  getter method
print(d1.dealer) #  getter property
d = d1.dealer

d1.dealer = "Little Bear"  # setter property
print(d1.dealer)

try:
    d1.dealer = 89.7
except TypeError as err:
    print(err)
else:
    print(d1.dealer)
print(d1.dealer)

d1.shuffle()
print(d1.cards)
print()
for i in range(5):
    print(d1.draw())

print(len(d1))

print(d1)
# <CardDeck: Nelly, 47>
print('-' * 60)
j = JokerDeck("Bonnie")
j.shuffle()
print(j.dealer)
print(j.cards)

