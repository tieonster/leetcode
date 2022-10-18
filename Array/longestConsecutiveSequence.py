# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

# Need to check each element in nums and see if it is the start of a sequence
# To determine if it is the start of a sequence, check if the immediate number to the left and see if it exists in nums
# If it does not exist, then start checking to see if the immediate number to the right of the sequence exists, and keep appending to the length

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for num in nums:
            # Checks if num is the start of a sequence
            if (num - 1) not in numSet:
                length = 1
                while (num + 1) in numSet:
                    length += 1
                    num += 1
                longest = max(length, longest)
                
        return longest
            