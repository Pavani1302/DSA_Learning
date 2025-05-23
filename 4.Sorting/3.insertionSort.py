def insertion(arr):
    n = len(arr)
    for i in range(n):
        j = i
        while (j>0 and arr[j-1]>arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr
arr_1 = [4,12,34,8,6]
print(insertion(arr_1))