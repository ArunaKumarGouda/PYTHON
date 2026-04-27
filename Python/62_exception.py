# Exception handling is used to handle errors(exceptions) in a program so that it doesn't crash and run smoothly.
try:
    print("Hello")
except:
    print("Error")
finally:
    print("Always runs")



try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print("Hey!")
    print(v)
except Exception as e:
    print(e)

print("Thank you")
