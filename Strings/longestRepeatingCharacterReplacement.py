# You are given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter 
# you can get after performing the above operations.



# Pseudo-code:
# 1) Get count of characters
# 2) Use sliding window approach with 2 pointers
# 3) If window length minus most_freq_count < k, means store res
# 4) If not, increment left pointer by 1, decrement count element by 1

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
                
            else:
                count[s[r]] += 1
                
            window_length = r - l + 1
            
            most_freq_count_val = max(count.values())
            
            if window_length - most_freq_count_val <= k:
                res = max(res, window_length)
                
            else:
                count[s[l]] -= 1
                l += 1
                
        return res