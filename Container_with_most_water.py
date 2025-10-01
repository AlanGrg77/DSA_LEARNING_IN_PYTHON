#leetcode 11 Medium
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        result = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])   
            result = max(result, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result
#time complexity = 0(n) space complexity = 0(1)