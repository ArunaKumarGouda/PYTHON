set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union |
union_set = set_a | set_b
print(union_set)  # {1, 2, 3, 4, 5, 6}

# Using .union()
union_set = set_a.union(set_b)
print(union_set)

# Intersection
# Using &
intersection_set = set_a & set_b
print(intersection_set)  # {3, 4}

# Using .intersection()
intersection_set = set_a.intersection(set_b)
print(intersection_set)

# Difference
print(set_a - set_b)  # {1, 2}
print(set_b - set_a)  # {5, 6}

# Symmetric Difference
print(set_a ^ set_b)  # {1, 2, 5, 6}


# Other Useful Set Methods
# .issubset() → checks if one set is subset of another
# .issuperset() → checks if one set is superset
# .isdisjoint() → checks if sets have no common elements



# Hands-on Practice with Dictionaries and Sets
# 1. Dictionary Example
product = {
    'product_id': 'P1001',
    'name': 'Wireless Mouse',
    'brand': 'LogiTech',
    'price': 1200.50,
    'in_stock': True,
    'tags': ['electronics', 'computer accessories', 'wireless']
}

print(product)
print(type(product))

# 2. Accessing Dictionary Values
product_name = product['name']
product_price = product.get('price')
product_tags = product['tags']

print(product_name)
print(product_price)
print(product_tags)

# Access list inside dictionary
print(product_tags[0])

# Safe access
print(product.get('warranty', 'Not Available'))



# 3. Set Example
order_ids = {101, 102, 103, 101, 104, 102, 105}

print(order_ids)

order_ids.add(106)
order_ids.add(103)  # ignored duplicate

order_ids.remove(102)

print(order_ids)



# 4. Dictionary vs Set Example
# Dictionary
student_grades = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 85,
    'David': 95
}

print(student_grades['Bob'])

# Set
unique_numbers = {10, 20, 30, 20, 40}
print(unique_numbers)

print(30 in unique_numbers)
print(100 in unique_numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)


# Iterating Through Dictionaries
my_dict = {
    "name": "Aruna",
    "age": 20
}

# 1. Loop through keys
for key in my_dict:
    print(key)

# 2. Loop through values
for value in my_dict.values():
    print(value)

# 3. Loop through key-value pairs
for key, value in my_dict.items():
    print(key, value)

# 4. With index
for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)
