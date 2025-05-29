def maxCon(arr):
    count = 0
    result = 0
    for n in arr:
        if n == 1:
            count += 1
            if count > result:
                result = count
        else:
            count = 0
    return result
arr_1 = [1,1,0,1,1,1]
print(maxCon(arr_1))