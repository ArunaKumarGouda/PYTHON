#User function Template for python3
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# 1. Use zip() to combine multiple lists into a single iterable 
########### Write your code below ###############
zipped = zip(list1, list2)# Your code here
########### Write your code above ###############
print(list(zipped))  # Converts to list for display

# 2. Use filter() with lambda function to filter out numbers greater than 2 in list1 
########### Write your code below ###############
filtered = filter(lambda x: x <= 2, list1)# Your code here
########### Write your code above ###############
print(list(filtered))

# 3. Using map() with lambda function to multiply each number of list1 by 2
########### Write your code below ###############
mapped =  map(lambda x: x * 2, list1)# Your code here
########### Write your code above ###############
print(list(mapped))
