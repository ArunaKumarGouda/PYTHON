# Q) 1:- Create a class "Programmer" for storing information of few programmers working at Microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Aruna", 32556, 761109)
print(p.name, p.salary, p.pin, p.company)

r = Programmer("Rohan", 300000, 458109)
print(r.name, r.salary, r.pin, r.company)
print()



# Q) 2:- Write a class "calculator" capable of finding square root of a number.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"The square of {self.n} is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
print()



# Q) 3:- Create a class with a class attribute a; create an object form it and set 'a' directly using object.a = o. Does this change the class attribute?
class Demo:
    a = 4

o = Demo()
print(o.a)  # print the class attribute because instance attribute is not present
o.a = 0     # instance attribute is set
print(o.a)  # print the instance attribute because instance attribute is present
print(Demo.a)   # Prints the class attribute
print()



# Q) 4:- Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")

    def cube(self):
        print(f"The square of {self.n} is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n**1/2}")

    @staticmethod
    def greet():
        print("hello")
a = Calculator(4)
a.square()
a.cube()
a.squareroot()
a.greet()
print()



# Q) 5:- Write a class Train which has methods to book a ticket, get status(no of seats) and get fare information train running under India Railways.
from random import randint

class Train:

    # def book(self, trainNo, fro, to):
    #     print(f"Ticked is booked in train no: {trainNo} from {fro} to {to}")

    # def getStatus(self, trainNo):
    #     print(f"Train number: {trainNo} if running on time")

    # def getFare(self, trainNo, fro, to):
    #     print(f"Ticked is booked in train no: {trainNo} from {fro} to {to} is {randint(222, 555)}")

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticked is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train number: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(37489)
t.book("bhubaneswer", "Berhampur")
t.getStatus()
t.getFare("bhubaneswer", "Berhampur")
print()



# Q) 6:- Can you change the self-parameter inside a class to something else (say "aruna"). Try changing self to "slf" or "aruna" and see the effects.
class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(aruna, fro, to):
        print(f"Ticked is booked in train no: {aruna.trainNo} from {fro} to {to}")

    def getStatus(aruna):
        print(f"Train number: {aruna.trainNo} is running on time")

    def getFare(aruna, fro, to):
        print(f"Ticket is booked in train no: {aruna.trainNo} from {fro} to {to} is {randint(222, 555)}")

t = Train(37489)
t.book("bhubaneswer", "Berhampur")
t.getStatus()
t.getFare("bhubaneswer", "Berhampur")
