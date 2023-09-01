# Given the root of a binary search tree, and an integer k, return the kth smallest value 
# (1-indexed) of all the values of the nodes in the tree.

# The idea is to make use of in-order traversal, which will return the elements sorted from left to right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Own solution
        # res = []
        # q = deque([root])

        # # bfs
        # while q:
        #     curr = q.popleft()
        #     res.append(curr.val)

        #     if curr.left:
        #         q.append(curr.left)

        #     if curr.right:
        #         q.append(curr.right)

        # # Using heap
        # heapq.heapify(res)

        # for i in range(k):
        #     num = heapq.heappop(res)

        # return num

        # Recursive approach (In-order traversal)
        # arr = []
        # def findNum(node, arr):
        #     if not node:
        #         return
        #     findNum(node.left, arr)
        #     arr.append(node.val)
        #     findNum(node.right, arr)
        # findNum(root, arr)

        # return arr[k- 1]


        # Neetcode solution
        n = 0
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1

            if n == k:
                return curr.val

            curr = curr.right

