# Variables & Data Types

This README contains notes on Python variables and data types, as demonstrated in the `code.py` file.

## Topics Covered

### Variables
- Variables are used to store data values in Python.
- Assign a value using `=`, e.g., `a = 1236` assigns the integer `1236` to `a`.
- Variables can hold different data types, such as integers, strings, or booleans.
- Python is dynamically typed, meaning no explicit type declaration is needed.
- Variable names are case-sensitive, e.g., `a` and `A` are different variables.

### Data Types
- Python supports various built-in data types, each with specific behaviors:
  - **Integer (`int`)**: Whole numbers, e.g., `1236`.
    - Example: `a = 1236; print(type(a))` outputs `<class 'int'>`.
  - **String (`str`)**: Text enclosed in single (`'`) or double (`"`) quotes, e.g., `"aditya"`.
    - Example: `b = "aditya"; print(type(b))` outputs `<class 'str'>`.
  - **Float (`float`)**: Decimal numbers, e.g., `5.4`.
    - Example: `e = 5.4; print(type(e))` outputs `<class 'float'>`.
  - **Complex (`complex`)**: Numbers with real and imaginary parts, e.g., `6 + 2j`.
    - Example: `f = complex(6, 2); print(f)` outputs `(6+2j)`.
  - **Boolean (`bool`)**: `True` or `False` (case-sensitive).
    - Example: `c = True; print(type(c))` outputs `<class 'bool'>`.
  - **NoneType (`NoneType`)**: Represents the absence of a value, `None` (case-sensitive).
    - Example: `d = None; print(type(d))` outputs `<class 'NoneType'>`.
- Use the `type()` function to check a variable’s data type.
- Operations between different data types (e.g., `int` + `str`) may raise errors unless converted.
  - Example: `print(1236 + "aditya")` raises a `TypeError`.
  - Same-type operations work, e.g., `print(1236 + 5)` outputs `1241`.

### Basic Collections
- Python provides data structures to store multiple values:
  - **List (`list`)**: Ordered, mutable collection of items, which can have mixed types.
    - Example: `list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]`.
    - Output: `[8, 2.3, [-4, 5], ['apple', 'banana']]`.
  - **Tuple (`tuple`)**: Ordered, immutable collection, often used for fixed data.
    - Example: `tuple1 = ("hii", 789)`.
    - Output: `('hii', 789)`.
  - **Dictionary (`dict`)**: Unordered collection of key-value pairs, where keys map to values of any type.
    - Example: `dict1 = {"name": "Aditya", "age": 20, "canvote": True}`.
    - Output: `{'name': 'Aditya', 'age': 20, 'canvote': True}`.
- Collections allow flexible data storage and manipulation.
- Note: In Python, every value (including numbers, strings, and collections) is an object, with associated methods and properties.

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Running `code.py` produces:
```
1236
aditya
1241
Type of a is <class 'int'>
Type of b is <class 'str'>
Type of c is <class 'bool'>
Type of d is <class 'NoneType'>
Type of e is <class 'float'>
Type of f is <class 'complex'>
f = (6+2j)
[8, 2.3, [-4, 5], ['apple', 'banana']]
('hii', 789)
{'name': 'Aditya', 'age': 20, 'canvote': True}
```

Explore the code to reinforce these concepts!
