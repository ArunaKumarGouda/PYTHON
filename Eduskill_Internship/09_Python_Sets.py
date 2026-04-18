# Creating set
my_set = {1, 2, 3}
my_set = set()

# Remove duplicates 
numbers = {1, 2, 2, 4, 3, 5, 5, 6}
duplicates = set(numbers)
print(duplicates)

# Adding elements
my_set.add(4)
my_set.update([5, 6]) # {4, 5, 6}
print(my_set)

# Removing elements
my_set.remove(3)   # error if not exist
my_set.discard(3)  # no error
my_set.pop()       # removes random element
my_set.clear()
