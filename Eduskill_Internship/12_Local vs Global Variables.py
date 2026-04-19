# Local Scope
def my_function():
    x = 10
    print(x)

my_function()

# Global Scope

x = 30
def show():
    print(x)

show()
print(x)


# Modifying Global Variables
# Use global keyword:
count = 0
def increment():
    global count
    count += 1
    
increment()
print(count)
