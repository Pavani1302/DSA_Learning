def reverse(arr,left,right):
    if left >= right:
        return
    arr[left], arr[right] = arr[right], arr[left]
    reverse(arr,left+1,right-1)
arr = input("Enter numbers: ")
arr = list(map(int, arr.split(',')))
reverse(arr, 0, len(arr) - 1)
print("Reversed array:", arr)