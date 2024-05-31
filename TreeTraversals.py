class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=' ')
        inorder_traversal(node.right)

def preorder_traversal(node):
    if node:
        print(node.value, end=' ')
        preorder_traversal(node.left)
        preorder_traversal(node.right)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)
        postorder_traversal(node.right)
        print(node.value, end=' ')


root = Node(100)
root.left = Node(400)
root.right = Node(500)
root.left.left = Node(700)
root.left.right = Node(600)
root.right.left = Node(800)
root.right.right = Node(200)
root.left.right.left = Node(900)
root.right.right.left = Node(300)

# Perform inorder traversal
print("Inorder traversal:")
inorder_traversal(root)
print()

# Perform preorder traversal
print("Preorder traversal:")
preorder_traversal(root)
print()

# Perform postorder traversal
print("Postorder traversal:")
postorder_traversal(root)
print()