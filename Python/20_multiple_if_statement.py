age = int(input("Enter your age :"))

if(age % 2 == 0):
    print("you enter the age which is an even number")

else:
    print("You enter the age which is an odd number")

# if elif else ladder
if(age >= 18):
    print("You are eligable")

elif(age < 0):
    print("You are entering an invalid negative age")

elif(age == 0):
    print("You are entering 0 which is an invalid age")

else:
    print("You are not eligable")

print("End of program")

