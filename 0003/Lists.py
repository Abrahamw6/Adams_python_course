# ~~~ Beginner Level: Understanding Lists ~~~
# A list is a mutable, ordered collection of items, defined with square brackets [].
# Items can be of any type: numbers, strings, booleans, even other lists!

# Creating lists
my_list = [1, 2, 3, "hello", 5.5]
print("Basic list:", my_list)

# Empty list
empty_list = []
print("Empty list:", empty_list)

# Mixed data types
mixed_list = [10, "Python", 3.14, True]
print("Mixed data types:", mixed_list)

# ~~~ A List in Action ~~~
#        [ 1 | 2 | 3 | "hello" | 5.5 ]
#        ^   ^   ^   ^        ^   ^
#        0   1   2   3        4   5

# ~~~ Accessing List Elements ~~~
# Lists use zero-based indexing. 

fruits = ["apple", "banana", "cherry", "date"]
print("First fruit:", fruits[0])  # apple

# Negative indices count from the end (-1 is last).
print("Last fruit:", fruits[-1])  # date
print("Second to last:", fruits[-2])  # cherry

# ~~~ Slicing Lists ~~~
# Syntax: list[start:end:step]
# - start: begin here (inclusive)
# - end: stop here (exclusive)
# - step: jump by this amount

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Slice [2:5]:", numbers[2:5])  # [2, 3, 4]
print("Slice from start to 4:", numbers[:4])  # [0, 1, 2, 3]
print("Slice from 6 to end:", numbers[6:])  # [6, 7, 8, 9]
print("Slice with step [::2]:", numbers[::2])  # [0, 2, 4, 6, 8]
print("Reverse list [::-1]:", numbers[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# ~~~ Slicing Visualized ~~~
#        [ 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ]
#          ^        ^                   ^
#          0        2                   6
#          Slice [2:6] = [2, 3, 4, 5]

# ~~~ Modifying Lists ~~~
# Lists are mutable—change them at will!

# Changing an element
fruits[1] = "blueberry"
print("Modified list:", fruits)

# Adding elements
fruits.append("elderberry")  # Adds to end
print("After append:", fruits)

fruits.insert(2, "coconut")  # Adds at index 2
print("After insert at index 2:", fruits)

fruits.extend(["fig", "grape"])  # Adds multiple items
print("After extend:", fruits)

# ~~~ Removing Elements ~~~
# Remove items with various methods.

fruits.remove("cherry")  # Removes first occurrence
print("After remove 'cherry':", fruits)

last_fruit = fruits.pop()  # Removes and returns last item
print("Popped last element:", last_fruit)
print("List after pop:", fruits)

second_fruit = fruits.pop(1)  # Removes and returns item at index 1
print("Popped element at index 1:", second_fruit)
print("List after pop(1):", fruits)

# Clear all elements
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)

# ~~~ List Methods ~~~
# Built-in methods make lists powerful.

numbers = [10, 20, 30, 20, 40]
print("Index of 20:", numbers.index(20))  # First occurrence
print("Count of 20:", numbers.count(20))  # Number of occurrences

numbers.sort()  # Sort in ascending order
print("Sorted list:", numbers)

numbers.reverse()  # Reverse the order
print("Reversed list:", numbers)

numbers_copy = numbers.copy()  # Shallow copy
print("Copied list:", numbers_copy)

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("Concatenated list:", combined)

# Repetition
repeated = list1 * 3
print("Repeated list:", repeated)

# Membership testing
print("Is 2 in list1?", 2 in list1)
print("Is 7 in list1?", 7 in list1)

# Length
print("Length of combined list:", len(combined))

# ~~~ Concatenation ~~~
#        [ 1 | 2 | 3 ] + [ 4 | 5 | 6 ]
#        ==================>
#        [ 1 | 2 | 3 | 4 | 5 | 6 ]

# ~~~ Advanced Level: List Comprehension ~~~
# Concise way to create lists: [expression for item in iterable if condition]

squares = [x**2 for x in range(6)]
print("Squares using list comprehension:", squares)

even_squares = [x**2 for x in range(6) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# Lists within lists for complex structures like matrices.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)

print("Element at [1][2]:", nested_list[1][2])  # 6

nested_list[0][1] = 20
print("Modified nested list:", nested_list)

# ~~~ Nested List ~~~
#        [ [ 1 | 2 | 3 ]
#          [ 4 | 5 | 6 ]
#          [ 7 | 8 | 9 ] ]

# ~~~ List and Memory ~~~
# Understand shallow vs. deep copying.

import copy
original = [[1, 2], [3, 4]]
shallow_copy = original.copy()  # Shallow copy
deep_copy = copy.deepcopy(original)  # Deep copy

original[0][0] = 99
print("Original after modification:", original)
print("Shallow copy:", shallow_copy)  # Nested list affected
print("Deep copy:", deep_copy)  # Nested list unaffected

# ~~~ Practical Tips ~~~
# - Use min(), max(), sum() for quick calculations
nums = [5, 2, 8, 1, 9]
print("Minimum value:", min(nums))
print("Maximum value:", max(nums))
print("Sum of values:", sum(nums))
