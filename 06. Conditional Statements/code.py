# Taking user input for age and converting to integer
a = int(input("Enter your age: "))
print("Your age is:", a)

# Comparison operators: return True if condition is met, False otherwise
print(a > 18)   # True if age is greater than 18
print(a <= 18)  # True if age is less than or equal to 18
print(a == 18)  # True if age equals 18
print(a != 18)  # True if age is not equal to 18

# If-elif-else structure with proper indentation
if a > 18:
    print("You can drive")
elif a >= 60:
    print("You are too old")  # Note: This condition is unreachable if a > 18
else:
    print("You can't drive")
    print("yay")
print("else statement end")  # Outside the if-elif-else block

# Ternary operator: concise if-else
a = 2
b = 330
print("A") if a > b else print("B")  # Prints "B" since a <= b

# Ternary operator with multiple conditions
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")  # Prints "=" since a == b
