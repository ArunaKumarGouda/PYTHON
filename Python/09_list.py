friends = ["apple", "orande", 5]            # We can change a perticulr value of a list
                                            # We can not change a strings perticular character in a list
print(friends)                              # To print a list

friends.append("Aruna")                     # insert a value at the end of the list
print(friends)

nums = [57, 23, 6, 31, 73, 24]
print(nums)

nums.reverse()
print("The reverse list is : ", nums)       # reverse a list

nums.sort()
print("The sorted list is : ", nums)        # Sorted list


nums.insert(3, 88)                          # insert a value to the list at any index (index, value)
print(nums)

li = [21, 45, 87, 2, 5, 10]
value = li.pop(2)
print(value)
print(li)                                   # Remove the value at index 2 and print the list


lists = ["fruits", 45, "Banana"]
print(lists)
lists.remove(45)
print(lists)                                  # Wronge
