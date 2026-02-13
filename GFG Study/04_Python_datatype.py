a = 5               # int datatype
print(type(a))

b = 5.3             # float datatype
print(type(b))

c = 3 + 5j          # complex datatype
print(type(c))      # The complex datatype is 2 part
print(c.real)       # This is real part and
print(c.imag)       # This is imaginary part

d = 4 + 7j
e = 9 + 2j
print(d + e)        # (13+9j)
print(d - e)        # (-5+5j)
print(d * e)        # Output: (22+71j)

# Sequence Data Types
s = "My name is Aruna"
print(s)

print(type(s))

print(s[1])
print(s[3])
print(s[4])
print(s[-4])



# List Data Type
l = []          # Empty list

# list with int values
a = [5, 2, 8]
print(a)

# list with mixed values int and String
b = [4, "Aruna", "Basanta", 67, 37]
print(b)



# Access List Items
a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])


# Tuple Data Type
tup1 = ()       # initiate empty tuple

tup2 = ('Geeks', 'For', 7, 'Geeks')
print("\nTuple with the use of String: ", tup2)

# Accessing typle items
print(tup2[2])
print(tup2[1])
print(tup2[-2])


# Boolean datatype
print(type(True))
print(type(False))
# print(type(false))   # Error: name 'false' is not defined.



# Truthy and falsy values
if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")


# Set Data Type
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

# Accessing set items
set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Geeks" in set1)
