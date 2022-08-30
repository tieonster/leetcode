# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.



# Pseudo-code:

# 1) Sort both strings according to alphabetical order: O(n log n)
# 2) Loop through 2nd anagram and minus character count 
# for each character encountered, if value for all char in dict = 0, means it is anagram