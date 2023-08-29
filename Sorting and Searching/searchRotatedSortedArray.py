# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Idea here is to conduct a binary search, but this time there are more conditions (4 cases in total)
# Uses the iterative method here
# Create 3 separate left, middle, right pointers
# While loop to check if l <= r
# return middle if target == middle number
# Search left portion: i.e. If number on left less than middle number, means the left portion is strictly increasing
# Next check: if target <= middle number and if target >= left number, means target lies within there, search left portion
# Set r = middle - 1 to search left portion
# else set l = middle + 1 to search right portion
# Search right portion: i.e. If number on right greater than middle number, means the right portion is strictly increasing
# if target >= middle number and if target <= right number, means target lies within right portion.
# Set l = middle + 1 to search right portion
# else set r = mid - 1 to search in left portion
# Break out of while loop and return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            # left sorted portion (Only one side is strictly increasing)
            if nums[left] <= nums[middle]: # Check if its strictly increasing 
                if target <= nums[middle] and target >= nums[left]: # If target less than middle and target more than left, then search the left portion
                    right = middle - 1

                else:
                    left = middle + 1
                    
            # right sorted portion, (Only one side is strictly increasing)
            else:
                if target >= nums[middle] and target <= nums[right]:
                    left = middle + 1

                else:
                    right = middle - 1

        return -1