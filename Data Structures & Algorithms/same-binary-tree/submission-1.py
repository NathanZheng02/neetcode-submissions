# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Case: If they are both None, then return True
        if not p and not q:
            return True
        
        # Base Case: If one of them is None, but the other one isn't, return False
        if not p or not q:
            return False

        # Recurse and compare
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val