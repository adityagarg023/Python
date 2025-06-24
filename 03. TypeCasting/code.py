# String concatenation: strings are combined side by side
a = "3"
b = "4"
print(a + b)  # Outputs "34"

# Integer addition: integers are added mathematically
a1 = 3
b1 = 4
print(a1 + b1)  # Outputs 7

# Explicit type casting: converting strings to integers for addition
print(int(a) + int(b))  # Converts "3" and "4" to 3 and 4, outputs 7
print(int(a) + a1)  # Converts "3" to 3, adds to 3, outputs 6

# Implicit type casting: integer is converted to float in float + integer operation
c = 2.4  # Float
d = 5  # Integer
print(c + d, "is", type(c + d))  # Outputs 7.4, type is float
