# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.


# Kadane's algorithm
# Compare current array value with previous subarray max value
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
                
            curSum += n
            maxSub = max(curSum, maxSub)
            
        return maxSub