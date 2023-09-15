# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Do a bottom up approach by calculating diameters from the leaf nodes of binary tree
# Define the diameters and height of a binary tree
# Have dfs recursive function that returns height of binary tree, computer diameter from height
# Diameter of tree is given by 2+left+right
# Height of binary tree with no left and right nodes is -1

# Modifying the code by using a list res as a container for the result 
# allows you to modify a mutable object within the nested function. 
# In Python, when you pass a mutable object (like a list) to a function and modify it inside that function, 
# those changes are reflected in the original object, even if it's within a nested function. 
# This behavior does not apply to immutable objects like integers, so you cannot let res = 0

# Code runs in O(n) time complexity, because only running through all nodes once


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(2+left+right, res[0])
            
            return (1 + max(left, right))
        
        dfs(root)
        
        return res[0]