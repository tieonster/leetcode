# Given the root of a binary tree, imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.

# Idea is to do dfs
# Keep track of the levels of the dfs iteration
# Have a rightSide variable that refreshes itself on each new level of the bfs tree
# Do a for loop to go through each node of the level, and append the right most node of each level to res (After the entire for loop)
# Return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                curr = q.popleft()
                
                if curr:
                    rightSide = curr
                    q.append(curr.left)
                    q.append(curr.right)

            if rightSide:
                res.append(rightSide.val)

        return res



        