"""
Day 4: Loop examples in Python.

This file demonstrates different ways to use `for` loops:
1) Basic iteration with `range`
2) `for...else` behavior
3) Iterating over a list by index
4) Using `range(start, stop)`
5) Using `range(start, stop, step)`
6) Using `pass` in an intentionally empty loop body
"""

# ------------------------------------------------------------
# 1) Basic for loop
# Prints numbers from 0 to n-1.
# ------------------------------------------------------------
n = 4
for i in range(0, n):
    print(i)


# ------------------------------------------------------------
# 2) for...else example
# The `else` block executes after the loop finishes normally
# (i.e., when no `break` statement interrupts the loop).
# ------------------------------------------------------------
print("Else in loop")
for i in range(0, 6):
    print(i)
else:
    print("Loop has ended")


# ------------------------------------------------------------
# 3) Loop through a list using index positions
# ------------------------------------------------------------
print("Loop in list")
fruits = ["banana", "apple", "cherry"]

for i in range(len(fruits)):
    print(fruits[i])
else:
    print("Loop has ended")


# ------------------------------------------------------------
# 4) Loop using the start parameter in range(start, stop)
# Prints values from 2 to 5.
# ------------------------------------------------------------
print("Using start parameter")

for i in range(2, 6):
    print(i)
else:
    print("Loop has ended")


# ------------------------------------------------------------
# 5) Loop with step size in range(start, stop, step)
# Prints numbers from 2 to 29, incremented by 3.
# ------------------------------------------------------------
print("Increment the sequence by 3 (default step is 1):")

for x in range(2, 30, 3):
    print(x)
else:
    print("Loop has ended")


# ------------------------------------------------------------
# 6) pass statement
# `pass` is used as a placeholder when a loop (or block) should
# exist syntactically but no action is required yet.
# ------------------------------------------------------------
for x in range(3):
    pass
else:
    print("Loop ended using pass")