# Preorder Traversal
def preOrder(root):
    if (root != null):
        return ([root.val] + [preOrder(root.left)] + [preOrder(root.right)])

# Inorder Traversal
def inOrder(root):
    if (root != null):
        return ([inOrder(root.left)] + [root.val] + [inOrder(root.right)])


# Postorder Traversal
def postOrder(root):
    if (root != null):
        return ([postOrder(root.left)] + [postOrder(root.right)] + [root.val])
