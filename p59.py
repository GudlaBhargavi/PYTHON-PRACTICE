def find_duplicate(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)

print(find_duplicate([1, 3, 4, 2, 2]))