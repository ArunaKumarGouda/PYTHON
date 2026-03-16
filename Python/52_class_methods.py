# A class method is a method which is bound to the 

class Employee:
    a = 1

    @classmethod
    def show(self):
        print(f"The class attribute of a is {self.a}")

    @property  
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45
e.name = "Aruna Gouda"
print(e.fname, e.lname)
e.show()
