# Given an integer array nums of unique elements, 
# return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.



# My solution:
# Very similar to combinations.py

# Neetcode solution:
# Backtracking and DFS decision trees
# Refer to ipad notes for decision tree
# Going down the tree by 1 level, we basically decide if we want to add
# the numner or NOT add the number.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
# My Solution:
        res = []
        k = 0
        
        def backtrack(start, comb, k):
            if len(comb) == k:
                res.append(comb.copy())
                    
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i+1, comb, k)
                comb.pop()
                
        while k < len(nums)+1:
            backtrack(0, [], k)
            k += 1
            
        return res

# Neetcode solution
        res = []
        subset = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res