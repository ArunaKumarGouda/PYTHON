num = [3, 4, 6, 5, 82]

while(n := len(num)) > 0:
    print(num.pop())


# Comparing with and without Walrus Operator
d = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True}
]

print("With Python 3.8 Walrus Operator:")
for entry in d:
    if name := entry.get("name"):
        print(name)

print("Without Walrus operator:")
for entry in d:
    name = entry.get("name")
    if name:
        print(name)


# Simplifying User Input Loops
foods = []
while True:
    f = input("What food do you like?: ")
    if f == "quit":
        break
    foods.append(f)


# With Walrus Operator
foods = []
while (f := input("What food do you like? (type 'quit' to stop): ")) != "quit":
    foods.append(f)
