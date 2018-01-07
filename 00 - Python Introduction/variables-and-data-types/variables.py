# VARIABLES AND DATA TYPES

# Objectives:
#  - Understand how to assign and use varables
#  - Learn about the different data types
#  - Learn why Python is called a dynamically-typed language

# DECLARING VARIABLES
a = 3
b = "STRING"
nothing = None

# Multiple Assignment
a, b = 1, 2

# Naming Requirements
#   1. Variables in Python are required to start with a letter or an underscore.
#   2. The rest of the name must consist of letters, numbers, or underscores
#   3. Names are case-sensitive

# Valid:
_cats = "meow"
abc123 = 1970

# Invalid:
2cats = 1 # SyntaxError
hey@you = 1 # SyntaxError

# NAMING CONVENTIONS
#   Most variable names should be written in `lower_snake_case`
#   `CAPITAL_SNAKE_CASE` usually refers to constants
#   UpperCamelCase usually refers to a class
#   Variables that start with and end with two underscores are intended to be private or are builtins:
myVariable = 3 # this isn't JavaScript!
my_variable = 3 # much better
AVOGADRO_CONSTANT = 6.022140857 * 10 ** 23
__no_touchy__ = 3 # someone doesn't want you to mess with this!


# DATA TYPES IN PYTHON
#   bool = `True` or `False`
#   int = an integer
#   float = a decimal number
#   str = a UNICODE string
#   list = an ordered collection of other types
#   dict = a dictionary aka unordered collection of key:value entries
# We can see the type of an object using the built in `type` function:
type(False) # bool
type("nice") # str
type({}) # dict
type([]) # list
type(()) # tuple
type(None) # NoneType
# Note: Python has no concept of "primitives" like JavaScript. In JS, strings and numbers are primitave types while arrays and objects are composite type. In Python, all data types are objects.


# DYNAMIC TYPING

# Python is highly flexible about assigning and reassigning variables to any type at any time:
awesomeness = None
awesomeness = 33.5
awesomeness = True

# By contrast, C/C++ are statically-typed languages, which means the variables are typed when they are declared:
int x = 5;
x = false; # COMPILE-TIME ERROR

# However, Python is NOT weakly or "loosely"-typed; it is a strongly-typed language. That means that while variables can be dynamically reassigned to different types, you cannot implicitly convert variables between types like this:
x = 3
y = " cats"
x + y # TypeError !!!!

# Explicitly convert the value in a Python:
x = 3
y = " cats"
str(x) + y # 3 cats

# In conclusion, Python is a DYNAMICALLY-TYPED AND STRONGLY-TYPED LANGUAGE.
