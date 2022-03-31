andy_countries = ['Spain', 'Tuvalu', 'Burkina Faso', 'Laos',
                  'India', 'Canada', 'Japan', 'Spain', 'Spain',
                  'Brazil', 'Belgium', 'Eritrea', 'Turkmenistan']

nellie_countries = ['Japan', 'Burkina Faso', 'India', 'Japan',
                    'Spain', 'Mexico', 'Argentina', 'Belgium', 'Brazil',
                    'Portugal']
andy = set(andy_countries)
andy_unique = list(andy)
nellie = set(nellie_countries)
print("andy: {}".format(andy))
print("nellie: {}\n".format(nellie))

print("Common:", andy & nellie)  # intersection
print("Not common:", andy ^ nellie) # Xor
print("All:", andy | nellie)  # union
print("Andy only:", andy - nellie)
print("Nellie only:", nellie - andy)

s = "You are the brute squad"
print("sorted(set(s)): {}\n".format(sorted(set(s))))

m = set()
m.add('foo')
m.add('bar')
m.add('bar')
m.add('foo')
m.add('baz')
m.add('spam')
m.add('foo')
print("m: {}\n".format(m))

fruits = ['Apple', 'APPLE', 'peach', 'Peach', 'pear', 'PEAR', 'pear', 'kiwi']
fruit_set1 = set()
for fruit in fruits:
    fruit_set1.add(fruit.lower())
print("fruit_set1: {}\n".format(fruit_set1))

unique_fruits = {}
for fruit in fruits:
    key = fruit.lower()
    if key not in unique_fruits:
        unique_fruits[key] = list()
    unique_fruits[key].append(fruit)

print("unique_fruits: {}\n".format(unique_fruits))

print("unique_fruits.keys(): {}\n".format(unique_fruits.keys()))











