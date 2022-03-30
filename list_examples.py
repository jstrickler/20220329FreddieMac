list1 = list()
list2 = ['spam', 'ham', 'eggs']
list3 = []

cities = ['Denver', 'Topeka', 'Everett', 'Boston', 'Tampa', 'Annapolis',
          'Sacramento', 'Palm Springs', 'Reno', 'Minneapolis']

cities.insert(0, 'Jacksonville')
cities.insert(5, 'Milwaukee')
print("cities: {}\n".format(cities))
cities.append('Dallas')
cities.append('Baton Rouge')
print("cities: {}\n".format(cities))

more_cities = ['Chicago', 'Pasadena', 'Richmond']
cities.extend(more_cities)
print("cities: {}\n".format(cities))
# print("cities[14][2]: {}\n".format(cities[14][2]))
# print("cities[-1][-2]: {}\n".format(cities[-1][-2]))

#  LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)

del cities[2]
print("cities: {}\n".format(cities))
del cities[-1]
print("cities: {}\n".format(cities))

cities.remove('Everett')
cities.remove('Minneapolis')
print("cities: {}\n".format(cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}\n".format(cities))

city = cities.pop(3)
print("city: {}".format(city))
print("cities: {}\n".format(cities))

#  del LIST[pos]   LIST.remove(value)  LIST.pop(pos=-1)
print("cities[0:3]: {}".format(cities[0:3]))
print("cities[:3]: {}\n".format(cities[:3]))

#  [start=0:stop=len(LIST)]    [start:stop:step]
print("cities[2:5]: {}".format(cities[2:5]))
print("cities[6:]: {}\n".format(cities[6:]))

print("cities[:]: {}\n".format(cities[:]))

c2 = cities  # NOT A COPY OF cities -- it's an ALIAS
c2.append('Bismarck')
print("cities: {}".format(cities))
c3 = cities[:]   # or c3 = list(cities) COPY of cities
c3.append("Madison")
print("cities: {}".format(cities))

c4 = cities
c5 = cities[:]  # or c5 = list(cities)
print(c4 == cities, c5 == cities)
print(c4 is cities, c5 is cities)
if c4 is not cities:
    print("whoo hooo")
# == != > < >= <=  is   is not

s = "You are the brute squad!"
print("s: {}".format(s))
print("s[12:17]: {}".format(s[12:17]))
print("s[:3]: {}\n".format(s[:3]))

print("cities: {}\n".format(cities))

for city in cities:
    # city = next(cities)
    print(city.upper())
print()

for wombat in cities[:5]:
    print(wombat.lower())
print()

for color in "red", "purple", "blue":
    print(color)
print()

print("cities: {}\n".format(cities))

some_cities = ['Durham', 'Palm Springs', 'St. John', 'Denver']

for city in some_cities:
    print(city, city not in cities)
print()

t1 = 'a', 'b', 'c'
t2 = 'd', 'e', 'f'
t3 = t1 + t2
print("t3: {}".format(t3))

x = "py"
y = "thon"
language = x + y
print(language)



