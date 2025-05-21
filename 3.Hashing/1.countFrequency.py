def count_frequency(arr):
    freq_table = {}
    for num in arr:
        if num in freq_table:
            freq_table[num] += 1
        else:
            freq_table[num] = 1
    return freq_table

arr = [1,2,3,1,4,1,2,6]
print(count_frequency(arr))