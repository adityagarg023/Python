# Demonstrating basic data types and structures in Python

# Integer data type
a = 1236
print("Value of a:", a)

# Strings must be enclosed in double or single quotes
b = "aditya"
print("Value of b:", b)

# Different data types cannot be directly operated together
# Uncommenting the below line will result in an error:
# print(a + b)

# Performing operations on compatible data types
a1 = 5
print("Sum of a and a1:", a + a1)

# Boolean and NoneType values
# Note: 'True' and 'None' must be capitalized
c = True
d = None

# Using type() function to get the data type of a variable
print("Type of a:", type(a))
print("Type of b:", type(b))
print("Type of c:", type(c))
print("Type of d:", type(d))

# Floating-point and complex number types
e = 5.4
f = complex(6, 2)  # A complex number with real part 6 and imaginary part 2

print("Type of e:", type(e))
print("Type of f:", type(f))
print("Value of f:", f)

# Lists: Can store multiple values of different types
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print("List:", list1)

# Tuples: Similar to lists but immutable (cannot be changed after creation)
tuple1 = ("hii", 789)
print("Tuple:", tuple1)

# Dictionaries: Key-value pairs, where keys are mapped to values
dict1 = {"name": "Aditya", "age": 20, "can_vote": True}
print("Dictionary:", dict1)

# In Python, everything is an object!
