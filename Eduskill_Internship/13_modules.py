# Import full module
import math

print(math.sqrt(4))
print(math.pi)
print(math.ceil(4.2))
print(math.floor(4.8))


# Import specific functions
from random import randint, choice

try:
    print(randint(1, 10))
    print(randint([1, 2, 3]))
except TypeError:
    print("Write correct code")

# Import with alias
import math as m;
print(m.pow(2, 3))


# Creating Custom Modules
# Step 1: Create a file (my_math_utils.py)
def square(n):
    return n * n

def cube(n):
    return n * n * n

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Step 2: Use the module
try:
    import my_math_utils

    print(my_math_utils.square(5))
    print(my_math_utils.cube(5))   
    print(my_math_utils.factorial(5))

except ModuleNotFoundError:
    print("Install Modules")

# Import specific functions
try:
    from my_math_utils import square, factorial
    print(square(7))
    print(factorial(7))
except ModuleNotFoundError:
    print("Install modules")


# Hands-on: Create Your Own Module
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
# Use it
import string_helpers

print(string_helpers.reverse_string("hello"))
print(string_helpers.count_vowels("hello"))
