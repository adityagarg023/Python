# Time Module and Conditional Statements in Python

This README contains notes on using the time module and conditional statements in Python to create time-based greetings, as demonstrated in the `code.py` file.

## Topics Covered

### Time Module
- The `time` module provides functions to work with time in Python.
- `time.strftime(format)` formats the current time as a string based on the specified format.
  - Example: `time.strftime("%H:%M:%S")` returns the current time in `HH:MM:SS` format (e.g., `06:00:00`).
  - Example: `time.strftime("%H")` returns the hour in 24-hour format (e.g., `06` for 6 AM).
- The hour is extracted to determine the appropriate greeting based on the time of day.
- Note: `strftime` returns a string, so conversion to an integer (e.g., `int(time.strftime("%H"))`) is needed for numerical comparisons.

### Conditional Statements
- The `if-elif-else` structure controls program flow based on conditions.
  - **Syntax**:
    ```python
    if condition:
        # Code if condition is True
    elif another_condition:
        # Code if another_condition is True
    else:
        # Code if no conditions are True
    ```
  - In the code, conditions check the hour to select a greeting:
    - `hourstamp < 12`: Outputs `Good Morning` (before 12 PM).
    - `hourstamp < 17`: Outputs `Good Afternoon` (12 PM to 4:59 PM).
    - `hourstamp < 20`: Outputs `Good Evening` (5 PM to 7:59 PM).
    - `else`: Outputs `Good Night` (8 PM or later).
  - Example: If `hourstamp` is `6` (6 AM), `Good Morning` is printed.
- Conditions are evaluated sequentially, and only the first `True` condition’s block is executed.

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. The program will display the current time and a greeting based on the hour.
3. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Example run at 6:00 AM:
```
06:00:00
Good Morning
```

Example run at 3:00 PM:
```
15:00:00
Good Afternoon
```

Example run at 9:00 PM:
```
21:00:00
Good Night
```

Explore the code to reinforce these concepts!
