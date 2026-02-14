a = (1, 2, 3, False, "Aruna")        # We can not change tuples value
print(a)
print(type(a))                       # 'a' is a tuple

no = a.count(3)
print(no)                            # Count the value

num = a.index(3)
print(num)                           # Return index number of a tuple

repeated = a * 3
print(repeated)                      # Repeat the tuple 3 times

print(3 in a)                        # To check the given number id present or not in a tuple  Output : True
print(4 in a)                        # Output : False

print(len(a))                        # To print length of a tuple

