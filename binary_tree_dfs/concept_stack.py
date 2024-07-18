class Node:
    def __init__(self, value=0, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def dfs_preorder(root):
    if not root:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value, end=" ")
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)


def dfs_inorder(root):
    if not root:
        return

    stack = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        node = stack.pop()
        print(node.val, end=" ")
        current = current.right


def dfs_postorder(root):
    if not root:
        return

    stack1 = [root]
    stack2 = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.right:
            stack2.append(node.right)
        if node.left:
            stack2.append(node.left)

    while stack2:
        node = stack2.pop()
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
