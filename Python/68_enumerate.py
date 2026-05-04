l = [23, 435, 7, 453, 77, 2343]

# index = 0
# for item in l:
#     print(f"The item number at index{index} is {item}")
#     index += 1

# This can be simplified using enumerate function
for index, item in enumerate(l):
    print(f"The item number at index{index} is {item}")
