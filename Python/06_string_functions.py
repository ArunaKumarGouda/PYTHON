name = "Aruna"
print(len(name))  # output : 5
print(name.startswith("Aru")) # output : True
print(name.endswith("una")) # output : True
print(name.endswith("un")) # output : False
print(name.lower()) # output : aruna
print(name.upper()) # output : ARUNA

string = "abecdeacbfe"
count = string.count("e")
print(count) # output : 3

s = "Hello World"
index = s.find("World")
print(index) # output : 6

p = "Hello World"
replaced_string = p.replace("World", "Python")
print(replaced_string) # output : Hello Python
