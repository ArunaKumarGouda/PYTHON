# Inheritance is a way of creating a new class from an existing class.

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.showLanguage} language")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.showLanguage} language")


a = Employee()
b = Programmer()

print(a.company, b.company)
