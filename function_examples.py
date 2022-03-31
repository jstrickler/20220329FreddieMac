import math

def get_message():
    return "Hello, FreddieMac world"

x = get_message()
print("x: {}".format(x))
print("get_message(): {}\n".format(get_message()))

def display_message():
    message = get_message()
    print(message)

def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return area

def rectangle_area(length, width):
    return length * width

a1 = circle_area(22)
a2 = circle_area(12.9)
a3 = rectangle_area(5, 11.6)
print(a1, a2, a3)

def greet(whom="world"):
    print("Hello,", whom)

greet('Mom')
greet("students")
greet()

def search(keyword, *files, ignore_case=False):
    print("keyword: {}".format(keyword))
    print("files: {}".format(files))

search('bird', 'DATA/alice.txt', 'DATA/parrot.txt')
search('bird')
search('bird', 'DATA/parrot.txt')
search('bird', 'DATA/alice.txt', 'DATA/parrot.txt', ignore_case=True)
def wacky(p1, p2, *p3, spam, ham, **p6):
    print("p1: {}".format(p1))
    print("p2: {}".format(p2))
    print("p3: {}".format(p3))
    print("spam: {}".format(spam))
    print("ham: {}".format(ham))
    print("p6: {}".format(p6))
    print('-' * 10)

wacky(1, 2, spam=3, ham=99)
wacky(1, 2, 3, 4, 5, spam="foo", ham="bar", eggs="scrambled", toast="buttered")








