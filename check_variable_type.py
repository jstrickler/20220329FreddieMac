a = "apple"
b = 1234
c = 9.77

print(isinstance(a, str), isinstance(a, (int, float)))
print(isinstance(b, str), isinstance(b, (int, float)))
print(isinstance(c, str), isinstance(c, (int, float)))
print(type(a), type(a).__name__)

x  = type(b)
print(x)   #  print(str(x))
print(type(x))

m = x(55)
print(m, type(m))

x = 1
x = "abc"
x = 4.7

#  int float bool complex
#  str bytes
#  dict set frozenset
#  nonetype

x = 0
y = 1
print(type(x), type(y))
a = True
b = False
print(type(a), type(b))
x = bool(0)
print(x)


#  str(obj)  -->  human readable string
#  repr(obj) --> code-friendly representation which will reproduce the object

x = 1
y = True
print(int(y))


