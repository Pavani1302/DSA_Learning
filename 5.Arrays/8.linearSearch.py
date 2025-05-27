def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [2, 3, 4, 5, 3] 
target_1 = 3
target_2 = 9 
print(linearSearch(arr,target_1))
print(linearSearch(arr,target_2))