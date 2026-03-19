
x = int(input("Enter number:"))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

print("Using different method")

# @param x: int
# @return: string
def checkEvenOdd(x):
    if x % 2 == 0:
        return("Even")
    else:
        return("Odd")
print("The number", x, "is", checkEvenOdd(6))
