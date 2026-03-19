a = int(input("Enter number 1 :"))
b = int(input("Enter number 2 :"))
c = int(input("Enter number 3 :"))

d = a ^ a
e = c ^ d
f = a & b
g = c | (a ^ a)
e = ~e

print(d, e, f, g)
