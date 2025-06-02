# ~~~ Sequential Execution ~~~
# Python executes code top to bottom, line by line.

print("Hello")
print(456)
print("Hello Again")
print(4569)

# ~~~ Understanding If-Else ~~~
# If-else controls which block of code runs based on a condition.
# Syntax: if condition: (block executes if true) else: (block executes if false)
# Blocks are defined by indentation (no curly braces {} like other languages).

# Basic if example
if True:
    print("It is True")
if False:
    print("It will be skipped because it is not True")

# If-else example
if True:
    print("It is true")
else:
    print("It is false")

# ~~~  If-Else Flow ~~~
#        Condition?
#        /        \
#      True      False
#       /            \
#    Execute        Execute
#    If Block       Else Block

# ~~~ What Are True and False Values? ~~~
# True values: True, any number (except 0), non-empty strings
# False values: False, 0, empty string ("")

# Testing true values
if 4:
    print("It is true: 4 is non-zero")
else:
    print("It is false")

if -4:
    print("It is true: -4 is non-zero")
else:
    print("It is false")

if "hello":
    print("It is true: non-empty string")
else:
    print("It is false")

if True:
    print("It is true: literal True")
else:
    print("It is false")

# Testing false values
if "":
    print("It is true")
else:
    print("It is false: empty string")

if 0:
    print("It is true")
else:
    print("It is false: zero")

if False:
    print("It is true")
else:
    print("It is false: literal False")

# ~~~ Conditions with Comparisons ~~~
# Use comparison operators: >, <, ==, !=, >=, <=

if 4 > 3:
    print("It is true: 4 > 3")
else:
    print("It is false")

if 4 == 4:
    print("It is true: 4 equals 4")
else:
    print("It is false")

if 4 > 4:
    print("It is true")
else:
    print("It is false: 4 not greater than 4")

if 1 == 1.0:
    print("It is true: 1 equals 1.0")
else:
    print("It is false")

# ~~~ If-Elif-Else Ladder ~~~
# Use elif for multiple conditions; only one block executes.
# Checks conditions top to bottom until a true condition is found.

marks = 90
if marks > 90:
    print("A")
elif marks > 80:
    print("B")
elif marks > 70:
    print("C")
elif marks > 55:
    print("D")
else:
    print("Fail")

# ~~~  If-Elif-Else Ladder ~~~
#        marks > 90?
#        /        \
#      True      False
#       /        marks > 80?
#      "A"       /        \
#              True      False
#               /        marks > 70?
#              "B"       /        \
#                     True      False
#                      /        marks > 55?
#                     "C"       /        \
#                            True      False
#                             /        \
#                            "D"      "Fail"

# ~~~ Practical Examples ~~~
# Check if a number is positive, negative, or zero
number = -5
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")

# Check if a string is empty
user_input = ""
if user_input:
    print("You entered:", user_input)
else:
    print("No input provided")

# Nested if-else: Check age and eligibility
age = 20
if age >= 18:
    print("You are an adult")
    if age >= 21:
        print("You can also vote and drink")
    else:
        print("You can vote but not drink")
else:
    print("You are a minor")

# - Use clear, logical conditions
# - Avoid deep nesting for readability; consider combining conditions
# - Use 'and', 'or', 'not' for complex conditions

# Example with logical operators
temperature = 25
if temperature > 30:
    print("It's hot")
elif temperature > 20 and temperature <= 30:
    print("It's warm")
else:
    print("It's cold")
