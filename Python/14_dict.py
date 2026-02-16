marks = {
    "Aruna": 100,
    "Basanta": 90,
    "Himansu": 80,
    0: "Aruna"
}
print(marks["Aruna"])  

print("The items is : ", marks.items())
print("The keys is : ", marks.keys())
print("The values is : ", marks.values())

marks.update({"Aruna": 99, "Malay": 43})
print(marks["Aruna"])
print(marks.items())

print(marks.get("Basanta"))

print(marks.get("Himansu1"))  # return none
print(marks["Himansu1"])      # return Error
