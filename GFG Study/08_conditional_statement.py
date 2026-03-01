age = 20
if age >= 18:
    print("Eligable to vote")

# If else Conditional Statement
age = 10
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")


# Short Hand if-else
marks = 45
result = "pass" if marks >= 40 else "fail"
print(f"You are {result}")


# elif Statement
age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")


# Nested if..else Conditional Statement
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


# Ternary Conditional Statement
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)


# Match-Case Statement
num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")


# Another examples
day = "mon"

match day:
    case "mon":
        print("Monday")
    case "tue":
        print("Tuesday")
    case "wed":
        print("Wednesday")
    case _:
        print("Invalid day")
