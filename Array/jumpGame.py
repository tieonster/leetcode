# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

# Greedy Approach
# Goal is to iterate from the last element
# Set goal variable which contains the index of the last element
# Check if the index + number of jumps on the index is more than or equals to the goal index
# If it fulfills the criteria, it means that it is able to jump from the current index to the goal index
# Set goal to the current index
# After finishing the loop, if the goal is at index 0, it means that it is successful.
# Return True, else Return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        if goal == 0:
            return True

        else:
            return False