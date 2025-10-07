import collections 
def maxArea(heights):
    res = 0 
    l, r = 0, len(heights) - 1

    while l < r:
        answer = (r - l) * min(heights[l],heights[r])
        res = max(res, answer)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res

def trap_watter(height):
    if not height:
        return 0
    l, r = 0, len(height) - 1
    maxLeft, maxRight = height[l], height[r]
    result = 0

    while l < r:
        if maxLeft < maxRight:
            l += 1
            maxLeft = max(maxLeft, height[l])
            result += maxLeft - height[l]
        else:
            r -= 1
            maxRight = max(maxRight, height[r])
            result += maxRight - height[r]
    return result
def group_anagram(strs):
    res = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return list(res.values())
def two_sumII(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum == target:
            return [l+1,r+1]
        if sum < target:
            l += 1
        else:
            r -= 1
    return []

def threeSum(nums):
    nums.sort()
    result =  []
    for i in range(len(nums) -2):#len(nums) onyl also works but its just extra steps, -2 so that we can creat atleast 3 triplets of pairs like nums[i],nums[l],nums[j]
        if nums[i] > 0:#the first value can't be more than 0 as after adding it, we will never get 0(since its already sorted)
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                result.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
    return result
def contain_duplicate(array):
    seen = set()
    for i in range(len(array)):
        if array[i] in seen:
            return True
        
        seen.add(array[i])  
    return False 
print(contain_duplicate([1,2,3,4,5,6])) 


    

print(maxArea([1,7,3,5,4,7,3,6]))
print(trap_watter([0,2,0,3,1,0,1,3,2,1]))
print(group_anagram(["act","pots","tops","cat","stop","hat"]))
print(threeSum([-1,0,1,2,-1,-4]))
