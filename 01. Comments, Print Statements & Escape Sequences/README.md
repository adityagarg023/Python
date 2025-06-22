# Comments, Print Statements & Escape Sequences

This README contains notes on fundamental Python concepts related to comments, print statements & escape sequences, as demonstrated in the `code.py` file.

## Topics Covered

### Comments
- **Single-line Comments**: Use `#` to add comments that explain code. Everything after `#` on the same line is ignored by Python.
  - Example: `# This is a single-line comment`
- **Multi-line Comments**: Use triple single (`'''`) or double (`"""`) quotes to create comments spanning multiple lines. These are often used for detailed explanations or documentation.
  - Example:
    ```python
    """
    This is a multi-line comment.
    It can span several lines.
    """
    ```
- Comments improve code readability and are essential for documenting your learning process.

### Print Statements
- The `print()` function outputs text or values to the console.
- **Basic Usage**: `print("hello world")` displays `hello world`.
- **Multiple Items**: Print multiple values by separating them with commas.
  - Example: `print("heyy", 6, 7)` outputs `heyy 6 7`.
- **Custom Separators**: Use the `sep` parameter to define a separator between items.
  - Example: `print("heyy", 6, 7, sep="-")` outputs `heyy-6-7`.
- **Custom Ending**: Use the `end` parameter to specify what appears at the end of the output (default is `\n` for a newline).
  - Example: `print("heyy", end="001\n")` outputs `heyy001` followed by a newline.
- Print statements are versatile for debugging and displaying results.

### Escape Sequences
- Escape sequences use a backslash (`\`) to include special characters in strings.
- **Newline (`\n`)**: Moves output to the next line.
  - Example: `print("hello world\nbye world")` outputs:
    ```
    hello world
    bye world
    ```
- **Escaping Quotes**: Use `\` to include quotes that match the string’s enclosing quotes.
  - In double-quoted strings (`"..."`), escape double quotes: `\"`.
    - Example: `print("hello \"world\"")` outputs `hello "world"`.
  - In single-quoted strings (`'...'`), escape single quotes: `\'`.
    - Example: `print('hello \'world\'')` outputs `hello 'world'`.
  - No escape is needed for opposite quote types (e.g., `'` in `"..."` or `"` in `'...'`.
    - Example: `print("hello 'world'")` outputs `hello 'world'` without escaping.
- Escape sequences allow precise control over string content.

## How to Run
1. Run the `code.py` file in this folder:
   ```bash
   python code.py
   ```
2. Review the code and comments in `code.py` for practical examples of these concepts.

## Example Output
Running `code.py` produces:
```
hello world
bye world
hello there, 'you' are "stupid"
hello there, 'you' are "stupid"
heyy-6-7-42-001
```

Explore the code to reinforce these concepts!
