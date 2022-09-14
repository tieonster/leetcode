# Notes:

### BFS
Iterative approach using queue <br />
Initialize queue with root value <br />
Pop root value to current <br />
Append current.left and current.right to q <br />

### DFS
Iterative approach using stack (Similar to queue) <br />
Recursive approach: <br />
1. Set leftValues = dfs(root.left) <br />
2. Set rightValues = dfs(root.right) <br />
return root.val + leftValues + rightValues <br />

### Max Root To Leaf
Recursive approach: <br />
1. Set leftSum = dfs(root.left) <br />
2. Set rightSum = dfs(root.right) <br />
3. Set maxChildPathSum = max(leftSum, rightSum) <br />
return (maxChildPathSum + root.val) <br />

### Min value of BST
Recursive approach: <br />
1. Set leftMin = dfs(root.left) <br />
2. Set rightMin = dfs(root.right) <br />
return min(root.val, leftMin, rightMin) <br />

### Sum of Tree Values
Iterative Approach: (Either BFS or DFS) <br />
Create totalSum variable and increment it with current.val after popping current.val <br />
Recursive Approach: <br />
Simply return root.val + dfs(root.left) + dfs(root.right) <br />

### Tree Includes
Iterative Approach: (Either BFS or DFS) <br />
Check if current val (that has been popped) is equal target <br />
Recursive Approach: <br />
Condition if root.val == target, return true <br />
return dfs(root.left, target) or dfs(root.right, target)

### Tree Traversal
Recursive approach, for preorder, inorder, postorder <br />

All Notes were written based on this youtube tutorial: [TUTORIAL](https://www.youtube.com/watch?v=fAAZixBzIAI)

# Questions:

### Binary Tree Level Order Traversal
BFS <br />
Add a list called level to keep track of level of BFS <br/>
[SOLUTION](https://www.youtube.com/watch?v=6ZnyEApgFYg)

### Construct Binary Tree from Preorder and Inorder Traversal
Root of a tree is always first item in preorder traversal sequence <br />
Find index of root value in inorder sequence <br />
Every value on the left of the number is in left subtree, every value on the right of the number is in right subtree <br />
[SOLUTION](https://www.youtube.com/watch?v=ihj4IQGZ2zc)

### Invert Binary Tree
Recursive way <br />
Set root.left = invertTree(root.right), and root.right = invertTree(root.left) <br />
[SOLUTION](https://www.youtube.com/watch?v=OnSn2XEQ4MY)

### Lowest Common Ancestor of Binary Search Tree
Don't need BFS/DFS, simply use while loop <br/>
Idea here is that both p and q needs to be lower/higher than current. <br />
Cannot have a situation where one is higher, one is lower. That would mean the lowest common ancestor is curr <br />
[SOLUTION](https://www.youtube.com/watch?v=gs2LMfuOR9k)

### Lowest Common Ancestor of Binary Tree
[SOLUTION](https://www.youtube.com/watch?v=WO1tfq2sbsI&t=668s)

### Max Depth of Binary Tree
Use DFS recursion <br />
Increment 1 everytime DFS is called <br />
[SOLUTION](https://www.youtube.com/watch?v=hTM3phVI6YQ&t=635s)

### Same Tree
Use DFS recursive <br />
If both p and q are not empty, return p.val == q.val and dfs(p.left, q.left) and dfs(p.right, q.right)
[SOLUTION](https://www.youtube.com/watch?v=vRbbcKXCxOw&t=48s)
