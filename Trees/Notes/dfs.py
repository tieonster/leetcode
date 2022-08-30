## DFS Algorithms


## Iterative Approach using Stack

results = []

stack = [root]

while (len(stack)) > 0:
    current = stack.pop(-1) # Removes last item from the stack
    results.push(current.val)

    if current.right != null:
        stack.push(current.right)

    if current.left != null:
        stack.push(current.left)


## Recursive Approach

def depthFirstValues(root):
    if (root == null):
        return []
    leftValues = depthFirstValues(root.left)
    rightValues = depthFirstValues(root.right)
    return [root.val] + [leftValues] + [rightValues]