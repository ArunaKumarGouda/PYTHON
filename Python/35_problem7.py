# Q) 1:-  Write a program using function to find greatest of three numbers
def greatestOfThreeNumber(a, b, c):
    if(a > b and a > c):
        return a
    if(b > a and b > c):
        return b
    if(c > a and c > b):
        return c
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
print("The greatest number is: ", greatestOfThreeNumber(a, b, c))


# Q) 2:- Write a python program using function to convert Celsius to Fahrenheit.
def f_to_c(f):
    return (f - 32) * 5 / 9

f = int(input("Enter temperature in F: "))
print(f"{f_to_c} degree C")


# Q) 3:- How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c", end = "")
print("d", end = "")


# Q) 4:- Write a recursive function to calculate the sum of first n natural numbers.
def sum(n):
    if(n == 1):
        return 1
    return sum(n - 1) + n
print(sum(4))


#) 5:- Write a python function to print first n lines of the following pattern:
# ***
# **      -for n = 3
# *    
def pattern(n):
    if(n == 0):
        return
    print("*" * n)
    pattern(n - 1)
pattern(6)


# Q) 6:- Write a python function which converts inches to cms.
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is: {inch_to_cms(n)}")


# Q) 7:- Write a python function to remove a given word from a list ad strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n
    
l = ["Aruna", "Rohan", "Subham", "an"]
print(rem(l, "an"))


# Q) 8:- Write a python function to print multiplication table of a given number.
def multiply(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

multiply(4)
