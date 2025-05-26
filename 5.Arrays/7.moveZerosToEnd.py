def moveToEnd(arr):
    arr_1 = []
    arr_2 = []
    for num in arr:
        if num != 0:
            arr_1.append(num)
        else:
            arr_2.append(num)
    return arr_1 + arr_2
arr = [1,0,9,2,0,5,3]
print(moveToEnd(arr))