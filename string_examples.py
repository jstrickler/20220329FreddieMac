s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"
print(len(s1), len(s2), len(s3), len(s4), len(s5))

print("Guido's the BDFL-emeritus of Python")
print('Guido is the "BDFL-emeritus" of Python')
print("""Guido's the "BDFL-emeritus" of Python""")

actor = "Chris Hemsworth"
print(actor[0])

print(len(actor), type(actor))

print(actor.upper(), actor.lower(), actor.title(), actor.capitalize())
x = actor.upper()
print(actor)
print(x)
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))

print(actor.startswith('Chris'), actor.startswith('Liam'))
print("Hem" in actor, "Haw" in actor)

print(actor)
print(actor.find('Chris'), actor.find("Hem"), actor.find('Liam'))

print(actor.replace('Chris', 'Liam'))
print(actor.replace('Hem', 'Penny'))
print(actor.replace('worth', ''))

record = "a b c d"
fields = record.split()
print("fields:", fields)

record = 'John:Paul:George:Ringo'
beatles = record.split(':')
print("Beatles:", beatles)

thing_string = "fee\tfi\tfo\tfum"
things = thing_string.split('\t')
print("things:", things)

print('/'.join(beatles))

#  iterable: strings lists tuples dictionaries sets

print('/'.join('abcd'))

s1 = "      Python is the best          "
print("|" + s1.lstrip() + "|")
print("|" + s1.rstrip() + "|")
print("|" + s1.strip() + "|")
print()

salary = "  $  98382,   ,,,"
print(">" + salary.strip('$ ,') + "<")

junk = "$$123"
print(junk.lstrip('$'))

print(junk.replace('$$', ''))

s = '"this is a thing"'
print(s)
s = s.strip('"')
print(s)


