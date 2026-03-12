class Employee:
    language = "Python"    
    salary = 12700000

    def getInfo(self):
        print(f"Ths language is {self.language}, and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

    # def greet(self):
    #     print("Good morning")

object = Employee()
object.language = "JavaScript"  
object.greet()
object.getInfo()
# Employee.getInfo(object) 
