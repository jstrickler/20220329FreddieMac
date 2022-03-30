fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

print(len(fruits), len(nums))
print(min(fruits), min(nums))
print(max(fruits), max(nums))
print(sum(nums))
print(sorted(fruits))
print(sorted(nums))

print("fruits: {}\n".format(fruits))

rev_fruits = reversed(fruits)
print(rev_fruits)
for fruit in rev_fruits:
    print(fruit)
print('-' * 60)

name = "Robert"
for char in reversed(name):
    print(char)

print("nums: {}".format(nums))

numbered_fruits = zip(nums, fruits)
print(numbered_fruits)
print(list(numbered_fruits))
numbered_fruits = zip(nums, fruits)
for number, fruit in numbered_fruits:
    print(f"{number:4d} {fruit}")

values = ['a', 'b', 'c', 'd']
for i, value in enumerate(values):
    print(i, value)
print()
print(list(enumerate(values)))
print()

for i, value in enumerate(values, 1):
    print(i, value)
print()

#  range(stop)  range(start, stop)  range(start, stop, step)

for i in range(5):
    print(i)
print()

for i in range(1, 6):
    print(i, i ** 2, i ** 3)
print()

for i in range(10):
    print("Python! Python! for the win!")

