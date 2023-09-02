# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Approach here is to use backtracking algorithm
# Create another function, which stores the number of openN and closeN brackets
# Identify the 3 conditions:
# return if openN == closeN == n
# only add parantheses if openN < n (First Strategy)
# only add closing paranthesis if openN > closeN
# Recursion for each of these conditions, remember to pop out last element

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add paranthesis if open < n
        # Only add closing paranthesis if open > close
        # Valid IFF open == close == n

        stack = []
        res = []

        def backtrack(openN, closeN):
            print(stack)
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if openN > closeN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0,0)
        return res

                 
            
