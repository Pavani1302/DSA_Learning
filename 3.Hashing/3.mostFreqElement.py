def frequentElement(arr):
    arr_freq = {}
    for num in arr:
        if num in arr_freq:
            arr_freq[num] += 1
        else:
            arr_freq[num] = 1
    max_fre = -1
    result = float('inf')
    for num in arr_freq:
        if arr_freq[num] > max_fre:
            max_fre = arr_freq[num]
            result = num
        elif arr_freq[num] == max_fre:
            result = min(result, num)
    return result
print(frequentElement([1, 1, 2, 2, 3, 3, 4, 4, 4]))
print(frequentElement([1, 1, 2, 2, 2, 3, 3, 4, 4, 4]))