# Conditional Statements

This README contains notes on conditional statements, comparison operators, and the ternary operator in Python, as demonstrated in the `code.py` file.

## Topics Covered

### Conditional Statements
- Conditional statements control program flow based on conditions using `if`, `elif`, and `else`.
  - **Syntax**:
    ```python
    if condition:
        # Code if condition is True
    elif another_condition:
        # Code if another_condition is True
    else:
        # Code if no conditions are True
    ```
  - Indentation (typically 4 spaces) defines the block of code under each condition.
    - Example: 
      ```python
      if a > 18:
          print("You can drive")
      ```
      Outputs `You can drive` if `a` is greater than 18.
  - `elif` (short for "else if") checks additional conditions if the previous ones are False.
  - `else` runs if no conditions are True.
    - Example: For `a = 17`, `else` block outputs `You can't drive` and `yay`.
  - All statements in an indented block are executed together.
  - Note: In the code, `elif a >= 60` is unreachable if `a > 18` is True, as conditions are checked sequentially.

### Comparison Operators
- Comparison operators evaluate conditions and return `True` or `False`:
  - `>`: Greater than, e.g., `a > 18` returns `True` if `a` is 19.
  - `<=`: Less than or equal to, e.g., `a <= 18` returns `True` if `a` is 18.
  - `==`: Equal to, e.g., `a == 18` returns `True` if `a` is 18.
  - `!=`: Not equal to, e.g., `a != 18` returns `True` if `a` is not 18.
- These operators are used in conditional statements or printed directly.
  - Example: `print(a > 18)` outputs `True` or `False` based on `a`.

### Ternary Operator
- The ternary operator provides a concise way to write simple `if-else` statements.
  - **Syntax**: `value_if_true if condition else value_if_false`
  - Example: `print("A") if a > b else print("B")` prints `A` if `a > b`, otherwise `B`.
  - Multiple conditions can be chained:
    - Example: 
      ```python
      print("A") if a > b else print("=") if a == b else print("B")
      ```
      Outputs `=` if `a == b`, `A` if `a > b`, or `B` if `a < b`.
- Useful for short, single-expression decisions.

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. Follow the prompt to enter your age.
3. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Example run with input `20`:
```
Enter your age: 20
Your age is: 20
True
False
False
True
You can drive
else statement end
B
=
```

Example run with input `17`:
```
Enter your age: 17
Your age is: 17
False
True
False
True
You can't drive
yay
else statement end
B
=
```

Explore the code to reinforce these concepts!
