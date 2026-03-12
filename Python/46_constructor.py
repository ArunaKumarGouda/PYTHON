class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

# aruna = Employee()
# aruna.name = "Aruna Kumar Gouda"
# aruna.greet()
# aruna.getInfo()
# print(aruna.name, aruna.language, aruna.salary)

# rohan = Employee()

abinash = Employee("Abinadh Pradhan", 300000, "JavaScript")
print(abinash.name, abinash.salary, abinash.language)
