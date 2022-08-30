# Finding minimum value of Binary Search Tree

# Iterative Approach (Using DFS)
def minValue(root):
    if (root == null):
        return None
    minVal = float('inf')
    stack = [root]

    while (len(stack) > 0):
        curr = stack.pop()
        if curr.val < minVal:
            minVal = curr.val
        if (curr.right != null):
            stack.push(current.right)
        if (curr.left != null):
            stack.push(current.left)

    return (minVal)


# Method 2 (Recursive Approach)
def minVal(root):
    if (root == null):
        return None
    leftMin = minVal(root.left)
    rightMin = minVal(root.right)
    return (min(root.val, leftMin, rightMin))