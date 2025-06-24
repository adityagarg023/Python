# Taking user input for two numbers and an operator
first = int(input("Enter First Value: "))  # Convert input to integer
second = int(input("Enter Second Value: "))  # Convert input to integer
operator = input("Enter operator: ")  # Operator as string (+, -, *, /)

# Using if-elif-else to perform arithmetic based on operator
if operator == "+":
    print("Value of", first, "+", second, "is", first + second)
elif operator == "-":
    print("Value of", first, "-", second, "is", first - second)
elif operator == "*":
    print("Value of", first, "*", second, "is", first * second)
elif operator == "/":
    print("Value of", first, "/", second, "is", first / second)
else:
    print("Invalid Value or Operator")
