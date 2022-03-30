from pprint import pprint

knight_info = {}
file_name = 'DATA/knights.txt'

with open(file_name) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment, raw_num = line.split(':')
        knight_info[name] = title, color, quest, comment, int(raw_num)

pprint(knight_info)

for name, info in knight_info.items():
    print(info[0], name)
print('-' * 60)

# Galahad's color
print(knight_info['Galahad'][1])
print(knight_info['Arthur'][2])

