# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:
        # # My Solution
        # stack = []

        # for char in s:
        #     # Check to make sure that first char is not closing bracket
        #     if stack == [] and (char == ")" or char == "]" or char == "}"):
        #         return False

        #     # Check to see if first char is open bracket or not
        #     if char == "(" or char == "[" or char == "{":
        #         stack.append(char)

        #     # Cases to deal with closing bracket
        #     elif stack and char == ")":
        #         if stack[-1] != "(":
        #             return False
        #         else:
        #             stack.pop()

        #     elif stack and char == "]":
        #         if stack[-1] != "[":
        #             return False
        #         else:
        #             stack.pop()

        #     elif stack and char == "}":
        #         if stack[-1] != "{":
        #             return False
        #         else:
        #             stack.pop()

        # return False if stack else True

        # Neetcode solution
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)

        return True if not stack else False