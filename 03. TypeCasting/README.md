# Type Casting

This README contains notes on string concatenation, arithmetic operations, and type casting in Python, as demonstrated in the `code.py` file.

## Topics Covered

### String Concatenation
- When strings are added using the `+` operator, they are concatenated (placed side by side).
  - Example: `"3" + "4"` results in `"34"`, not `7`.
  - Syntax: `a = "3"; b = "4"; print(a + b)` outputs `34`.
- Concatenation only works with strings. Adding a string and a number (e.g., `"3" + 4`) raises a `TypeError`.

### Arithmetic Operations
- For numbers (integers or floats), the `+` operator performs mathematical addition.
  - Example: `3 + 4` results in `7`.
  - Syntax: `a1 = 3; b1 = 4; print(a1 + b1)` outputs `7`.
- The behavior of `+` depends on the data types of the operands:
  - Strings: Concatenation.
  - Numbers: Addition.

### Type Casting
- Type casting converts a value from one data type to another.
- **Explicit Type Casting**:
  - Use functions like `int()` to convert strings to integers.
  - Example: `int("3") + int("4")` converts `"3"` and `"4"` to `3` and `4`, then adds them to get `7`.
  - Syntax: `a = "3"; b = "4"; print(int(a) + int(b))` outputs `7`.
  - Useful when inputs (e.g., from `input()`) are strings but need to be treated as numbers.
- **Implicit Type Casting**:
  - Python automatically converts one data type to another in certain operations.
  - Example: Adding a float and an integer (e.g., `2.4 + 5`) results in a float (`7.4`).
    - The integer `5` is implicitly converted to `5.0` before addition.
  - Syntax: `c = 2.4; d = 5; print(c + d, "is", type(c + d))` outputs `7.4 is <class 'float'>`.
- Type casting enables operations between different data types but requires care to avoid errors (e.g., `int("abc")` raises a `ValueError`).

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Running `code.py` produces:
```
34
7
7
6
7.4 is <class 'float'>
```

Explore the code to reinforce these concepts!
