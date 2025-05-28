def missingNum(arr):
    n = len(arr)
    total = (n * (n+1)) // 2
    return total - sum(arr)
arr = [1,0,3]
print(missingNum(arr))