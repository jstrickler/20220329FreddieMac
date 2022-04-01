fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1: {}\n".format(f1))

f2 = sorted(fruits, key=len)
print("f2: {}\n".format(f2))

def ignore_case(fruit):
    sort_value = fruit.lower()
    print(f"comparing {fruit} as {sort_value}")
    return sort_value

f3 = sorted(fruits, key=ignore_case)
print("f3: {}\n".format(f3))

f4 = sorted(fruits, key=str.lower)
print("f4: {}\n".format(f4))

# fruits.sort(key=str.lower)

def custom_sort(e):
    return len(e), e.lower()   # length, lower-case

f5  = sorted(fruits, key=custom_sort)
print("f5: {}\n".format(f5))

def weird(f):
    print("getting sort key for", f)
    sort_key = f[-1]
    print("sort key is", sort_key)
    print('--')
    return sort_key  # last element of ONE ELEMENT of target list

f6 = sorted(fruits, key=weird)
print("f6: {}\n".format(f6))

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print('-' * 60)

def by_dob(person):
    return person[-1]  # last element of ONE ELEMENT of target list

for person in sorted(people, key=by_dob, reverse=True):
    print(person)
print('-' * 60)

def by_last_name(person):
    return person[1], person[0]

for person in sorted(people, key=by_last_name):
    print(person)
print('-' * 60)

for person in sorted(people, key=lambda p: (p[-1])):
    print(person)
print('-' * 60)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
for name, city in airports.items():
    print(name, city)
print('-' * 60)

for name, city in sorted(airports.items()):
    print(name, city)
print('-' * 60)

for name, city in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(name, city)
print('-' * 60)

def by_value(element):
    return element[1], element[0]

for name, city in sorted(airports.items(), key=by_value):
    print(name, city)
print('-' * 60)
