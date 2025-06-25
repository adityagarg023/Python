# String Operations

This README contains notes on string concatenation, indexing, slicing, immutability, and string methods in Python, as demonstrated in the `code.py` file.

## Topics Covered

### String Concatenation
- Strings can be combined using the `+` operator or commas in `print()`.
  - Using `+` concatenates without adding spaces.
    - Example: `"Hello, " + "Aditya"` outputs `Hello,Aditya`.
  - Using commas in `print()` adds a space between arguments.
    - Example: `print("Hello, ", "Aditya")` outputs `Hello, Aditya`.
- Multi-line strings are created using triple quotes (`'''` or `"""`), preserving line breaks and formatting.
  - Example: `'''He said,\n"I want to eat an apple"'''` outputs:
    ```
    He said,
    "I want to eat an apple"
    ```

### String Indexing and Slicing
- **Indexing**: Access individual characters using zero-based indices.
  - Example: For `name = "Aditya"`, `name[1]` outputs `d` and `name[4]` outputs `y`.
- **Slicing**: Extract a substring using `[start:end]` or `[start:end:step]`.
  - Example: For `names = "Aditya,Daksh"`, `names[0:5]` outputs `Adity`.
  - Negative indices count from the end (e.g., `-1` is the last character).
    - Example: `names[-3:-1]` outputs `sh`.
  - Invalid ranges (e.g., `names[-1:-3]` or `names[5:3]`) return an empty string.
- The `len()` function returns the string’s length.
  - Example: `len("Aditya,Daksh")` outputs `12`.

### String Immutability
- Strings in Python are immutable, meaning they cannot be modified in place.
- Operations like `upper()` or `replace()` create new strings rather than altering the original.
  - Example: `"Aditya".upper()` returns `"ADITYA"`, but `"Aditya"` remains unchanged.

### String Methods
- Python provides built-in methods to manipulate strings:
  - `upper()`: Converts to uppercase, e.g., `"Aditya".upper()` outputs `ADITYA`.
  - `lower()`: Converts to lowercase, e.g., `"Aditya".lower()` outputs `aditya`.
  - `rstrip(chars)`: Removes trailing characters, e.g., `"!Aditya!!".rstrip("!")` outputs `!Aditya`.
  - `replace(old, new)`: Replaces substrings, e.g., `"!Aditya!".replace("Adi", "Dak")` outputs `!Daktya!`.
  - `split(delimiter)`: Splits string into a list, e.g., `"! !Aditya!".split(" ")` outputs `['!', '', 'Aditya!']`.
  - `capitalize()`: Capitalizes first character, lowercases rest, e.g., `"welcoME".capitalize()` outputs `Welcome`.
  - `center(width)`: Centers string with spaces, e.g., `"welcoME".center(50)` adds spaces to make length 50.
  - `count(sub)`: Counts occurrences, e.g., `"welcoME".count("o")` outputs `2`.
  - `endswith(sub)`: Checks if string ends with substring, e.g., `"welcoME".endswith("E")` outputs `True`.
  - `endswith(sub, start, end)`: Checks slice, e.g., `"welcoME".endswith("s", 4, 10)` outputs `False`.
  - `find(sub)`: Returns index of first occurrence or `-1`, e.g., `"welcoME".find("co")` outputs `3`.
  - `isalnum()`: Checks if string is alphanumeric, e.g., `"welcoME To".isalnum()` outputs `False` (due to space).
  - `isalpha()`: Checks if string is alphabetic, e.g., `"welcoME".isalpha()` outputs `False` (due to space).
  - `islower()`: Checks if all cased characters are lowercase, e.g., `"welcoME".islower()` outputs `False`.
  - `isupper()`: Checks if all cased characters are uppercase, e.g., `"welcoME".isupper()` outputs `False`.
  - `isprintable()`: Checks if all characters are printable, e.g `\n` makes `"Hello,\nkiddo".isprintable()` `False`.
  - `isspace()`: Checks if string contains only whitespace, e.g., `"    ".isspace()` outputs `True`.
  - `istitle()`: Checks if string is title case, e.g., `"Aditya,Daksh".istitle()` outputs `False`.
  - `startswith(sub)`: Checks if string starts with substring, e.g., `"welcoME".startswith("we")` outputs `True`.
  --

System: It looks like your message was cut off at the end, as the `README.md` content appears incomplete (ending mid-sentence with `e.g., `"welcoME".startswith("we")` outputs `True`. --`). I'll assume you intended to include all the string methods listed in the code and complete the `README.md` accordingly, ensuring it covers all topics (String Concatenation, String Indexing and Slicing, String Immutability, and String Methods) with a focus on the full set of string methods from the code. I'll also include the `swapcase()` and `title()` methods, which were mentioned in the code but may have been intended for the README's string methods section.

Below are the finalized artifacts for `string_operations/code.py` (unchanged from your provided code, as it was complete) and `string_operations/README.md` (completed to include all string methods and formatted consistently with previous READMEs). Since the code was already provided and the README is being finalized, I'll use the same artifact ID for `code.py` as in my previous response and assign a new artifact ID for the completed `README.md`.

###Artifact for `string_operations/code.py`
<xκεArtifact artifact_id="e8f0b2a1-7e3b-4a4c-9f7b-3a4e6e2c1d5a" artifact_version_id="b1c2d3e4-5f6g-7h8i-9j0k-1l2m3n4o5p6q" title="string_operations/code.py" contentType="text/python">
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
