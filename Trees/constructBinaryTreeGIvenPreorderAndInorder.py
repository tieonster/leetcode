# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
# binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


# Note: First value of preorder traversal is the root of the tree (Refer to ipad notes for more detailed drawings)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First element in preorder traversal is always the root of the binary tree
# Element to the immediate right of this first element is the root of the left subtree

# Find this first element in preorder traversal and split inorder traversal into 2 parts
# Left elements of splitted list is on the left subtree, right elements of splitted list is on the right subtree


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) # Index of mid basically tells us how many nodes we want in the left subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        root.right= self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root