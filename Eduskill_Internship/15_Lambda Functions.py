# lambda argumant: ecpression
add = lambda a, b: a + b
print(add(3,5))

# Square Example
square = lambda x: x * x
print(square)


# Using Lambda with Built-in Functions
# With map()
numbers = [1, 2, 3]
squared = list(map(lambda x: x*x, numbers))
print(squared)

# With filter()
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# With sorted()
students = [('Alice', 85), ('Bob', 92)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
