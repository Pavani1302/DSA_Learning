def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1,0,-1):
        swap = False
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swap = True
        if swap is False:
            break
    return arr

arr = [15,12,34,9,25]
arr_1 = [12,14,18,34]
print(bubbleSort(arr))
print(bubbleSort(arr_1))