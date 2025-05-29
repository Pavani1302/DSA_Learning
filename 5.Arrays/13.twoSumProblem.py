def twoSum(arr,target):
    for right in range(len(arr)):
        for left in range(right):
            if arr[left] + arr[right] == target:
                return [left,right]
    return []
arr_1 = [2,7,11,5]
print(twoSum(arr_1,target=9))
arr_2 = [3,2,4]
print(twoSum(arr_2,target=6))