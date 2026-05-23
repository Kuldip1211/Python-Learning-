"""
Functions: Basic Concepts in Python

A function is a reusable block of code that runs when it is called.
Functions are used to organize code, avoid repetition, and make code more maintainable.
"""

# ================================================================
# 1) FUNCTION DECLARATION
# Definition: A function is declared using the 'def' keyword followed by
# a name, parentheses (), and a colon. The code inside is the function body.
# ================================================================
def my_function():
    """This function prints a greeting message."""
    print("Hello World Function")

# ================================================================
# 2) CALLING A FUNCTION
# Definition: You call a function by writing its name followed by ()
# This executes all the code inside the function body.
# ================================================================
my_function()  # Executes the function and prints the message

# ================================================================
# 3) RETURN VALUES
# Definition: The 'return' keyword sends a value back to the caller.
# A function can either print output (print) or return a value (return).
# Print shows output on screen, return allows you to use the value elsewhere.
# ================================================================
def get_greeting():
    """This function returns a greeting string."""
    return "Hello World"

# Store the returned value in a variable
greeting = get_greeting()

# Print the returned value
print(greeting)

# ================================================================
# 4) EMPTY FUNCTION WITH PASS
# Definition: In Python, function bodies cannot be empty syntactically.
# Use 'pass' as a placeholder when you have no code yet.
# 'pass' does nothing; it's a no-op statement used for future implementation.
# ================================================================
def pass_function():
    """This is a placeholder function with no implementation yet."""
    pass  # Placeholder - function body is empty but valid


# ================================================================
# 5) VARIABLE SCOPE: GLOBAL AND NONLOCAL
#
# GLOBAL:
# Definition: A global variable is declared at the module level (outside functions).
# Use the 'global' keyword inside a function to modify a global variable.
#
# NONLOCAL:
# Definition: 'nonlocal' refers to a variable in the nearest enclosing scope.
# Use 'nonlocal' in an inner function when you need to modify a variable
# from an outer (enclosing) function.
# ================================================================

# EXAMPLE: Using nonlocal to modify an outer function's variable
# The inner() function modifies 'x' from the outer() function using nonlocal
def outer():
    """Outer function with a local variable x."""
    x = 10

    def inner():
        """Inner function that modifies the outer function's variable."""
        nonlocal x  # Reference the 'x' from the enclosing outer() function
        x = 20      # Change x's value to 20
        print("Inner:", x)

    inner()     # Call inner function, which changes x to 20
    print("Outer:", x)  # Print x, which is now 20 (nonlocal updated it)

outer()  # Output: Inner: 20, Outer: 20