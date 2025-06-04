def pluseOne(arr):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] < 9:
            arr[i] += 1
            return arr
        else:
            arr[i] = 0
    return [1] + arr
arr_1 = [1,2,3]
print(pluseOne(arr_1))
arr_2 = [1,9]
print(pluseOne(arr_2))
arr_3 = [9,9,9]
print(pluseOne(arr_3))