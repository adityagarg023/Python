# Assigning and printing an integer
a = 1236
print(a)

# Strings must be enclosed in single or double quotes
b = "aditya"
print(b)

# Different data types cannot be combined in operations like concatenation
# Example: print(a + b) would raise an error
# Same data types can be operated on
a1 = 5
print(a + a1)  # Adds two integers

# Boolean and NoneType values (True/False and None)
# First letter must be capitalized
c = True
d = None

# Using type() to check the data type of variables
print("Type of a is", type(a))  # Integer
print("Type of b is", type(b))  # String
print("Type of c is", type(c))  # Boolean
print("Type of d is", type(d))  # NoneType

# Other data types: float and complex
e = 5.4  # Float
f = complex(6, 2)  # Complex number (6 + 2i)
print("Type of e is", type(e))
print("Type of f is", type(f))
print("f =", f)

# List: Stores multiple values of different types, mutable
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

# Tuple: Similar to list but immutable
tuple1 = ("hii", 789)
print(tuple1)

# Dictionary: Maps keys to values of any type
dict1 = {"name": "Aditya", "age": 20, "canvote": True}
print(dict1)

# Note: In Python, everything is an object
