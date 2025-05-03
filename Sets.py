# Python Sets - Comprehensive Notes

# Overview
# A set is a built-in data structure in Python that stores unique elements.
# Sets are unordered, mutable, and do not allow duplicate values.
# Sets are useful for operations like removing duplicates, membership testing, and mathematical operations (union, intersection, etc.).

# Creating a Set
# Sets are created using curly braces {} or the set() constructor.
mySet = {1, 2, 3, 4, 5, 6, 6, 4, 2}  # Duplicates are automatically removed
print("Initial Set:", mySet)  # Output: {1, 2, 3, 4, 5, 6}

# Converting a List to a Set
myList = [100, 30, 30, 100]
myListSet = set(myList)  # Converts list to set, removes duplicates
print("List to Set:", myListSet)  # Output: {100, 30}

# Set Methods and Operations

# 1. Adding Elements
# add() - Adds a single element to the set
mySet.add(200)  # Adds 200 to the set
print("After add(200):", mySet)
mySet.add(-100)  # Adds -100 to the set
print("After add(-100):", mySet)

# Example: Adding a string to a set
exampleSet = {1, 2, 3}
exampleSet.add("hello")
print("Adding string to set:", exampleSet)  # Output: {1, 2, 3, 'hello'}

# 2. Updating with Multiple Elements
# update() - Adds multiple elements from an iterable (list, set, etc.)
mySet20 = {11, 24, 66, 40, 26}
mySet.update(mySet20)  # Adds elements from mySet20
print("After update with mySet20:", mySet)
mySet.update([300, 400])  # Adds elements from a list
print("After update with list [300, 400]:", mySet)

# Example: Updating with a tuple
exampleSet.update((4, 5))
print("Updating with tuple (4, 5):", exampleSet)  # Output: {1, 2, 3, 4, 5, 'hello'}

# 3. Removing Elements
# discard() - Removes a specific element; no error if element is not present
mySet.discard(3)  # Removes 3
print("After discard(3):", mySet)
mySet.discard(999)  # No error for non-existent element
print("After discard(999):", mySet)

# remove() - Removes a specific element; raises KeyError if element is not present
mySet.remove(4)  # Removes 4
print("After remove(4):", mySet)
# mySet.remove(999)  # Would raise KeyError

# pop() - Removes and returns a random element; raises KeyError if set is empty
popped_element = mySet.pop()
print("Popped element:", popped_element)
print("After pop():", mySet)

# clear() - Removes all elements from the set
mySet.clear()
print("After clear():", mySet)  # Output: set()

# del - Deletes the entire set
del mySet
# print(mySet)  # Would raise NameError

# 4. Copying a Set
# copy() - Creates a shallow copy of the set
mySet = {1, 2, 3, 4, 5}
mySet2 = mySet.copy()
print("Copied set:", mySet2)
mySet2.add(10)  # Modifying copy does not affect original
print("Original set:", mySet)
print("Modified copy:", mySet2)

# Set Operations

# 1. Union
# Combines elements from two sets, removing duplicates
mySet3 = {34, 25, 67, 89, 80}
mySet4 = {134, 205, 667, 9, 80, 25}
union_set = mySet3.union(mySet4)  # Using union() method
print("Union (method):", union_set)
union_set_operator = mySet3 | mySet4  # Using | operator
print("Union (operator):", union_set_operator)

# Example: Union with identical sets
mySet5 = {34, 25, 67, 89, 80}
print("Union with identical set:", mySet3.union(mySet5))  # Same as mySet3

# 2. Intersection
# Returns common elements between two sets
intersection_set = mySet3.intersection(mySet4)  # Using intersection() method
print("Intersection (method):", intersection_set)  # Output: {25, 80}
intersection_set_operator = mySet3 & mySet4  # Using & operator
print("Intersection (operator):", intersection_set_operator)

# Example: Intersection with identical sets
print("Intersection with identical set:", mySet3.intersection(mySet5))  # Same as mySet3

# 3. Difference
# Returns elements in the first set that are not in the second set
difference_set = mySet3.difference(mySet4)
print("Difference (mySet3 - mySet4):", difference_set)  # Output: {89, 34, 67}

# 4. isdisjoint()
# Returns True if two sets have no common elements
mySet6 = {134, 205, 667}
print("Is mySet3 disjoint with mySet4?:", mySet3.isdisjoint(mySet4))  # False (due to 25, 80)
print("Is mySet3 disjoint with mySet6?:", mySet3.isdisjoint(mySet6))  # True (no common elements)

# Special Cases: True, False, 1, 0
# In Python, True == 1 and False == 0, so sets treat them as duplicates
mySet11 = {True, False}
print("Set with True, False:", mySet11)  # Output: {False, True}

mySet12 = {True, 1, False}
print("Set with True, 1, False:", mySet12)  # Output: {False, True} (1 is treated as True)

mySet13 = {True, False, 0}
print("Set with True, False, 0:", mySet13)  # Output: {True, False} (0 is treated as False)

mySet14 = {True, 1, False, 0}
print("Set with True, 1, False, 0:", mySet14)  # Output: {False, True}

mySet15 = {1, True, False, 0}
print("Set with 1, True, False, 0:", mySet15)  # Output: {False, True}

mySet16 = {1, True, 0, False}
print("Set with 1, True, 0, False:", mySet16)  # Output: {False, True}

mySet17 = {1, True, 1.0, 0, False}
print("Set with 1, True, 1.0, 0, False:", mySet17)  # Output: {False, True} (1.0 is treated as True)

# Additional Notes
# - Sets are unordered, so you cannot access elements by index.
# - Sets are mutable, but elements inside a set must be immutable (e.g., numbers, strings, tuples).
# - Frozen sets (frozenset) are immutable sets: frozenset({1, 2, 3}).
# - Use sets for efficient membership testing (e.g., 'in' operator) and removing duplicates.
