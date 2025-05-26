def rightRotateK(arr, k):
    k = k % len(arr)
    if k != 0:
        arr[:] = arr[-k:] + arr[:-k]
        return arr

arr = [3,7,8,9,10,11]
k = 2
print(rightRotateK(arr,k))