
counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        if food in counts:
            counts[food] += 1  # counts[food] = counts[food] + 1
        else:
            counts[food] = 1   # first time for this food

print("counts: {}".format(counts))
