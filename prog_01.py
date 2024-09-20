# Practice Python 101

# Prints two lines, and input field asking your name...
print("Hello, World!")
name = input("What's your name? ")
print("Hello {}!\nWelcome to Dataquest!".format(name))

# Python skit about spam. Setting and printing Strings and calculating...

spam_amount = 0     # Variable assignment
print(spam_amount)

spam_amount = spam_amount + 4       # Reaasigning the value of the existing variable

if spam_amount > 0:     # Conditionals: if  spam_amount is positive we print the string...
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount     # Assigning the variable with the result of multiplying a string with the amount of another variable... in this case 4
print(viking_song)


type(spam_amount)       # tells you the type of the thing your dealing with
type(19.95)             # type is another build-in function in python

print(5 / 2)        # calculates the "true division"
print(6 / 2)        # always gives you a float

print(5 // 2)       # the // operator always rounds the result down to the next integer
print(6 // 2)

# Order of operations = PEMDAS 
    # Parentheses, Exponents, Multiplication/Division, Addition/Subtraction

print(8 - 3 + 2) 
    # Output: 7

print(-3 + 4 * 2)
    # Output: 5

# sometimes the defult order of operations isn't what we want:

hat_height_cm = 25
my_height_cm = 190
# How tall am I, in meters, when wearing my hat?
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters, "?") 
    # Output:  Height in meters = 26.9 ?

# Now we can use parentheses to force Python to evaluate sub-expressions in whatever order:

total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)
    # Output: Height in meters = 2.15


# Built-in functions ffor working with numbers (min & max)
print(min(1, 2, 3))
print(max(1, 2, 3))

# abs returns the absolute value of an argument:
print(abs(32))
print(abs(-23))

# int and float can also be called as functions which convert their arguments to the corresponding type:
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)

# First exercise set

print("You've successfully run some Python code")
print("Congratulations!")

# how to import:
#from learntools.core import binder; binder.bind(globals())
#from learntools.python.ex1 import *
#print("Setup complete! You're ready to start question 0.")

# Build in functions:
def least_difference(a, b, c):
    diff1 = abs(a - b) # 15, 3, 5
    diff2 = abs(b - c) # 8, 1, 2
    diff3 = abs(a - c) # 7, 2, 3
    return min(diff1, diff2, diff3);

print(
    least_difference(2, 17, 9),
    least_difference(6, 9, 8),
    least_difference(7, 2, 4),
    ) # output: 7 1 2

# higher order functions:
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
   # """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
   # """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)

# By default, max returns the largest of its arguments. But if we pass in a function using the optional key argument, 
# it returns the argument x that maximizes key(x) (aka the 'argmax').
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)



