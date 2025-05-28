def missingNum(arr):
    for i in range(len(arr)+1):
        if i not in arr:
            return i
arr = [1,0,3]
print(missingNum(arr))