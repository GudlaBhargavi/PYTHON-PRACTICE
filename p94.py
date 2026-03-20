nums = [1,2,3,4,5,6,7]
target = 5

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2
    
    if nums[mid] == target:
        print("Found at index", mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1