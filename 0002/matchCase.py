# ~~~~~~  Python Match Case  ~~~~~
# Introduced in Python 3.10, match case is similar to switch-case in other languages.
# It matches a value against patterns and executes the corresponding block.
# Syntax: match variable: followed by case patterns:

# Basic example: Match a day number to a day name
day = 6
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# Example 2
day = "Monday"
match day:
    case "Monday":
        print(1)
    case "Tuesday":
        print(2)
    case "Wednesday":
        print(3)
    case "Thursday":
        print(4)
    case "Friday":
        print(5)
    case "Saturday":
        print(6)
    case "Sunday":
        print(7)
    case _:
        print("Invalid day")
# ~~~ Match Case Flow ~~~
#        day = 6?
#        /       \
#       /         \
#      1    2    3    4    5    6    7   Other
#      |    |    |    |    |    |    |    |
#    Mon  Tue  Wed  Thu  Fri  Sat  Sun  Invalid

# ~~~ Using Multiple Values per Case ~~~
# Use the | operator to match multiple values for one case.

day = 7
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Office Days")
    case 6 | 7:
        print("Weekends")
    case _:
        print("Invalid day")

# ~~~ Matching with Patterns: Tuples ~~~
# Match case can match complex structures like tuples, lists, and more.

point = (0, 9)
match point:
    case (x, 0):
        print("x-axis:", x)
    case (0, y):
        print("y-axis:", y)
    case (x, y):
        print(f"Point at ({x}, {y})")
    case _:
        print("Invalid point")

# ~~~ Tuple Matching ~~~
#        point = (x, y)
#        /            \
#       /              \
#     (x, 0)        (0, y)        (x, y)   Other
#       |              |             |        |
#     x-axis        y-axis        Point    Invalid

# ~~~ Matching with Conditions (Guards) ~~~
# Add conditions to cases using 'if' for more control.

number = 10
match number:
    case n if n < 0:
        print("Negative number")
    case n if n == 0:
        print("Zero")
    case n if n > 0 and n % 2 == 0:
        print("Positive even number")
    case n if n > 0 and n % 2 != 0:
        print("Positive odd number")
    case _:
        print("Unknown")

# ~~~ Matching Lists ~~~
# Match case works with lists, using similar pattern matching.

items = [1, 2, 3]
match items:
    case [a]:
        print("Single item:", a)
    case [a, b]:
        print("Two items:", a, b)
    case [a, b, c]:
        print("Three items:", a, b, c)
    case _:
        print("Other list pattern")

# ~~~ Matching with Wildcards and Rest ~~~
# Use * to capture remaining elements, similar to unpacking.

values = [1, 2, 3, 4, 5]
match values:
    case [first, *rest]:
        print("First:", first, "Rest:", rest)
    case _:
        print("No match")

# ~~~ Practical Examples ~~~
# Example: HTTP status code handler
status = 404
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown status")

# Example: Command processor
command = ("move", 10, "up")
match command:
    case ("move", distance, direction) if direction in ["up", "down"]:
        print(f"Moving {distance} units {direction}")
    case ("move", distance, direction) if direction in ["left", "right"]:
        print(f"Moving {distance} units {direction}")
    case ("stop",):
        print("Stopping")
    case _:
        print("Invalid command")

# - Use match case for cleaner, more readable code than if-elif-else
# - The _ case is a wildcard, catching unmatched values
# - Combine patterns (tuples, lists) and guards (if) for flexibility
# - Match case is powerful for structured data (e.g., tuples, lists)