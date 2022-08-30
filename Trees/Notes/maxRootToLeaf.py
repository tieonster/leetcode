# Finding the max root to leaf path sum

# Recursive
def maxPathSum(root):
    if (root == null):
        return None
    if (root.left == null and root.right == null):
        return root.val
    leftSum = maxPathSum(root.left)
    rightSum = maxPathSum(root.right)
    maxChildPathSum = max(leftSum, rightSum)
    return (maxChildPathSum + root.val)
