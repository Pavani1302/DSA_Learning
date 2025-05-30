def sortColors(arr):
    red = []
    white = []
    blue = []
    for num in arr:
        if num == 0:
            red.append(num)
        elif num == 1:
            white.append(num)
        else:
            blue.append(num)
    arr[:] = red + white + blue
    return arr
arr_1 = [2,0,2,1,1,0]
print(sortColors(arr_1))