# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. If target exists, 
# then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity


# Recursive/Iterative method
# Have two pointers: low and high
# Have another pointer middle

# Change the low and high pointer to middle respectively
class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
            def dfs(array, low, high, target):
                if high >= low:
                    middle = (low + high) // 2
                                    
                    if target == array[middle]:
                        return middle
                    
                    elif target > array[middle]:
                        return dfs(array, middle+1, high, target)

                    else: 
                        return dfs(array, low, middle-1, target)
                    
                else:
                    return -1
                    
            index = dfs(nums, 0, len(nums)-1, target)
            
            return index
            
        
# Iterative method
# Same idea but using while loop instead
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1