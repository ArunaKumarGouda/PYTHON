# Q)1:- Write a python program to find the greatest of four numbers entered by the user
a1 = int(input("Enter number 1:"))
a2 = int(input("Enter number 2:"))
a3 = int(input("Enter number 3:"))
a4 = int(input("Enter number 4:"))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("the number 1 is greatest and the number is :", a1)

elif(a2 > a1 and a2 > a3 and a2 > a4):
    print("the number 2 is greatest and the number is :", a2)

elif(a3 > a1 and a3 > a2 and a3 > a4):
    print("the number 3 is greatest and the number is :", a3)

elif(a4 > a1 and a4 > a2 and a4 > a3):
    print("the number 4 is greatest and the number is :", a4)


# Q)2:- Write a program to findout whether a student has passed or failed if it requires a total of 40% and atlist 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
mark1 = int(input("Enter mark 1 :"))
mark2 = int(input("Enter mark 2 :"))
mark3 = int(input("Enter mark 3 :"))

total_percentage = (100 * (mark1 + mark2 + mark3)) / 300
print("Total percentage of marks is :", total_percentage)

if(total_percentage >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33):
    print("You are passed")
else:
    print("You are failed, try again next year.")


# Q)3:- A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams.
p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Enter message :")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is a spam")
else:
    print("This comment is not a spam")


#Q)4:- Write a program to find whether a givem username contains less then 10 characters or not.
username = input("Enter username")

if(len(username) > 10):
    print("This username is valid")
else:
    print("This username is not valid")


# Q)5:- Write a program which finds out whether a name is present in a list or not.
l = ["Aruna", "Ritwick", "Niranjan", "Abinash"]

name = input("Enter name :")

if(name in l):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")


# Q)6:- Write a program to calculate the grade of a student from his marks :
marks = int(input("Enter your marks :"))

if(marks < 100 and marks > 90):
    grade = "O"
elif(marks < 90 and marks >= 80):
    grade = "E"
elif(marks < 80 and marks >= 70):
    grade = "A"
elif(marks < 70 and marks >= 60):
    grade = "B"
elif(marks < 60 and marks >= 50):
    grade = "C"
elif(marks < 50 and marks >= 40):
    grade = "D"
elif(marks < 40):
    grade = "F"

print("Your Grade is :", grade)


# Write a program to find out whether a given post is talk about "Aruna" or not
post = input("Enter post :")

if("Aruna".lower() in post.lower()):
    print("This post is talking about aruna")
else:
    print("This post is not talking about aruna")
