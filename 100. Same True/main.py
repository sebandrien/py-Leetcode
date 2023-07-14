# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        # One of the trees is empty, or the values of the current nodes differ
        if p is None or q is None or p.val != q.val:
            return False
        # Recursively compare the left and right sub-trees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
