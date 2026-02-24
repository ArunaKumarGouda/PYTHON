# Break statement
for i in range(100):
    if(i == 31):
        break        # Exit the loop right now
    print(i)

# Continue statement
for i in range(50):
    if(i == 10 or i == 11 or i == 12):
        continue     # Skip the iteration
    print(i)


# For simple practice
print("Printing...")

for i in range(40):
    if(i == 10 or i == 11 or i == 13 or i == 15):
        continue

    if(i == 30):
        break

    print(i)
