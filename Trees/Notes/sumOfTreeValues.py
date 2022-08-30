# Find the sum of all tree values

# Method 1 (Use an iterative approach, can be either DFS or BFS)
def treeSum(root):
    if (root == null):
        return 0
    queue = [root]
    totalSum = 0
    while (len(queue)) > 0:
        current = queue.popleft()
        totalSum += current.val
        if (current.left != null):
            queue.append(root.left)
        if (current.right != null):
            queue.append(root.right)

    return totalSum

# Method 2 (Recursive)
def treeSum(root):
    if (root == null):
        return 0
    return root.val + treeSum(root.left) + treeSum(root.right)