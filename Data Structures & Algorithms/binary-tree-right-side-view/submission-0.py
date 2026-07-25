# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Right value of BFS
        res = []
        queue = deque([root])

        while queue:
            right_node = None
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    right_node = node
            if right_node:
                res.append(right_node.val)

        return res
