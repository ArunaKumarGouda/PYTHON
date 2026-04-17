fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)


coordinates = (10.0, 20.0, 30.0)

for coord in coordinates:
    print(coord)


# Using enumerate() (with index)
colors = ['red', 'green', 'blue']

for index, color in enumerate(colors):
    print(f"Index: {index}, Color: {color}")

# Using range()
my_list = ['a', 'b', 'c']

for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")


# Exercise 1: Create List
student_grades = []
student_grades.append(85)
student_grades.append(92)
student_grades.append(78)
student_grades.append(95)

print(student_grades)


# Exercise 2: List Slicing
top_two = student_grades[1:3]
print(top_two)


# Exercise 3: Tuple Iteration
rgb_color = (255, 165, 0)

for value in rgb_color:
    print(value)


# Exercise 4: List vs Tuple
# List
mutable_data = [10, 20]
mutable_data.append(30)
print(mutable_data)

# Tuple
immutable_data = (10, 20)

try:
    immutable_data.append(30)
except AttributeError:
    print("Cannot modify tuple")

try:
    immutable_data[0] = 5
except TypeError:
    print("Tuples are immutable")
