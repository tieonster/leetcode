# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Recursion and backtracking
# Set results list
# Create backtracking function and set base case if len(comb) == k
# Include for loop to iterate through all n numbers

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb.copy()) # Append copy so that original comb can still be manipulated by the recursion calls
                return
            for i in range(start, n+1):
                comb.append(i)
                # print(comb)
                backtrack (i+1, comb)
                comb.pop()
                # print(comb)
        backtrack(1, [])
        
        return res