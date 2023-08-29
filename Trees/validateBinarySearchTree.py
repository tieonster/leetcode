# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.


# Create another helper function that uses recursion
# Have a left and right boundary for each iteration of the recursion. 
# This boundary needs to be updated in every iteration of the dfs
# any node on the left of the root, even grandchild, has to be smaller than the root node.
# Every node on the right of the root, even the grandchildren, has to be larger than the root node. 
# Check if the current node value lies between left and right boundary. If it does not, then return false
# Otherwise, iterate through the remaining subtrees recursively.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # valid takes in node, left and right boundaries as parameters
        def valid(node, leftBound, rightBound):
            # Returns True if reached null node
            if not node:
                return True
            
            # Check node value and see if it is larger than the left boundary and smaller thatn the right boundary respectively. If it is not, then it is not a BST
            if not (node.val < rightBound and node.val > leftBound):
                return False
            
            # Iterate through left and right subtrees, and setting the boundaries accordingly
            return (valid(node.left, leftBound, node.val) and valid(node.right, node.val, rightBound))
                    
        return valid(root, float("-inf"), float("inf"))