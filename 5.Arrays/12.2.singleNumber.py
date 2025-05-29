def singleNum(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
arr = [2,5,2,7,6,7,6]
print(singleNum(arr))