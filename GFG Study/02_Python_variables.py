# Python variables
a = 4               # Here a is a and b are called variables
b = "Aruna"
print(a)
print(b)

# Multiple Assignments in python variables
a = b = c = 100
print(a, b, c)


a, b, c = 2, 54.6, "Akg"
print(a)
print(b, c)


# Type Casting a Variable
s = "10"  
n = int(s)

cnt = 5
f = float(cnt) 

age = 25
s2 = str(age)  

print(n)  
print(f)  
print(s2)

# Type of variables
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))


# Deleting a Variable 
x = 30
# del x          NameError: name 'x' is not defined
print(x)


# Swapping Two Variables
a, b = 5, 10
a, b = b, a
print(a, b)

# Counting Characters in a String
word = "Python"
print("The word is : ", word)
length = len(word)
print("Length of the word : ", length)
