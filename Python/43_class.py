class Employee:
    name = "Aruna"     # This is a class attribute
    language = "python"
    salary = 1200000

object = Employee()
print(object.name)
print(object.language)
print(object.salary)


aruna = Employee()
aruna.name = "Aruna Kumar Gouda"    # This is an object attribute or instance attribute 
print(aruna.name, aruna.salary, aruna.language)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class 
