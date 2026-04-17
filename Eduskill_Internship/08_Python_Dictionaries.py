# Create Dictionary
my_dict = {}
my_dict = dict()

student = {
    "name": "Rahul", 
    "age": 22
}
# Access Values
print(student["name"])
print(student)

# using .get()
print(student.get("age"))
print(student.get("city", "Not Found"))

# Add / Modify Data
student["city"] = "Delhi"   # Add
student["age"] = 23         # Update
print(student)

# Iteration in Dictionary
for key in student:
    print(key)

# values
for value in student.values():
    print(value)

# key + value
for key, value in student.items():
    print(key, value)
    
# Remove Data
del student["age"]
student.pop("city")
student.popitem()  # removes last item
student.clear()    # empty dictionary

# Dictionary Methods
# .keys()
print(student.keys())
# .values()
print(student.values())
# .items()
print(student.items())      # (key, value)
