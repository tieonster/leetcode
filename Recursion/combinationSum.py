# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Backtracking
# Very similar to combinations and subsets question
# Have backtracking function, and base case
# Count sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        
        def backtrack(start, comb):
            if sum(comb) > target:
                return
            
            if sum(comb) == target:
                res.append(comb.copy())
            
            for i in range(start, n):
                comb.append(candidates[i])
                backtrack(i, comb)
                comb.pop()
                
        backtrack(0, [])
        
        return res