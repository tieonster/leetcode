# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Use DFS recursion from bottom up
# Return 2 parameters for every dfs call, one to determine if tree is balanced, one to determine height of subtree
# To calculate height of the tree, use 1 + max(left, right)
# Ingenious call

# Code runs in O(n) time complexity, because only running through all nodes once

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1]-right[1]) <= 1
            
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]
        
         