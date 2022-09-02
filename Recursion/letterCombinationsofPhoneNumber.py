# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.


# Makes use of recursion and backtracking
# Base case: Check if length of current string is same as length of original digits string
# for loop in backtrack function to loop through letters in mapping
# Slightly different in that we used a for loop here

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        res = []
        
        def backtrack(i, currStr):
            if len(currStr) == len(digits):
                res.append(currStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, currStr + c)
                
        if digits:
            backtrack(0, "")
            
        return res
        
        