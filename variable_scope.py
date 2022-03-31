
x = 100  # global variable (aka name)

def spam():
    x = 50  # bad practice!!
    animal = "wombat"  # local name (aka variable)
    print("In spam(), x is", x)
    return x

value = spam()
# print("animal: {}".format(animal))
print("x: {}".format(x))
print("value: {}".format(value))

def doit(data):
    data.append("got you!")

bears = ['grizzly', 'black', 'spectacled']
doit(bears)
print("bears: {}".format(bears))
b = bears #  alias, not copy
