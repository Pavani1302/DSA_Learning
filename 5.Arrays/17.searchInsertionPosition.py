def searchInsertionPosition(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
                return i
    return len(nums)
        
nums = [2,5,9,11,21]
target = 25
print(searchInsertionPosition(nums,target))