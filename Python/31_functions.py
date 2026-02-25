# Function Defination
def avg():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))

    average = (a + b + c) / 2
    print("The average of ", a, b, "and", c, "is ", average)

avg()      # Function Call
print("Thank You!")
avg()
print("Thank You!")


# Simple Example of function
# Q) Write a program to greet a user with "Good day" using function
def goodDay():
    name = input("Enter your name: ")
    print("Hello!", name, "have a good day.")

goodDay()


'''
Function is two type 
1. Built in function(Already present in python)
2. User defined function(Defined by the user)
'''
