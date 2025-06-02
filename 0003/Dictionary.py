# ~~~ Dictionaries ~~~
# A dictionary is an unordered, mutable collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any type: numbers, strings, lists, even other dictionaries!

# Creating a dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Basic dictionary:", my_dict)

# Empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# Dictionary with mixed value types
mixed_dict = {"id": 1, "title": "Python", "active": True, "scores": [90, 85]}
print("Mixed value types:", mixed_dict)

# ~~~ ASCII Art: Dictionary Structure ~~~
#        { "name" : "Alice" | "age" : 25 | "city" : "New York" }
#           ^        ^          ^       ^      ^          ^
#          key     value      key    value   key       value

# ~~~ Accessing Dictionary Elements ~~~
# Access values using keys (not indices like lists).
# Use square brackets [] or the get() method.

print("Name:", my_dict["name"])  # Access with key
print("Age:", my_dict.get("age"))  # Access with get()
print("Missing key with get:", my_dict.get("country", "Not found"))  # Default value

# ~~~ Modifying Dictionaries ~~~
# Dictionaries are mutable—change, add, or remove key-value pairs.

# Changing a value
my_dict["age"] = 26
print("Modified age:", my_dict)

# Adding a new key-value pair
my_dict["country"] = "USA"
print("After adding country:", my_dict)

# Updating multiple pairs with update()
my_dict.update({"city": "Boston", "job": "Engineer"})
print("After update:", my_dict)

# ~~~ Removing Elements ~~~
# Remove key-value pairs with various methods.

# pop() - removes a key and returns its value
age = my_dict.pop("age")
print("Popped age:", age)
print("Dictionary after pop:", my_dict)

# popitem() - removes and returns the last key-value pair
last_item = my_dict.popitem()
print("Popped last item:", last_item)
print("Dictionary after popitem:", my_dict)

# clear() - removes all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print("After clear:", temp_dict)

my_dict = {"name": "Bob", "age": 30, "city": "Chicago"}

# keys() - returns all keys
print("Keys:", my_dict.keys())

# values() - returns all values
print("Values:", my_dict.values())

# items() - returns key-value pairs as tuples
print("Items:", my_dict.items())

# copy() - creates a shallow copy
dict_copy = my_dict.copy()
print("Copied dictionary:", dict_copy)

# ~~~ Dictionary Operations ~~~
#        { "name" : "Bob" | "age" : 30 | "city" : "Chicago" }
#           ^                 ^                  ^
#          keys()           values()          items()
#          ["name", "age", "city"]  [ "Bob", 30, "Chicago" ]  [("name", "Bob"), ...]

# Looping through keys
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

# Looping through keys and values using items()
for key, value in my_dict.items():
    print(f"Key: {key} -> Value: {value}")

# Membership test (for keys)
print("Is 'name' a key?", "name" in my_dict)
print("Is 'salary' a key?", "salary" in my_dict)

# Length of dictionary
print("Number of key-value pairs:", len(my_dict))

# Basic dictionary comprehension
squares = {x: x**2 for x in range(5)}
print("Squares dictionary:", squares)

# With condition
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}
print("Even squares:", even_squares)

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
paired_dict = {k: v for k, v in zip(keys, values)}
print("Paired dictionary from lists:", paired_dict)

# ~~~ Nested Dictionaries ~~~
# Dictionaries can contain other dictionaries for complex data.

nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}
print("Nested dictionary:", nested_dict)

# Accessing nested values
print("Person1 name:", nested_dict["person1"]["name"])

# Modifying nested values
nested_dict["person2"]["age"] = 31
print("Modified nested dictionary:", nested_dict)

# ~~~ Nested Dictionary ~~~
#        { "person1" : { "name" : "Alice" | "age" : 25 }
#          "person2" : { "name" : "Bob"  | "age" : 31 } }

# ~~~ Dictionary and Memory ~~~
# Understand shallow vs. deep copying for dictionaries.

import copy
original = {"a": 1, "b": [2, 3]}
shallow_copy = original.copy()  # Shallow copy
deep_copy = copy.deepcopy(original)  # Deep copy

# Modify nested list
original["b"][0] = 99
print("Original after modification:", original)
print("Shallow copy:", shallow_copy)  # Nested list affected
print("Deep copy:", deep_copy)  # Nested list unaffected

# - Use get() to avoid KeyError for missing keys
# - Dictionaries are unordered in Python < 3.7; order is preserved in 3.7+
# - Use dict comprehension for concise creation
# - Built-in functions: len(), any(), all()

my_dict = {"a": 0, "b": 1, "c": 2}
print("Length:", len(my_dict))
print("Any true values?", any(my_dict.values()))
print("All true values?", all(my_dict.values()))