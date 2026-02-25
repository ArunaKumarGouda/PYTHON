# Q)1:- Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter a number :"))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")


# Q)2:- Write a program to greet all the person names stored in a list 'l' and which starts with S.
# l = ["Aruna", "Shasank", "Rahul", "Bikram"]
l = ["Shasank", "Aruna", "Rahul", "Bikram"]

for names in l:
    if(names.lower().startswith("a")):
        print(f"Hello {names}")
else:
    print("Done")


# Q)3:- Attempt problem 1 using while loop
n = int(input("Enter a number :"))
i = 1

while(i <= 10):
    print(f"{n} X {i} = {n * i}")
    i += 1


# Q)4:- Write a program to fing whether a given number is prime or not
n = int(input("Enter a number :"))

for i in range(2, n):
    if(n % i == 0):
        print("Number is not prime")
        break
else:
    print("Number is prime")


# Q)5:- Write a program to fing the sum of first n natural numbers using while loop
n = int(input("Enter a natural number :"))

i = 1
sum = 0
while(i <= n):
    sum += i
    i += 1

print(sum)


# Q)6:- Write a program to calculate the factorial of a given number using for loop
n = int(input("Enter a number :"))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"The factorial of {n} is {factorial}")


# Q)7:- Star pattern 1
n = int(input("Enter number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end = "")
    print("*" * (2 * i - 1), end = "")
    print()


# Q)8:- Star pattern 2
n = int(input("Enter number: "))

for i in range(1, n + 1):
    print("*" * i, end = "")
    print()


# Q)9:- Star pattern 3
n = int(input("Enter number: "))

for i in range(1, n + 1):
    if(i == 1 or i == n):
        print("*" * n, end = "")

    else:
        print("*", end = "")
        print(" " * (n - 2), end = "")
        print("*", end = "")

    print()


# Q)10:- Wtite a program to print multiplication table of n using 
n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} X {11 - i} = {n * (11 - i)}")
    
