def doubleTup(numbers):
    result = []
    for num in numbers:
        result.append(num * 2)
    return tuple(numbers)

# taking input from user
numbers = tuple(map(int, input("Enter numbers seperated by space: ").split()))

# calling the function 
output = doubleTup(numbers)

# printing result
print("Doubled tuple:", output)
