def two_sum(nums, target):
    l,r = 0 , len(nums) - 1

    while l < r:
        sum = nums[l] + nums[r]
        if (sum == target):
            return [l+1,r+1]
        if (sum < target):
            l += 1
        else:
            r -= 1

print(two_sum([1,2,3,4,5,6], 5))