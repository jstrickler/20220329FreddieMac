import math

ANIMAL = 'wombat'

def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return area

def rectangle_area(length, width):
    return length * width

def _spam():
    print("spam spam spam")
