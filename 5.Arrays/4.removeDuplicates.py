def removeDup(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
    return new_arr
arr_1 = [8,5,1,9,8,5,2]
arr_2 = [5,2,8,1,9]
print(removeDup(arr_1))
print(removeDup(arr_2))