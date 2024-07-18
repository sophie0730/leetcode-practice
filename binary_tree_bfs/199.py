class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deque = collections.deque()
        if root:
            deque.append(root)

        res = []

        while deque:
            size, val = len(deque), 0

            for _ in range(size):
                node = deque.popleft()
                val = (
                    node.val
                )  # 如果左右節點都有，這個迴圈會跑兩次，最後會被右邊那個節點覆蓋掉值
                if node.left:
                    deque.append(node.left)

                if node.right:
                    deque.append(node.right)

            res.append(val)
        return res
