# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has 
# both p and q as descendants (where we allow a node to be a descendant of itself).”

# Solution Explanation: Lowest Common Ancestor Binary Tree (Tushar Roy)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Return root if both left and right have value
        if left and right:
            return root
        
        # Return none if both left and right are null
        if not left and not right:
            return None
        
        # return left if only left has value
        if left:
            return left
        # return right if only right has value
        else:
            return right