x=5
print(type(x))


#spme more data types
x = str("Hello World")
x = int(20)
x = float(20.5)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)











#EXAMPLE OF ONE TYPE CONVERSION TO OTHER
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))