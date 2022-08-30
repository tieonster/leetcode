# Given a string s, find the length of the longest substring without repeating characters.



# Create left pointer, right pointer is the one moving through the loop
# Using a set to check for duplicates (Set contians a list of unique values)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
                
                    