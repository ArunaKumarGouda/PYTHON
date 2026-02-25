number = 7
if number:
    print("True")

number = 0
if number:
    print("False")


if [1, 2]:
    print("non-empty list is truthy")

if -4:
    print("-4 is truthy")


if not 0:
    print("0 is falsy")

if not []:
    print("Empty list is falsy")


num1 = 7
num2 = 4

if num1 % 2:
    print(num1, "is odd")
else:
    print(num1, "is even")

if num2 % 2:
    print(num2, "is odd")
else:
    print(num2, "is even")


# Built-in bool() function
print(bool(7))      
print(bool(0))      
print(bool([1,2,3]))
print(bool([]))      
print(bool(None))
