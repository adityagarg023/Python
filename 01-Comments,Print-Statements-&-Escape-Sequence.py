# Example to demonstrate basic print statements and formatting in Python.

# Print a simple message and use \n for a newline within the string.
print ("hello world\nbye world")  # Outputs: hello world (new line) bye world

"""
To create multi-line comments or documentation, use triple single quotes (''' ... ''') 
or triple double quotes (""" ... """).
"""

# Demonstrating the use of escape characters (\) in strings:
# When using double quotes (") for strings, escape any double quotes within the string.
print ("hello there, 'you' are \"stupid\"")  # Outputs: hello there, 'you' are "stupid"

# When using single quotes (') for strings, escape any single quotes within the string.
print ('hello there, \'you\' are "stupid"')  # Outputs: hello there, 'you' are "stupid"

# Demonstrating multiple arguments in a single print statement:
# - Use `sep` to define the separator between multiple arguments.
# - Use `end` to define what is printed at the end of the output.
print ("heyy", 6, 7, 6 * 7, sep="-", end="001\n")
# Outputs: heyy-6-7-42 followed by "001" and a newline.
