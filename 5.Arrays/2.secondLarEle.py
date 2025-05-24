def largeEle(arr):
    max_ele = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > max_ele:
            max_ele = arr[i]
    return max_ele
def secLargeEle(arr):
    max_ele = largeEle(arr)
    new_arr = [x for x in arr if x != max_ele]
    if len(new_arr) == 0:
        return None
    return largeEle(new_arr)
arr_1 = [5,1,25,6,45,31]
arr_2 = [5,5,5]
print(secLargeEle(arr_1))
print(secLargeEle(arr_2))