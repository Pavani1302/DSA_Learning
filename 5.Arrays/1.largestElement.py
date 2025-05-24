def largestEle(arr):
    max_ele = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]
    return max_ele
arr_1 = [5,1,25,6,45,31]
print(largestEle(arr_1))