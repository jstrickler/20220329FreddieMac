
# namedtuple
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

values = 5, 19
values = (5, 19)

print("person: {}".format(person))
print("person[0]: {}".format(person[0]))
print(person[0], person[1])

first_name, last_name, product, dob = person   # iterable unpacking
print(first_name, last_name)

a = 23
b = 4
x = divmod(a, b)  #  //, %
print(x)
q, r = divmod(a, b)
print(f"quotient is {q} remainder is {r}")

ip = "192.36.14.99"
byte1, byte2, byte3, byte4 = ip.split('.')
print(byte1)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

for person in people:
    print(person[0], person[1], type(person))
print('-' * 60)

for first_name, last_name, *product, dob in people[-5:]:
    print(first_name, last_name.upper(), product)
print('-' * 60)


