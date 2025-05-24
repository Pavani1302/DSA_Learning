def sortedArray(arr):
    temp_arr = arr[:]
    new_arr = []
    while temp_arr:
        min_ele = temp_arr[0]
        for i in range(1,len(temp_arr)):
            if temp_arr[i] < min_ele:
                min_ele = temp_arr[i]
        new_arr.append(min_ele)
        temp_arr.remove(min_ele)
    return new_arr == arr
arr_1 = [5,1,24,84,76]
arr_2 = [2,5,8,9,21]
print(sortedArray(arr_1))
print(sortedArray(arr_2))