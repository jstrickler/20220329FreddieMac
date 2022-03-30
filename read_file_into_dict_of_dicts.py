from pprint import pprint

knight_info = {}
file_name = 'DATA/knights.txt'

with open(file_name) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment, raw_num = line.split(':')
        knight_info[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
            'value': int(raw_num),
        }

pprint(knight_info)

for name, info in knight_info.items():
    print(info['title'], name)
print('-' * 60)

# Galahad's color
print(knight_info['Galahad']['color'])
print(knight_info['Arthur']['quest'])

