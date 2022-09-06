# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.


# Idea here is to conduct a binary search, but this time there are more conditions
# Uses the iterative method here
# Create 3 separate left, middle, right pointers
# While loop to check if l <= r
# return middle if target == middle number
# Search left portion: i.e. If number on left less than middle number, than 2 things can happen
# if target > middle number (Search right portion by right) or if target < left number (Search Right portion)
# Set l = mid + 1
# else set r = mid - 1
# Search right portion:
# if target < middle number (Search left portion by right) or if target > right number (Search left portion)
# Set r = mid - 1
# else set l = mid + 1
# Break out of while loop and return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
            l, r = 0, len(nums) - 1
                
            while l <= r:
                mid = (l+r) // 2
                if target == nums[mid]:
                    return mid

                # left sorted portion
                if nums[l] <= nums[mid]:
                    if target > nums[mid] or target < nums[l]:
                        l = mid + 1 # Search the right portion if target is more than middle number or if target is less than extreme left array entry
                    else:
                        r = mid - 1

                # right sorted portion
                else:
                    if target < nums[mid] or target > nums[r]:
                        r = mid - 1

                    else:
                        l = mid + 1
            return -1
                        