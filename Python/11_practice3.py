# Q:1 :- Write a program to store five fruits in a list entered by the user.
fruits = []

f1   = input("Enter fruit 1 : ")
fruits.append(f1)
f2 = input("Enter fruit 2 : ")
fruits.append(f2)
f3 = input("Enter fruit 3 : ")
fruits.append(f3)
f4 = input("Enter fruit 4 : ")
fruits.append(f4)
f5 = input("Enter fruit 5 : ")
fruits.append(f5)

print(fruits)

# Q:2 :- Write a program to accept marks om 6 students and display them in a sorted manner
marks = []

m1 = int(input("Enter marks 1 : "))
marks.append(m1)
m2 = int(input("Enter marks 2 : "))
marks.append(m2)
m3 = int(input("Enter marks 3 : "))
marks.append(m3)
m4 = int(input("Enter marks 4 : "))
marks.append(m4)
m5 = int(input("Enter marks 5 : "))
marks.append(m5)
m6 = int(input("Enter marks 5 : "))
marks.append(m6)

marks.sort()

print(marks)

# Q:3 :- Check that tuple type can not be change in python

a = (4, "Aruna", 423)
a[2] = "Ram"  # output : Error : 'tuple' object does not support item assignment

# Q:4 :- write a program to sum a list with 4 numbers.
l = (2, 8, 4, 5)
print(sum(l))

# Q:5 :- write a program to count the number of zeros in the following tuples.
tpl = (1, 0, 0, 5, 0, 4, 2)
b = tpl.count(0)
print(b)
