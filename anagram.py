#242 leetcode Easy
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sHash = {}
        tHash = {}

        for i in range(len(s)):
            if s[i] in sHash:
                sHash[s[i]] += 1
            else:
                sHash[s[i]] = 1
            if t[i] in tHash:
                tHash[t[i]] += 1
            else:
                tHash[t[i]] = 1
            # sHash[s[i]] = 1 + sHash.get(s[i], 0)
            # tHash[t[i]] = 1 + tHash.get(t[i], 0)
        return sHash == tHash #oder of insertion doesn't matter in hash map