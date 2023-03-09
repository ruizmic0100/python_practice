# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three"s, and are often used
    as documentation.

"""

# 1. Primitive Datatypes and Operators

# You have numbers
3 # => 3

# Math is what you would expect
1 + 1 # => 2
8 - 1 # => 7
10 * 2 # => 20
35 / 5 # => 7.0

# Integer division rounds down for both positive and negative numbers.
5 // 3 # => 1
-5 // 3 # => -2
5.0 // 3.0 # => 3.0
-5.0 // 3.0 # => -2.0

# The result of division is always a float
10.0 / 3 # 3.3333333333335

# Modulo operation
7 % 3 # => 1
# i % j have the same sign as j, unlike c
-7 % 3 # => 2

# Exponentiation (x**y, x to the yth power)
2**3 # => 8

# Enforce precedence with parentheses
1 + 3 *2 # => 7
(1 + 3) * 2 # 8

# Boolean values are primitives (Note: the capitalization)
True # => True
False # => False

# negate with not
not True # => False
not False # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False # => False
False or True # => True

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8 # => 8
False - 5 # => -5

# Comparison operators look at the numerical value of True and False
0 == False # => True
1 == True # => True
2 == True # => False
-5 != False # => True

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False.
# All other values are True
bool(0) # => False
bool("") # => False
bool([]) # => False
bool({}) # => False
bool(()) # => False
bool(set()) # => False
bool(4) # => True
bool(-6) # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&,|)
bool(0) # => False
bool(2) # => True
0 and 2 # => 0
bool(-5) # => True
bool(2) # => True
-5 or 0 # => -5

# Equality is ==
1 == 1 # => True
2 == 1 # => False

# Inequality is !=
1 != 1 # => False
2 != 1 # => True

1 < 2 and 2 < 3 # => True
2 < 3 and 3 < 2 # => False
# Chaining makes this look nicer
1 < 2 < 3 # => True
2 < 3 < 2 # => False

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4] # Pointed a at a new list, [1, 2, 3, 4]
b = a            # Point b at what a is pointing to
b is a           # => True, a and b refer to the same object
b == a           # => True, a's and b's objects are equal


# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too
"Hello " + "world!" # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
"Hello " "world!" # => "Hello world!"

# A string can be treated like a list of characters
"Hello world!"[0] # => 'H'

# You can find the length of a string
len("This is a string") # => 16

# since Python3.6, you can use f-strings or formatted string literals.
name = "Reiko"
f"She said her name is {name}." # => "She said her name is Reiko"
# any valid python expression inside these braces is returned to the string.
f"{name} is {len(name)} characters long." # => "Reiko is 5 characters long."

# None is an object
None # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for eqaulity of object identity.
