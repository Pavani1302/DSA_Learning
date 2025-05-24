def sortedArray(arr):
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True
arr_1 = [5,1,24,84,76]
arr_2 = [2,5,8,9,21]
arr_3 = [1,5,9,2,5]
print(sortedArray(arr_1))
print(sortedArray(arr_2))
print(sortedArray(arr_3))