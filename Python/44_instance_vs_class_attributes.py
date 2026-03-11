class Employee:
    language = "Python"     # This is a class attribute
    salary = 12700000

object = Employee()
object.language = "JavaScript"  # This is an instance attrubute
print(object.language, object.salary)

# Instance attribute take preference over class attribute during assignment & retrieval
