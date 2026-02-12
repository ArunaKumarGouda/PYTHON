name = input("Enter your name : ")
print("Hello!", name, "Welcome.")


s = "Aruna"
age = 20
city = "Badagada"
print(s, age, city)

# Take multiple inputs in python
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
 
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)


# Print Numbers in Python
n = int(input("Enter number : "))
print(n)

# Print Float or Decimal Number in Python
price = float(input("Enter price of rose : "))
print("The price of rose is : ", price)

# Find DataType of Input in Python
a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
