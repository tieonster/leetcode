# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Use the sliding window technique
# Create 2 hashmaps, one that stores the count of the char in s1, another which stores the count of char in s2
# For each iteration of loop, compare the 2 hashmaps
# If they are equal, then return true
# Else continue the loop

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return True

        if len(s1) > len(s2):
            return False

        window_len = len(s1)
        l = 0
        r = window_len - 1
        chars_s1 = collections.defaultdict(lambda: 0)
        chars = collections.defaultdict(lambda: 0)
        
        # Get char count in s1
        for char in s1:
            chars_s1[char] += 1

        # Get char count in s2
        for i in range(window_len):
            chars[s2[i]] += 1

        # Check if char count in s1 is the same as s2
        if chars == chars_s1:
            return True

        # Check for the rest of the windows in s2
        else:
            while r < len(s2):
                chars[s2[l]] -= 1
                
                # Remove entry if its 0
                if chars[s2[l]] == 0:
                    chars.pop(s2[l])

                # Move window 
                l += 1
                r += 1

                # Add to s2 char count
                if r < len(s2):
                    chars[s2[r]] += 1

                else:
                    break
                # Check if s1 count is the same as s2
                if chars == chars_s1:
                    return True

        
        return False
                

                

        
                

                

        