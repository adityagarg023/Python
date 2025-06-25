# User Inputs

This README contains notes on handling user input and type casting in Python, as demonstrated in the `code.py` file.

## Topics Covered

### User Input
- The `input()` function captures user input as a string.
  - Example: `input("Enter your name: ")` displays "Enter your name: " and waits for user input.
  - The input is stored in a variable, e.g., `a = input("Enter your name: ")`.
- The prompt inside `input()` helps guide the user on what to enter.
  - Example: `a = input("Enter your name: ")` followed by `print("My name is", a)` outputs the entered name, e.g., `My name is Aditya`.
- All inputs are strings by default, regardless of what the user types (e.g., numbers or text).

### Type Casting
- Since `input()` returns strings, type casting is needed to treat inputs as other data types (e.g., integers for arithmetic).
- **Explicit Type Casting**:
  - Use `int()` to convert a string to an integer.
  - Example: `x = input("Enter first number: ")` stores a string, but `int(x)` converts it to an integer.
  - Without casting, adding two inputs concatenates them as strings.
    - Example: If `x = "5"` and `y = "3"`, then `x + y` yields `"53"`.
  - With casting, arithmetic operations work as expected.
    - Example: `int(x) + int(y)` for `x = "5"` and `y = "3"` yields `8`.
- Note: Invalid conversions (e.g., `int("abc")`) raise a `ValueError`.

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. Follow the prompts to enter your name and two numbers.
3. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Example run with inputs `Aditya`, `5`, and `3`:
```
Enter your name: Aditya
My name is Aditya
Enter first number: 5
Enter second number: 3
53
8
```

Explore the code to reinforce these concepts!
