def selection(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

arr1 = [15,12,34,9,25]
arr2 = [15,35,5,95]
print(selection(arr1))
print(selection(arr2))