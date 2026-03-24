list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))

zipped = zip(list1, list2)
print(list(zipped))

filtered = filter(lambda x: x <= 2, list1)
print(list(filtered))

mapped = map(lambda x: x * 2, list1)
print(list(mapped))
