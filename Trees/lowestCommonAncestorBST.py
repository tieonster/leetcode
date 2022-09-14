# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: 
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that 
# has both p and q as descendants (where we allow a node to be a descendant of itself).”


# BST means everything on the left has a small value, everything on the right has a larger value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Idea here is that both p and q needs to be lower/higher than current.
# Cannot have a situation where one is higher, one is lower. That would mean the lowest common ancestor is curr
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # if current node is smaller than p and q, move current node to rigth subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # if current node is larger than p and q, move current node to left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr