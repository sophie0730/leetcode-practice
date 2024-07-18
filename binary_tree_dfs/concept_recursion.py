class Node:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def dfs_preorder(node):  # root, left, right
    if node:
        print(node.value, end=" ")
        dfs_preorder(node.left)
        dfs_preorder(node.right)


def dfs_inorder(node):  # left, root, right
    if node:
        dfs_inorder(node.left)
        print(node.value, end=" ")
        dfs_inorder(node.right)


def dfs_postorder(node):  # left, right, root
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=" ")


root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Pre-order Traversal:")
dfs_preorder(root)
print("\nIn-order Traversal:")
dfs_inorder(root)
print("\nPost-order Traversal:")
dfs_postorder(root)
