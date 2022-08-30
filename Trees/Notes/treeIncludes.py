# # Tree includes problem checks if tree contains a certain value

# Method 1 (BFS Iterative)
def treeIncludes(root, target):
    queue = [root]
    while (len(queue) > 0):
        current = queue.popleft() # remove from front of queue
        if current == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return False


# Method 2 (DFS)
def treeIncludes(root, target):
    if (root == null):
        return False
    if (root.val == target):
        return True
    return treeIncludes(root.left, target) or treeIncludes(root.right, target)