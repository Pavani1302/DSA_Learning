def findUnion(arr_1,arr_2):
    result = set(arr_1).union(set(arr_2))
    return result

arr_1 = [1, 2, 3, 4, 5]
arr_2 = [1, 2, 7]
print(list(findUnion(arr_1,arr_2)))