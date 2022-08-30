## BFS Algorithms


## Iterative Approach using Queue
# Check if root is null first

# Initialize queue = [root]

while (len(queue)) > 0:
    current = queue.popleft() # Removes front element
    results.push(current.val)

    if current.right != null:
        queue.append(current.right)

    if current.left != null:
        queue.append(current.left)


## Recursive Approach
# Not recommended since queue data structure is used here