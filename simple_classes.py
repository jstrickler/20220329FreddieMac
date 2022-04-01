
# colors is an instance (AKA 'object') of the list class
colors = list()
colors.append('blue')
colors.append('pink')
colors.insert(0, 'black')

cities = list()
cities.insert(0, 'Durham')

x = 5   #  x = int(5)
print(type(cities), type(x))
print(x.bit_length())

def spam():
    print("spam!")
print(type(spam))

class Dog:    # UpperCaps  StudlyCaps
    def bark(self):
        print("woof! woof!")

    def pant(self):
        print("pant pant pant")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()
d2.bark()
d3.pant()










