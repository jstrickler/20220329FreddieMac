from john.math import geometry
# from john/math import geometry.py

# find and run geometry.py

a = geometry.circle_area(33)
print("a: {}".format(a))
print(geometry.ANIMAL)

geometry._spam()

# module search algorithm
# 1. current folder
# 2. folders in PYTHONPATH
# 3. standard folders (sys.prefix + '/lib)

