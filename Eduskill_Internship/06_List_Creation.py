empty_list = []     # Empty list


fruits = ['apple', 'banana', 'cherry']
mixed_list = ['hello', 10, True, 3.14]


print(fruits[0])  # apple   # indexing
print(fruits[1])  # banana

print(fruits[-1]) # cherry      # Negative indexing starts from the end
print(fruits[-2]) # banana


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[:5])      # [0, 1, 2, 3, 4]
print(numbers[3:])      # [3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])     # [2, 3, 4, 5, 6]
print(numbers[::2])     # [0, 2, 4, 6, 8]
print(numbers[1:8:3])   # [1, 4, 7]
print(numbers[::-1])    # reversed list


print(numbers.append(10))
print(numbers.insert(11, 11))
print(numbers.remove(11))
print(numbers.pop(10))
