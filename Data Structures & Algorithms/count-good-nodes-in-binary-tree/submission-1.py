# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Just need to keep track of largest seen prev for a given node
        res = 0
        queue = deque()
        queue.append((root, float("-inf")))

        while queue:
            node, maxi = queue.popleft()
            if node.val >= maxi:
                res += 1
            
            if node.left:
                queue.append((node.left, max(maxi, node.val)))
            if node.right:
                queue.append((node.right, max(maxi, node.val)))
        
        return res
