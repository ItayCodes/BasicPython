# Welcome to BasicPython, a simple tutorial to help you figure out your way around the most popular coding language.
# A couple of things to know first:

# ==================================================================================================================== #


# The hash symbol (#) is used to write comments in Python.
# Anything after # on a line is ignored by the Python interpreter and is not executed as code.
# Comments are useful for explaining your code or temporarily disabling a line of code.

"""
You could also use this format to form...
a multi-line comment!
"""

# ==================================================================================================================== #

# The most well-known function in Python is 'print()', which is used to display output in the console.
# This is very helpful for development purposes, to test out and play with your code.
print("Hello, World!")

# ==================================================================================================================== #

# What is a variable?
# A variable is a container for storing data. It can hold different types of values.
# Here are a few examples:

name = "John"  # String
last_name = "Doe"  # String
age = 18  # Integer
height = 5.7  # Float
is_student = True  # Boolean

# You can also check the data type using a combination of 2 functions, 'print()' and 'type()'
print(type(name))  # <class 'str'>
print(type(last_name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

# There is also another data type called None, or a NoneType
# This is here to represent an empty value
empty_value = None
print(type(empty_value))  # <class 'NoneType'>

# But what do these mean?
# This means we can access our variables at any time. They are stored in memory and can be modified or printed!

# Examples using the 'print()' function:
print("Hello, my name is", name)  # Hello, my name is John

# What if I want to include more variables?
# You can use String Concatenation, like so:
print("Hello, my name is " + name + " " + last_name)

# But this seems tedious, doesn't it?
# Especially when working with numbers, if you try to concatenate a string with a number using '+', you'll get an error.
# ❌ This will cause an error because 'age' is an integer
# print("Hello, my name is " + name + " and I am " + age + " years old.")
# TypeError: can only concatenate str (not "int") to str


# The best method would be to use what's called an 'f-string', which allows you to insert variables directly inside a string.
print(f"Hello, my name is {name}, and I am {age} years old.")  # ✅ Best method

# Alternative fix (but f-strings are better)
print("Hello, my name is " + name + " and I am " + str(age) + " years old.")  # ✅ Works, but less readable

# ==================================================================================================================== #

# Another cool function is the 'input()' function, which allows the user to input their own value
name = input("Enter your name: ")
print(f"Hello, {name}")

# Let's say we'd like to do a calculation with our input, for that we'll need to change the data type of the user input.
# Since the input() function always returns a string, we won't be able to perform mathematical operations on it.
age = int(input("Enter your age: "))  # Turning the string into an integer
print(f"In 5 years, you will be {age + 5} years old.")  # Performing a calculation inside our string!

# Since we're dealing with numbers, let's explore arithmetic operations in Python.
x = 10
y = 3

print(x + y)  # ➕ Addition
print(x - y)  # ➖ Subtraction
print(x * y)  # ✖ Multiplication
print(x / y)  # ➗ Division (returns float)
print(x // y)  # 🔢 Floor division (integer result)
print(x % y)  # 🔄 Modulus (remainder)
print(x ** y)  # 🔺 Exponentiation (power)

# ==================================================================================================================== #

# When coding, logic is a very important factor, it lets our code make decisions based on different factors.
# This is why we have Conditional Statements!
# These statements check a condition, which always evaluates to either 'True' or 'False'.
# The result is known as a Boolean (bool) data type.

# Checking if a user is old enough to vote
age = int(input("Enter your age: "))  # Taking user input and converting it to an integer

if age >= 18:  # Condition: Is the age 18 or older?
    print("You are eligible to vote!")  # ✅ If True, this block runs and the operation is complete.
elif age > 0:  # Else-if: Age is greater than 0 but less than 18
    print("You are too young to vote.")  # ✅ If the first condition is False and this is True, this block runs.
else:  # Else: If no previous condition was True, execute this
    print("Invalid age entered.")  # ✅ If all previous conditions are False, this block runs.

# ==================================================================================================================== #

# 🚀 Future Enhancements:
# ✅ Loops (for, while, conditions, and breaks)
# ✅ Data Structures (lists, sets, tuples, and dictionaries)
# ✅ Functions and Error Handling
# ✅ File Handling (open, read, write, 'with open', different modes)
# ✅ Modules and Importing
# ✅ Object-Oriented Programming (OOP)
# ✅ Working with APIs

# ==================================================================================================================== #
