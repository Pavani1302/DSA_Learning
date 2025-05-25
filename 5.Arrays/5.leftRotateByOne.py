def rotateOne(arr):
    new_arr = arr[1:] + [arr[0]]
    return new_arr
arr = [1,2,3,4,5]
print(rotateOne(arr))