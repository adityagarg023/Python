# Demonstrating user input and type casting in Python

# Taking user input (The text inside input() is displayed as a prompt)
a = input("Enter your name: ")
print("My name is", a)

# All user inputs are stored as strings by default, even if they contain numbers
x = input("Enter first number: ")
y = input("Enter second number: ")

# Direct addition of x and y as strings (concatenation)
print("String concatenation (x + y):", x + y)  # If x=3, y=4 → Output: "34"

# Type casting: Converting x and y to integers before performing addition
print("Integer addition (int(x) + int(y)):", int(x) + int(y))  # If x=3, y=4 → Output: 7
