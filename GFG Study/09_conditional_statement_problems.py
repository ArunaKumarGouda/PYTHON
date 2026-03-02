# Problem 1: Check if user is eligible to vote
age = int(input("Enter your age: "))
if age >= 18: 
    print("You are eligable to vote")
else:
    print("You are not eligable to vote")


# Problem 2: Check if a number is positive
num = int(input("Enter number: "))

if num >= 0:
    print("Number is positive")
else:
    print("Number is negative")

# if-else Statement
# Problem 1: Check if a student is pass/fail in exam.
marks = int(input("Enter your marks: "))
result = "Pass" if marks >= 40 else "Fail"
print(result)


# Problem 2: Check if a user has balance to buy an item
balance = float(input("Enter your balance: "))
price = float(input("Enter your item price: "))

if balance >= price:
    print("You are able to buy an item")
else:
    print("You are not able to buy an item")


# if-elif-else Statement
# Problem 1: Suggest a mode of transport based on distance
distance = float(input("Enter the distance to your destination (in km): "))

if distance <= 2:
    print("You can walk.")
elif distance <= 10:
    print("Use a bicycle or scooter.")
elif distance <= 50:
    print("Take a car or public transport.")
else:
    print("Consider a train or flight.")


# Nested if-else Statement
# Problem 1: Login with username and password
username = input("Enter username: ")
password = input("Enter password: ")

if username == "Aruna":
    if password == "9510":
        print("Login successfully")
    else:
        print("Incorrect password")
        print("Please try again...")
else:
    print("username not found") 


# Problem 2: Check exam pass and scholarship eligibility
marks = int(input("Enter your marks: "))

if marks >= 40:
    if marks >= 70:
        print("You are passed with scholarship eligibility")
    else:
        print("You are passed with out scholarship eligibility")
else: 
    print("You are failed")



# Ternary Statement
# Problem 1: Check if number is even
number = int(input("Enter number: "))
print("Even" if number % 2 == 0 else "Odd")


# Problem 2: Compare two numbers
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("a is greater" if a > b else "b is greater")


# Problem 3: Temperature check
temp = int(input("Enter the temperature: "))

print("Hot" if temp > 25 else "Cool")


# Match- case Statement
# Problem 1: Assign grade
grade = input("Enter your grade (A/B/C): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("Average")
    case _:
        print("Fail")


# Problem 2: Activity Suggestion based on weather condition
weather = input("Enter the weather (sunny/rainy/cloudy/snowy): ").lower()

match weather:
    case "sunny":
        print("Great day for a picnic!")
    case "rainy":
        print("Stay indoors and read a book.")
    case "cloudy":
        print("Perfect time for a walk.")
    case "snowy":
        print("Build a snowman or go skiing!")
    case _:
        print("Unknown weather condition.")



# Problem 3: Mobile notification settings based on user profile mode
mode = input("Enter phone mode (silent/vibrate/loud/do not disturb): ").lower()

match mode:
    case "silent":
        print("Notifications are muted.")
    case "vibrate":
        print("Phone will vibrate for notifications.")
    case "loud":
        print("All notifications will play sound.")
    case "do not disturb":
        print("No calls or notifications will come through.")
    case _:
        print("Invalid mode selected.")
