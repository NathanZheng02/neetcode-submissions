# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(first, second):
            if not first and not second:
                return True
            
            if not first or not second:
                return False
            
            return isSameTree(first.left, second.left) and isSameTree(first.right, second.right) and first.val == second.val
        

        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) or isSameTree(root, subRoot)