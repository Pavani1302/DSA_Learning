def threeConsecutiveOdd(arr):
    for i in range(len(arr)-2):
        if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]!=0:
            return True
    return False
arr_1 = [2,6,4,1]
print(threeConsecutiveOdd(arr_1))
arr_2 = [1,2,34,3,4,5,7,23,12]
print(threeConsecutiveOdd(arr_2))