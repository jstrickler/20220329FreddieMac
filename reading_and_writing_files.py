
mary_in = open('DATA/mary.txt', 'r')
mary_in.close()

# read one line at a time
file_path = 'DATA/mary.txt'
mary_data = []
with open(file_path) as mary_in:
    for raw_line in mary_in:  # raw_line is ".......\n"
        line = raw_line.rstrip()  # remove trailing \n
        fields = line.split()
        mary_data.append(tuple(fields))
        print(line)   # print raw_line + "\n"
print('-' * 60)
print(mary_data, '\n')
print('-' * 60)


with open(file_path) as mary_in:
    all_contents = mary_in.read()  # read file into single string
    print("raw:")
    print(repr(all_contents))  # raw view
    print("normal:")
    print(all_contents)
print('-' * 60)

# read entire file into list of strings with newlines
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# read entire file into list of strings without newlines
with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

knights = []
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knights.append(name)
print("knights: {}\n".format(knights))

target = 'x'
word_file = "DATA/words.txt"
word_count = 0
output_file_name = f"{target}_words.txt"
with open(word_file) as words_in:
    with open(output_file_name, 'w') as file_out:
        for line in words_in:
            if line.startswith(target):
                word_count += 1
                file_out.write(line)

print(f"{word_count} words start with {target}")

# file modes
#  'r'  read  (default)
#  'w'  write
#  'a'  append
#  'x'  write if file doesn't exist




