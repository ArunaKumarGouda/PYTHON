# Defining a Function
def function():
    print("Welcome")

# Calling a Function
function()


# Check whether a number passed as an argument or not
def checkEvenOdd(x):
    if(x % 2 == 0):
        print("Number is even")
    else:
        print("number is odd")

checkEvenOdd(16)
checkEvenOdd(7)


# Types of Function Arguments
# Default arguments

def myFun(x, y = 30):
    print("x = ", x)
    print("y = ", y)
myFun(10)


# Keyword arguments
def student(fname, lname):
    print(fname, lname)

student("Aruna", "Gouda")


# Positional argument
def nameAge(name, age):
    print("Hii, my name is ", name)
    print("my age is ", age)
nameAge("Aruna", 20)
print()
nameAge(21, "Basanta")


# Arbitrary Arguments
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun("Hey", "Welcome", first = "Geeks", mid = "for", last = "Geeks")


# Function within Functions
def f1():
    s = "I love coding"
    def f2():
        print(s)
    
    f2()
f1()


# Anonymous Functions
def cube(x): 
    return x*x*x
cube_1 = lambda x : x*x*x

print(cube(7))
print(cube_1(7))


# Return Statement in Function
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(square_value(2))
print(square_value(-4))


# Pass by reference and pass by value
# Function modifies the first element of list
def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   # list is modified

# Function tries to modify an integer
def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)     # integer is not modified


# Recursive Functions
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))
