
file_path = 'DATA/wombats.txt'
try:
    with open(file_path) as mary_in:
        for raw_line in mary_in:
            print(raw_line.rstrip())
except (FileNotFoundError, PermissionError) as err:
    print(err, type(err))
print()

food = []
with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food.append(raw_line.rstrip())

try:
    print("food[99]: {}\n".format(food[99]))
except IndexError as err:
    print(err)
print()

nums = [800, 0, 80, -10, 1000, 32, 255, 400, 5, 5000]

for num in nums:
    try:
        result = 12345 / num
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)
    finally:
        print("F")


print("ALL DONE")