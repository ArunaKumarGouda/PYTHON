# Arithmethic Operators
# Variables
print("Arithmetic Operators")
a = 15
b = 4

# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)
print()




#Comparison Operators
print("Comparison Operators")
a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print()


#Logical Operators
print("Logical Operators")

a = True
b = False
print(a and b)
print(a or b)
print(not a)
print()


#Bitwise Operators
print("Bitwise Operators")

a = 10
b = 4

print(a & b)    # 1 only if both bits are 1
print(a | b)    # 1 if at least one bit is 1
print(~a)       # invert all bits (1→0, 0→1)     ~a = -(a + 1):  ~10 = -(10 + 1) = -11
print(a ^ b)    # 1 if bits are different
print(a >> 2)   # shift bits right, divide by 2^n
print(a << 2)   # shift bits left, multiply by 2^n
print()         # new line



#Assignment Operators
print("Assignment Operators")

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)
print()


#Identity Operators
print("Identity Operators")

a = 10
b = 20
c = a

print(a is not b)
print(a is c)
print()



#Membership Operators
print("Membership Operators")

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")
print()



#Ternary Operators
print("Ternary Operators")

a, b = 10, 20
min = a if a < b else b     # short_if = value1 if condition else value2

print(min)

marks = 75
result = "Pass" if marks >= 40 else "Fail"
print(result)
print()



#Precedence and Associativity of Operators
print("Precedence and Associativity of Operators")

#Operator Precedence
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

#Operator Associativity
print(100 / 10 * 10)
print(5 - 2 + 3)
print(5 - (2 + 3))
print(2 ** 3 ** 2)
