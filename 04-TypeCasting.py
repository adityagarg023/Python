# Demonstrating type conversion and implicit type casting in Python

# String concatenation
# Since 'a' and 'b' are strings, the '+' operator concatenates them
a = "3"
b = "4"
print("String concatenation (a + b):", a + b)  # Output: "34"

# Integer addition
# Since 'a1' and 'b1' are integers, the '+' operator performs normal addition
a1 = 3
b1 = 4
print("Integer addition (a1 + b1):", a1 + b1)  # Output: 7

# Explicit type conversion (Type Casting)
# The int() function converts 'a' and 'b' (which are strings) into integers before addition
print("Explicit type conversion (int(a) + int(b)):", int(a) + int(b))  # Output: 7
print("Explicit type conversion (int(a) + a1):", int(a) + a1)  # Output: 6

# Implicit Type Casting
# When performing operations between float and int, Python automatically converts the int to float
c = 2.4   # Float
d = 5     # Integer

# Since 'c' is a float, 'd' is implicitly converted to float, making the result also a float
result = c + d
print("Implicit type casting (c + d):", result, "is of type", type(result))  # Output: 7.4 (float)
