# Demonstrates basic string printing with newline
# \n is used to move text to the next line
print("hello world\nbye world")

# Multi-line comments are created using triple single or double quotes
"""
This is a multi-line comment.
It can span multiple lines and is useful for detailed explanations.
"""

# Strings can be enclosed in single (') or double (") quotes
# Use \ to escape quotes that match the enclosing type to avoid syntax errors
# No escape needed for opposite quote type
print("hello there, 'you' are \"stupid\"")  # Double quotes enclose, escape "
print('hello there, \'you\' are "stupid"')  # Single quotes enclose, escape '

# Printing multiple items with custom separator and ending
# sep: defines the separator between items (e.g., "-")
# end: defines what is printed at the end (e.g., "001\n")
print("heyy", 6, 7, 6*7, sep="-", end="001\n")
