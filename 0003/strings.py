# ==============================================
#        _____ _        _                 
#       / ____| |      (_)                
#      | (___ | |_ _ __ _ _ __   __ _ ___ 
#       \___ \| __| '__| | '_ \ / _` / __|
#       ____) | |_| |  | | | | | (_| \__ \
#      |_____/ \__|_|  |_|_| |_|__,_|___/
# ==============================================

# ~~~ Strings ~~~
# Strings are used to store text data in Python.
# They are immutable, meaning they cannot be changed after creation.

# Creating strings
single_quote = 'Hello, World!'
double_quote = "Hello, World!"
print("Single quote string:", single_quote)
print("Double quote string:", double_quote)

# Multiline string (using triple quotes)
multi_line = """This is a
multiline
string."""
print("Multiline string:", multi_line)

# ~~~ String Structure ~~~
#        " H e l l o ,   W o r l d ! "
#        ^ ^ ^ ^ ^ ^ ^   ^ ^ ^ ^ ^ ^
#        0 1 2 3 4 5 6   7 8 9 10 11 12

# ~~~ Accessing String Elements ~~~
# Strings are indexed, starting at 0. Negative indexing starts from -1 (end).

text = "Python"
print("First character:", text[0])  # P
print("Last character:", text[-1])  # n
print("Third character:", text[2])  # t

# ~~~ Slicing Strings ~~~
# Syntax: string[start:end:step]
# - start: inclusive, end: exclusive, step: optional increment

phrase = "Hello, World!"
print("Slice [0:5]:", phrase[0:5])  # Hello
print("Slice from start to 5:", phrase[:5])  # Hello
print("Slice from 7 to end:", phrase[7:])  # World!
print("Slice with step [::2]:", phrase[::2])  # Hlo ol!
print("Reverse string [::-1]:", phrase[::-1])  # !dlroW ,olleH

# ~~~ Slicing Visualized ~~~
#        " H e l l o ,   W o r l d ! "
#          ^         ^         ^
#          0         5         7
#          Slice [0:5] = "Hello"

# ~~~ Immutability of Strings ~~~
# Strings are immutable; you cannot change individual characters.
# Workaround: Create a new string with modifications.

# This would raise an error if uncommented:
# text[1] = "X"  # TypeError: 'str' object does not support item assignment

# Create new string
new_text = text[:1] + "X" + text[2:]
print("Modified string (new):", new_text)  # PXthon

# ~~~ Beginner Level: Basic String Operations ~~~
# Strings support concatenation, repetition, and membership tests.

# Concatenation
greeting = "Hello"
name = "Alice"
combined = greeting + " " + name
print("Concatenated string:", combined)

# Repetition
repeated = greeting * 3
print("Repeated string:", repeated)

# Membership testing
print("Is 'H' in greeting?", "H" in greeting)  # True
print("Is 'z' in greeting?", "z" in greeting)  # False

# Length of string
print("Length of combined string:", len(combined))

# ~~~ Concatenation ~~~
#        " H e l l o " + " " + " A l i c e "
#        =====================>
#        " H e l l o   A l i c e "

# ~~~ String Methods ~~~
# Python provides built-in methods for string manipulation (all return new strings).

text = "  Python Programming!  "

# strip() - removes leading/trailing whitespace
print("Stripped:", text.strip())

# lower() - converts to lowercase
print("Lowercase:", text.lower())

# upper() - converts to uppercase
print("Uppercase:", text.upper())

# replace() - replaces a substring
print("Replaced:", text.replace("Python", "Java"))

# split() - splits string into a list by delimiter
words = text.split()
print("Split by space:", words)

# join() - joins list elements into a string
joined = "-".join(words)
print("Joined with '-':", joined)

# find() - returns index of first occurrence (-1 if not found)
print("Index of 'Prog':", text.find("Prog"))

# count() - counts occurrences of a substring
print("Count of 'm':", text.count("m"))

# ~~~ Intermediate Level: String Formatting ~~~
# Format strings to include variables or values.

name = "Bob"
age = 30

# Using % operator
old_style = "My name is %s and I am %d years old." % (name, age)
print("Old-style formatting:", old_style)

# Using str.format()
format_method = "My name is {} and I am {} years old.".format(name, age)
print("str.format():", format_method)

# Using f-strings (Python 3.6+)
f_string = f"My name is {name} and I am {age} years old."
print("f-string:", f_string)

# ~~~ Advanced Level: More String Methods ~~~
# Additional useful methods for advanced manipulation.

text = "Python3.9 is Great!"

# startswith() - checks if string starts with substring
print("Starts with 'Py'?", text.startswith("Py"))  # True

# endswith() - checks if string ends with substring
print("Ends with '!'?", text.endswith("!"))  # True

# isalpha() - checks if all characters are letters
print("Is 'Python' all letters?", "Python".isalpha())  # True

# isdigit() - checks if all characters are digits
print("Is '123' all digits?", "123".isdigit())  # True

# isspace() - checks if all characters are whitespace
print("Is '   ' all whitespace?", "   ".isspace())  # True

# ~~~ String Escape Characters ~~~
# Use backslash (\) to include special characters.
# Common escapes: \n (newline), \t (tab), \" (quote), \\ (backslash)

escaped = "Line1\nLine2\tTabbed\nHe said, \"Hello!\""
print("Escaped characters:")
print(escaped)

# Raw strings (ignore escape characters)
raw = r"Line1\nLine2\tTabbed"
print("Raw string:", raw)

# ~~~ Escape Characters ~~~
#        " L i n e 1 \n L i n e 2 \t T a b b e d "
#        Newline (^)          Tab (^)

# ~~~ String and Memory ~~~
# Strings are immutable, so each operation creates a new string.
# Be mindful of memory for large strings or frequent operations.

original = "Hello"
modified = original + " World"
print("Original string:", original)
print("New modified string:", modified)

# - Strings are immutable: operations create new strings
# - Use f-strings for readable formatting (Python 3.6+)
# - Use strip() to clean user input
# - Built-in functions: len(), min(), max()

chars = "abcXYZ"
print("Length:", len(chars))
print("Minimum (lexicographical):", min(chars))  # a
print("Maximum (lexicographical):", max(chars))  # Z