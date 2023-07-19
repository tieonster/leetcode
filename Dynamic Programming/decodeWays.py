# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the 
# reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is 
# different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

class Solution:
    def numDecodings(self, s: str) -> int:
        # ChatGPT solution
        n = len(s)
        # Each element dp[i] will represent the number of ways to decode the substring s[0:i]
        dp = [0] * (n + 1)
        # Initialize dp[0] = 1 to represent the empty string (there is only one way to decode an empty string).
        dp[0] = 1

        for i in range(1, n + 1):
            # If s[i-1] is not '0', we can form a valid single-digit number and consider it as a separate decoding possibility.
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # form a valid two-digit number and consider it as another possibility
            if i > 1 and (s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 1] <= '6')):
                dp[i] += dp[i - 2]

        return dp[n]
        
            