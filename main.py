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

# 🔄 Augmented Assignment Operators (`+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`)
# These operators allow modifying a variable without writing redundant expressions.

x = 10
x += 5  # Equivalent to: x = x + 5
print(x)  # Output: 15

y = 20
y -= 3  # Equivalent to: y = y - 3
print(y)  # Output: 17

z = 4
z *= 2  # Equivalent to: z = z * 2
print(z)  # Output: 8

a = 10
a /= 2  # Equivalent to: a = a / 2
print(a)  # Output: 5.0 (always float)

b = 10
b //= 3  # Equivalent to: b = b // 3
print(b)  # Output: 3 (integer division)

c = 10
c %= 3  # Equivalent to: c = c % 3
print(c)  # Output: 1 (remainder after division)

d = 2
d **= 3  # Equivalent to: d = d ** 3
print(d)  # Output: 8 (exponentiation)

# These are commonly used in loops and calculations to simplify code and improve efficiency.

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

# There are a few more data types in Python that are really helpful in certain scenarios, here are examples of them:
# 📜 LIST: Ordered, mutable (can be changed), allows duplicates
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Adding a new item
fruits.remove("banana")  # Removing an item
print(fruits)  # ['apple', 'cherry', 'orange']
print(fruits[0])  # Lists use **zero-based indexing** (first element is at index 0), "apple"

# 🔗 TUPLE: Ordered, immutable (cannot be modified after creation), allows duplicates
colors = ("red", "green", "blue")
# colors.append("yellow")  # ❌ This will cause an error (tuples cannot be modified)
print(colors[1])  # Accessing element: green

# 🔥 SET: Unordered (elements have no fixed position), mutable, and no duplicate values
# ❌ Sets do NOT support indexing (e.g., unique_numbers[0] will raise an error)
unique_numbers = {1, 2, 3, 3, 4, 5}  # Duplicates are automatically removed
print(unique_numbers)  # {1, 2, 4, 5, 6} (order may vary)

# 📖 DICTIONARY: Key-value pairs, mutable, maintains insertion order (Python 3.6+)
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
person["job"] = "Developer"  # Adding a new key-value pair
print(person["name"])  # Accessing a value: Alice
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Developer'}

# ==================================================================================================================== #

# Now let's introduce you to loops, which are very helpful when working with data structures like lists or ranges.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Will print each fruit in the list, one by one

# Using enumerate() to get both index and value while looping
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")  # Prints index along with the fruit name
    # 0: apple
    # 1: banana
    # 2: cherry

for i in range(5):
    print(i)  # Will print 0-4, one by one

# Dictionaries can be looped through in multiple ways:
person = {"name": "Alice", "age": 25, "city": "New York"}

# Only loop through the keys
for key in person.keys():  # .keys() is optional but improves readability
    print(key)  # Prints: name, age, city

# Only loop through the values
for value in person.values():
    print(value)  # Prints values: Alice, 25, New York

# Looping through both key, value pairs:
for key, value in person.items():
    print(f"{key}: {value}")

# Now that we understand for loops, let's learn about while loops.

count = 5
while count > 0:  # Condition
    print(f"Countdown: {count}")  # Execute if condition is met
    count -= 1  # Decrementing count when condition is met
print("Blast off! 🚀")  # Executes once the while loop stops
# Countdown: 5
# Countdown: 4
# Countdown: 3
# Countdown: 2
# Countdown: 1
# Blast off! 🚀

# You can also use a special keyword called break to stop the loop
x = 1
while x <= 5:
    if x == 3:
        print("Stopping at 3")
        break  # Exits the loop immediately; remaining iterations won't run
    print(x)
    x += 1
# 1
# 2
# Stopping at 3

# The continue keyword skips the rest of the current iteration and moves to the next one,
# meaning any code after it in the loop won't execute for that cycle.
x = 0
while x < 5:
    x += 1
    if x == 3:
        print("Skipping 3")
        continue  # Skips printing 3
    print(x)

# ==================================================================================================================== #

# 🚀 Future Enhancements:
# ✅ Functions and Error Handling
# ✅ File Handling (open, read, write, 'with open', different modes)
# ✅ Modules and Importing
# ✅ Object-Oriented Programming (OOP)
# ✅ Working with APIs

# ==================================================================================================================== #
