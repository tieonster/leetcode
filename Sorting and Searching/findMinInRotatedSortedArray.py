# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
# For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# To find the minimum element in a rotated sorted array using O(log n) time complexity, 
# you can utilize a modified binary search approach. 
# Since the array is rotated, the minimum element will always be on the side where the values are decreasing instead of increasing.

# In this algorithm:

# The left and right pointers define the search range. Initially, they point to the first and last elements of the array.
# Inside the loop, you calculate the middle index mid using (left + right) // 2.
# Compare the value at nums[mid] with the value at nums[right]:
# If nums[mid] is greater than nums[right], it means the minimum element is on the right side. Move the left pointer to mid + 1.
# Otherwise, the minimum element is on the left side or at mid. Move the right pointer to mid.
# The loop continues until the left pointer is equal to the right pointer, which means you've found the minimum element.
# This algorithm effectively narrows down the search range by half in each iteration, resulting in O(log n) time complexity.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # The minimum element is on the right side
                left = mid + 1
            else:
                # The minimum element is on the left side or at mid
                right = mid
        
        return nums[left]