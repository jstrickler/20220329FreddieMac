person = "Batman"
city = "Gotham City"
value = 39.438390233930293

print(person, city)  # str(person) + ' ' + str(city) + '\n'
print(person, city, sep="")
print(person, city, sep="/")
print(person, city, sep="WOMBAT!")
print(person, city.replace(' ', ''))

print(person, end=' ')
# some conditional output here ...
print(city)

print(person, "lives in", city)
#0       1     2
cities = ['Pittsburgh', 'Wheaton', 'Cumberland']
print("{0} lives in {1[0]} {1[1]} {1[2]}".format(person, cities))
print("{} lives in {}".format(city, person))
print(f"{person} lives in {city}")  # same as line 16

s = f"{person} lives in {cities[1]}"
print(s)

print(f"Value is {value}")
print(f"Value is {value:.2f}")
print("Value is {:.2f}".format(value))
number = 23095823095820395820395820398520952039528305982
print(f"Number: {number:,d}")
print(f"Number: {number}")
number =12345
print(f"number: {number:,d}")
# 133,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000









