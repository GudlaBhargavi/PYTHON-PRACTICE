def find_largest(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

print(find_largest([10, 45, 23, 67, 12]))