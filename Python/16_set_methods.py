# There is no way to change items in sets  
# Sets cannot contains duplicate values
# In sets Element's order does not matter
# Cannot access elements by index

s = {4, 56, 23, 4, 4, 621, 4, "Aruna"}
s.add(57)
print(s, type(s))
print("The length of a set is : ", len(s))  # Here the length of s is 6 because set doesnot allow duplicate values and the values are {4, 56, 23, 621, "Aruna", 57}
