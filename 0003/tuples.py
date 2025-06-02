# ~~~ Tuples ~~~
# A tuple is a collection that is ordered and unchangeable (immutable).
# Tuples allow duplicate values and can store multiple data types.

# Creating a tuple
my_tuple = (1, 2, 3, "hello", 5.5)
print("Basic tuple:", my_tuple)

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Single-item tuple (note the comma, as per )
single_item = (42,)
print("Single-item tuple:", single_item)

# Tuple with mixed types
mixed_tuple = (10, "Python", 3.14, True)
print("Mixed types:", mixed_tuple)

# ~~~  Tuple Structure ~~~
#        ( 1 | 2 | 3 | "hello" | 5.5 )
#        ^   ^   ^   ^        ^   ^
#        0   1   2   3        4   5

# ~~~ Accessing Tuple Elements ~~~
# Tuples are indexed, starting at 0. Negative indexing starts from -1 (end).
# Access values using square brackets and indices.

fruits = ("apple", "banana", "cherry", "date")
print("First fruit:", fruits[0])  # apple
print("Last fruit:", fruits[-1])  # date
print("Second to last:", fruits[-2])  # cherry

# ~~~ Slicing Tuples ~~~
# Use slicing to access a range of items.
# Syntax: tuple[start:end:step]
# - start: inclusive, end: exclusive, step: optional increment

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Slice [2:5]:", numbers[2:5])  # (2, 3, 4)
print("Slice from start to 4:", numbers[:4])  # (0, 1, 2, 3)
print("Slice from 6 to end:", numbers[6:])  # (6, 7, 8, 9)
print("Slice with step [::2]:", numbers[::2])  # (0, 2, 4, 6, 8)
print("Reverse tuple [::-1]:", numbers[::-1])  # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

# ~~~  Slicing Visualized ~~~
#        ( 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )
#          ^        ^                   ^
#          0        2                   6
#          Slice [2:6] = (2, 3, 4, 5)

# ~~~ Immutability of Tuples ~~~
# Tuples are unchangeable; you cannot modify, add, or remove items.
# Workaround: Convert to list, modify, then convert back to tuple.

# This would raise an error if uncommented:
# my_tuple[1] = 10  # TypeError: 'tuple' object does not support item assignment

# Convert to list and back ( workaround)
temp_list = list(my_tuple)
temp_list[1] = 10
my_tuple = tuple(temp_list)
print("Modified tuple (via list):", my_tuple)

# ~~~ Tuple Methods ~~~
# : Tuples have two built-in methods due to immutability.

# count() - returns number of occurrences of a value
numbers = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", numbers.count(2))  # 3

# index() - returns first index of a value
print("Index of 3:", numbers.index(3))  # 2

# ~~~ Tuple Operations ~~~

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print("Concatenated tuple:", combined)

# Repetition
repeated = tuple1 * 3
print("Repeated tuple:", repeated)

print("Is 2 in tuple1?", 2 in tuple1)  # True
print("Is 7 in tuple1?", 7 in tuple1)  # False

# Length of tuple
print("Length of combined tuple:", len(combined))

# ~~~  Concatenation ~~~
#        ( 1 | 2 | 3 ) + ( 4 | 5 | 6 )
#        ==================>
#        ( 1 | 2 | 3 | 4 | 5 | 6 )

# ~~~ Tuple Unpacking ~~~
# Unpacking assigns tuple values to variables.

# Basic unpacking
coords = (10, 20, 30)
x, y, z = coords
print("Basic unpacking: x =", x, "y =", y, "z =", z)

# Unpacking with asterisk (*) for variable-length parts
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("Unpacking with *: First:", first, "Middle:", middle, "Last:", last)

# Unpacking with partial asterisk
data = (1, 2, 3, 4, 5, 6)
a, b, *rest = data
print("Unpack first two: a =", a, "b =", b, "Rest:", rest)

# Unpacking nested tuples
nested = (1, (2, 3), 4)
p, (q, r), s = nested
print("Nested unpacking: p =", p, "q =", r, "r =", r, "s =", s)

# Unpacking in a loop
pairs = [(1, "one"), (2, "two"), (3, "three")]
for num, word in pairs:
    print(f"Loop unpacking: Number = {num}, Word = {word}")

# Swapping variables using tuple unpacking
x, y = (10, 20)
x, y = y, x
print("Swapped values: x =", x, "y =", y)

# Unpacking with ignored values using _
point = (5, 10, 15, 20)
x, _, z, _ = point
print("Unpacking with ignored values: x =", x, "z =", z)

# ~~~  Unpacking Visualized ~~~
#        ( 10 | 20 | 30 )
#          ^    ^    ^
#          x    y    z
#        Unpacking: x = 10, y = 20, z = 30

# ~~~ Nested Tuples ~~~
# Tuples can contain other tuples, useful for complex data.

nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print("Nested tuple:", nested_tuple)

# Accessing nested elements
print("Element at [1][2]:", nested_tuple[1][2])  # 6

# ~~~  Nested Tuple ~~~
#        ( ( 1 | 2 | 3 )
#          ( 4 | 5 | 6 )
#          ( 7 | 8 | 9 ) )

# ~~~ Tuples vs. Lists ~~~
# Tuples are immutable, lists are mutable.
# Tuples are faster and can be dictionary keys if no mutable elements.

# Using tuple as a dictionary key
point = (2, 3)
coord_dict = {point: "Origin"}
print("Dictionary with tuple key:", coord_dict)
print("Value for key (2, 3):", coord_dict[(2, 3)])

# - Tuples are ideal for fixed data (e.g., coordinates)
# - Tuples use less memory than lists
# - Built-in functions: len(), min(), max(), sum()

nums = (5, 2, 8, 1, 9)
print("Length:", len(nums))
print("Minimum value:", min(nums))
print("Maximum value:", max(nums))
print("Sum of values:", sum(nums))