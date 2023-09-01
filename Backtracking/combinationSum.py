# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Approach is to use backtracking, calling it recursively
# In the dfs function bel

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return

            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, [], 0)

        return res