def singleNum(arr):
    new_arr = []
    for num in arr:
        if num not in new_arr:
            new_arr.append(num)
        else:
            new_arr.remove(num)
    return new_arr.pop()
arr_1 = [2,2,1,1,3,4,3]
print(singleNum(arr_1))