# For Loop
n = 4
for i in range(0, n):
    print(i)


#  Iterating Over List, Tuple, String and Dictionary Using for Loops in Python
li = ["geeks", "for", "geeks"]
for x in li:
    print(x)
    
tup = ("geeks", "for", "geeks")
for x in tup:
    print(x)
    
s = "abc"
for x in s:
    print(x)
    
d = dict({'x':123, 'y':354})
for x in d:
    print("%s  %d" % (x, d[x]))
    
set1 = {10, 30, 20}
for x in set1:
    print(x)


# Iterating by Index of Sequences
li = ["geeks", "for", "geeks"]
for index in range(len(li)):
    print(li[index])


# While Loop
cnt = 0
while (cnt < 3):
    cnt = cnt + 1
    print("Hello Geek")

'''
# Infinite While Loop
# while (True):
#     print("Hello Geek")

Note: It is suggested not to use this type of loop as it is a never-ending infinite loop where the condition is always true and we have to forcefully terminate the compiler.
'''

# Nested Loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()


# Loop Control Statements
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print('Current Letter :', letter)


# Break Statement
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)


# Pass Statement
for letter in 'geeksforgeeks':
    pass
print('Last Letter :', letter)
