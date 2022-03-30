d1 = dict()  # empty dictionary
d1['blue'] = 5
d1['green'] = 17
d1['purple'] = 9
print("d1: {}\n".format(d1))
d1['blue'] = 37
print("d1: {}\n".format(d1))

states = {'NC': 'North Carolina', 'SC': 'South Carolina'}

data = {}  # empty

#  d = dict(iterable-of-pairs)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'DCA': 'Washington, DC',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Washington, DC',
}

print(airports['YCC'])
print(airports.get('JFK'))
print(airports.get('JFK', 'NOT FOUND'))
print(airports.setdefault('JFK', 'NY-Kennedy'))
print("airports: {}\n".format(airports))

#  DICT.items()
print("airports.items(): {}\n".format(airports.items()))
print()

for abbr, name in airports.items():
    print(abbr, name)
print('-' * 60)

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print('-' * 60)












