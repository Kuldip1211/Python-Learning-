# Set in Python
# A set is an unordered collection of unique values.
# It automatically removes duplicates.

numbers = {1, 2, 3, 4, 4, 5}
print("Original set:", numbers)

# add() -> adds one element to the set
numbers.add(6)
print("After add(6):", numbers)

# update() -> adds multiple elements from another iterable
numbers.update([7, 8, 9])
print("After update([7, 8, 9]):", numbers)

# remove() -> removes an element
# If the element does not exist, it gives an error.
numbers.remove(2)
print("After remove(2):", numbers)

# discard() -> removes an element
# If the element does not exist, it does not give an error.
numbers.discard(100)
print("After discard(100):", numbers)

# pop() -> removes and returns any one element from the set
removed_value = numbers.pop()
print("Value removed by pop():", removed_value)
print("After pop():", numbers)

# copy() -> creates a copy of the set
numbers_copy = numbers.copy()
print("Copied set:", numbers_copy)

# clear() -> removes all elements from the set
temp_set = {10, 20, 30}
print("Before clear():", temp_set)
temp_set.clear()
print("After clear():", temp_set)

# Union: combines all unique elements from both sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union using | :", set_a | set_b)
print("Union using union():", set_a.union(set_b))

# Intersection: returns common elements
print("Intersection using & :", set_a & set_b)
print("Intersection using intersection():", set_a.intersection(set_b))

# Difference: returns elements present in the first set but not in the second
print("Difference set_a - set_b:", set_a - set_b)
print("Difference using difference():", set_a.difference(set_b))

# Symmetric difference: returns elements that are in one set but not both
print("Symmetric difference:", set_a.symmetric_difference(set_b))

# issubset() -> checks whether all elements of one set are in another set
print("Is set_a a subset of set_b?", set_a.issubset(set_b))

# issuperset() -> checks whether a set contains all elements of another set
print("Is set_a a superset of set_b?", set_a.issuperset(set_b))

# isdisjoint() -> checks whether two sets have no common elements
set_c = {6, 7, 8}
print("Are set_a and set_c disjoint?", set_a.isdisjoint(set_c))

# Example loop: iterate through a set
print("\nLoop through set_a:")
for item in set_a:
	print(item)

# Important note:
# Set elements must be immutable types like numbers, strings, and tuples.
# You cannot store a list or dictionary directly inside a set.
