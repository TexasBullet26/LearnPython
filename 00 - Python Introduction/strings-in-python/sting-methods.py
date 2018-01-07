# STRINGS

# Objectives:
#  - Understand Unicode vs ASCII encodings
#  - Learn about the different string methods
#  - Learn about formatted strings

# Iterable series of characters, looping through a string
for x in "word":
    print(x)
# w
# o
# r
# d

# String Literal
x = "my favorite " \
    "string"

# Immutable
my_str = "can't touch this"
my_str[6] = " " #TypeError

# When you build strings with `+=` in a loop, you're creating a new string every iteration:
new_str = "hello "
for c in "world":
    new_str += c # new string created every single time!
print(new_str) # hello world

# In Python3, strings are Unicode by default.


# STRING METHODS

# Let's start with a simple variable:
string = "this Is nIce"

# Upper: To convert every character to upper-case we can use the `upper` function:
string.upper() # 'THIS IS NICE'

# Lower: To convert every character to lower-case we can use the `lower` function:
string.lower() # 'this is nice'

# Capitalize: To convert the first character in a string to upper-case and everything else to lower-case we can use the `capitalize` function:
string.capitalize() # 'This is nice'

# Title: To convert every first character in a string to upper-case and everything else to lower-case we can use the `title` function:
string.title() # 'This Is Nice'

# find method: To find a subset of characters in a string we can use the `find` method. This will return the index at which the first match occurs. If the character/characters is/are not found, `find` will return `-1`:
instructor = 'elie'
instructor.find('e') # 0
instructor.find('E') # -1 it IS case sensitive!
string.find("i") # 2, since the character "i" is at index 2
string.find('Tim') # -1

# isalpha function: To see if all characters are alphabetic we can use the `isalpha` function:
string.isalpha() # False
string[0].isalpha() # True

# isspace function: To see if a character or all characters are empty spaces, we can use the `isspace` function:
string.isspace() # False
string[0].isspace() # False
string[4].isspace() # True

# islower function: To see if a character or all characters are lower-cased, we can use the `islower` function (there is also a function, which does the inverse called `isupper`):
string.islower() # False
string[0].islower() # True
string[5].islower() # false
string.lower().islower() # True

# istitle function: To see if a string is a "title" (first character of each word is capitalized), we can use the `istitle` function:
string.istitle() # False
string.title().istitle() # True
"not Awesome Sauce".istitle() # False
"Awesome Sauce".istitle() # True

# endswith function: To see if a string ends with a certain set of characters we can use the `endswith` function:
"string".endswith('g') # True
"awesome".endswith('foo') # False

# partition function: To partition a string based on a certain character, we can use the `partition` function:
string.partition('i') # what's the type of what you get back?
"awesome".partition('e') # ('aw', 'e', 'some')

# STRING INTERPOLATION WITH FORMATTED STRINGS

# One of the most common string methods you'll use is the `format` method. This is a powerful method that can do all kinds of string manipulation, but it's most commonly just used to pass variables into strings. In general this is preferred over string concatenation, which can quickly get cumbersome if you're mixing a lot of variables with strings. For example:
first_name = "Trey"
last_name = "Lanzer"
city = "Dallas"
mood = "great"

# Without `format`:
greeting = "Hi, my name is " + first_name + " " + last_name + ", I live in " + city + " and I feel " + mood + "."

# With `format`: When we call `format` on a string, we can pass variables into the string! The variables will be passed in order, wherever `format` finds a set of curly braces:
greeting = "Hi, my name is {} {}, I live in {} and I feel {}.".format(first_name, last_name, city, mood)

# Starting in Python 3.6, however, we have f-strings, which are a cleaner way of doing string interpolation. Simply put f in front of the string, and then brackets with actual variable names:
greeting = f"Hi, my name is {first_name} {last_name}, I live in {city}, and I feel {mood}."
