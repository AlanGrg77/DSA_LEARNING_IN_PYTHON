#leetcode 3 Mid 
#longest substring without repeating characters
def long_substring(s):
    seen = set()
    l = 0
    length = 0

    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        length = max(length, r - l +1)
    return length

print(long_substring("ababrtyfg"))