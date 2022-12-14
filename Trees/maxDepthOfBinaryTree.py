# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Method 1 (Recursion)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Check for empty tree
        if not root:
            return 0
        
        # Check how many times algo recurses
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Method 2 (BFS)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft() # Remove element at the front of the queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level