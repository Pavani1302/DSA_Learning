def secondLargest(arr):
    largest = secLargest = float('-inf')
    for num in arr:
        if num > largest:
            secLargest = largest
            largest = num
        elif largest > num > secLargest:
            secLargest = num
    if secLargest == float("-inf"):
        return -1 
    else:
        return secLargest
arr = [3,8,1,54,98,32]
arr_1 = [5,5,5]
arr_2 = [6,1,6,8,2,8,8]
print(secondLargest(arr)) 
print(secondLargest(arr_1))
print(secondLargest(arr_2)) 