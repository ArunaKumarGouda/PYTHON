# Using walrus operator
if(n := len([1, 2, 3, 4, 5])) > 3:
    print(f"list is too long ({n} elements, expected <= 3)")

# output: list is too long (5 elements, expected <= 3)

# Another examples
# Without Walrus operator
n = len("Hello")
if n > 4:
    print(n)

# With walrus operator
if(n := len("Hello") > 3):
    print(n)
