#leetcode 125 Easy two pointer
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.alphaNumeric(s[l]):
                l += 1
            while r > l and not self.alphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


    def alphaNumeric(self,c):
        return (
            ('A' <= c <= 'Z') or
            ('a' <= c <= 'z') or
            ('0' <= c <= '9')
        ) 
    
    # class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     newStr = ''
    #     for c in s:
    #         if c.isalnum():
    #             newStr += c.lower()
    #     return newStr == newStr[::-1]