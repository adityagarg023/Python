# Exercise 1 -- Simple Calculator

This README contains notes on a Python program that implements a basic calculator, as demonstrated in the `code.py` file. The calculator takes two numbers and an operator as input and performs the corresponding arithmetic operation.

## Topics Covered

### User Input
- The `input()` function captures user input as a string.
  - Example: `input("Enter First Value: ")` prompts the user to enter a number.
- Strings are converted to integers using `int()` for arithmetic operations.
  - Example: `first = int(input("Enter First Value: "))` ensures the input is an integer.
- Without conversion, operations like addition would treat inputs as strings, leading to concatenation (e.g., `"2" + "3"` yields `"23"` instead of `5`).
- The calculator uses `input()` to collect two numbers and an operator (`+`, `-`, `*`, `/`).

### Arithmetic Operations
- The calculator supports four basic arithmetic operations:
  - **Addition (`+`)**: Adds two numbers, e.g., `5 + 3` equals `8`.
  - **Subtraction (`-`)**: Subtracts the second number from the first, e.g., `5 - 3` equals `2`.
  - **Multiplication (`*`)**: Multiplies two numbers, e.g., `5 * 3` equals `15`.
  - **Division (`/`)**: Divides the first number by the second, returning a float, e.g., `5 / 2` equals `2.5`.
- The operation is selected based on the user’s operator input.
- Note: Division by zero (e.g., `5 / 0`) will raise a `ZeroDivisionError`, which is not handled in this basic version.

### Conditional Statements
- The `if-elif-else` structure determines which operation to perform based on the operator.
  - **Syntax**:
    ```python
    if condition:
        # Code if condition is True
    elif another_condition:
        # Code if another_condition is True
    else:
        # Code if no conditions are True
    ```
  - Example: `if operator == "+"` checks if the user entered `+` and performs addition.
  - Each `elif` checks for other operators (`-`, `*`, `/`), and the `else` block handles invalid operators.
  - Example: If the user enters `%`, the program outputs `Invalid Value or Operator`.
- Conditional statements enable the calculator to respond dynamically to user input.

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. Follow the prompts to enter two numbers and an operator (`+`, `-`, `*`, `/`).
3. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Example run with inputs `5`, `3`, and `+`:
```
Enter First Value: 5
Enter Second Value: 3
Enter operator: +
Value of 5 + 3 is 8
```

Example run with invalid operator:
```
Enter First Value: 5
Enter Second Value: 3
Enter operator: %
Invalid Value or Operator
```

Explore the code to understand how a simple calculator is built in Python!
