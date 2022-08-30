# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}
        
        for i, num in enumerate(nums):
            wanted_val = target - num
            if wanted_val not in mapping:
                mapping[num] = i
                
            else:
                return [i, mapping[wanted_val]]