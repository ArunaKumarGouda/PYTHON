# Functions are like building blocks in programming
def greet():
    print("Hello World!")

# Function Parameters 
def hello(name):
    print(f"Hello, {name}")

hello("Aruna")

# Multi parameters
def add_numbers(a, b):
    print(a + b)

add_numbers(3, 6)

# return values
def mul_numbers(a, b):
    return a * b

result = mul_numbers(3, 5)
print(result)

# Practice Task
# Write a function to add two numbers:
def add_two_numbers(a, b):
    return a + b

c = add_two_numbers(3, 6)
print(c)
