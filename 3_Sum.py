#leetcode 15 Medium

from typing import  List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ < 0:
                    l += 1
                elif summ > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result
 #Time complexity O(n^2) Sapce complexity O(1) or O(n) depning on sorting alogrithm