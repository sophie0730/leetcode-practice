# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        if not root:
            return 0

        def dfs(node, max_val, ans):
            if not node:
                return 0

            if node.val >= max_val:
                ans[0] += 1
                max_val = node.val

            dfs(node.left, max_val, ans)
            dfs(node.right, max_val, ans)

        dfs(root, root.val, ans)
        return ans[0]
