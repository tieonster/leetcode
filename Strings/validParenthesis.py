# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Idea is to use a stack
# Create a hashmap that matches each closing bracket to its corresponding open bracket
# Loop through each character in the string
# Append it to the stack if character is opening bracket
# If char is closing bracket, then check to see if the last element in the stack is its corresponding opening bracket. If it is, then pop that opening bracket and continue
# If not return False
# Return true is loop is finished

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" : "["}
        
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return True if not stack else False
                
                