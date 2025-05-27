def findUnion(arr_1, arr_2):
    result = []
    for num in arr_1:
        if num not in result:
            result.append(num)
    for num in arr_2:
        if num not in result:
            result.append(num)
    return result

arr_1 = [1, 2, 3, 4, 5]
arr_2 = [1, 2, 7]
print(findUnion(arr_1,arr_2))