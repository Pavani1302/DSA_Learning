def majEle(arr):
    majEle = {}
    for num in arr:
        if num in majEle:
            majEle[num] += 1
        else:
            majEle[num] = 1
        if majEle[num] > len(arr)//2:
            return num
arr_1 = [2,2,1,1,1,2,2]
print(majEle(arr_1))
arr_2 = [3,5,3]
print(majEle(arr_2))