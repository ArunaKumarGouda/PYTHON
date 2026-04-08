def decrementList(arr):
    result = []
    for i in arr:
        result.append(i - 1)
    
    return result

arr = [3, 66, 25, 63, 25, 7]
print("The array is: ", arr)
print("After decreasing the value of 1 in each element, the array is: ", decrementList(arr))
