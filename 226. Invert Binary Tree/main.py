class Solution:
  def invertTree(self, root: TreeNode) -> TreeNode:
    if not root:
      return null:

    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.right)
    return root
