# String variables
name = "Aditya"
friend = "Yash"
another = "Rohan"

# String concatenation: + adds no space, , adds a space
print("Hello, " + name)  # Concatenates without space
print("Hello, ", name)   # Comma adds a space

# Multi-line strings using triple quotes
apple = '''He said,
"I want to eat an apple"'''
print(apple)

# String indexing: accessing characters by index (0-based)
print(name[1])  # Second character
print(name[4])  # Fifth character

# String slicing: extracting a portion of a string
names = "Aditya,Daksh"
print(names[0:5])   # From index 0 to 4
print(names[-2:3])  # Negative indexing, empty result
print(names[-3:-1]) # From third-to-last to second-to-last
print(names[-1:-3]) # Invalid range, empty result
print(names[5:3])   # Invalid range, empty result

# String length
print(len(names))

# String immutability: strings cannot be modified, operations create new strings

# String methods
a = "! !Aditya!! !!!"
print(a.upper())           # Convert to uppercase
print(a.lower())           # Convert to lowercase
print(a.rstrip("!"))       # Remove trailing "!"
print(a.replace("Adi", "Dak"))  # Replace "Adi" with "Dak"
print(a.split(" "))        # Split at spaces into a list

s = "welcoME To tHe coNSolE"
print(s.capitalize())      # Capitalize first character, lowercase rest
print(len(s))              # Length of string
print(s.center(50))        # Center string with 25 spaces on each side
print(len(s.center(50)))   # Length of centered string
print(s.count("o"))        # Count occurrences of "o"
print(s.endswith("E"))     # Check if string ends with "E"
print(s.endswith("s", 4, 10))  # Check if slice from index 4 to 9 ends with "s"
print(s.find("co"))        # Index of first "co" occurrence
print(s.find("to"))        # Index of first "to" occurrence (-1 if not found)
print(s.isalnum())         # Check if string is alphanumeric (false due to spaces)
print(s.isalpha())         # Check if string is alphabetic (false due to spaces)
print(s.islower())         # Check if all characters are lowercase
print(s.isupper())         # Check if all characters are uppercase

# Check if string is printable (no non-printable characters like \t, \n)
b = "Hello,\nkiddo"
print(s.isprintable())     # True, no non-printable characters
print(b.isprintable())     # False, contains \n

# Check if string contains only whitespace (spaces, tabs, etc.)
space = "        "
print(b.isspace())         # False, contains non-whitespace
print(space.isspace())     # True, contains only spaces

# Check if string is title case (first letter of each word capitalized)
print(names.istitle())     # False, not title case
print(s.istitle())         # False, not title case
print(s.startswith("we"))  # Check if string starts with "we"
print(s.swapcase())        # Swap uppercase and lowercase
print(s.title())           # Capitalize first letter of each word
