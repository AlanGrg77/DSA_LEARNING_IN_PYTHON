def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        y = target - num

        if y in seen:
            return [seen[i], i]
        
        seen[num] = i

print(two_sum([1,2,3,4,5,7], 5))