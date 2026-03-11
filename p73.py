def two_sum(nums, target):
    d = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in d:
            return [d[complement], i]

        d[nums[i]] = i

nums = [2,7,11,15]
print(two_sum(nums,9))