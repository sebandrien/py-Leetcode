class Solution:
  def lowestCommonAncestor(self, root: 'Treenode', p: 'Treenode', q: 'Treenode') -> 'Treenode':
    cur = root

    while cur:
      if p.val > cur.val and q.val > cur.val:
        cur = cur.right
      elif p.val < cur.val and q.val < cur.val:
        cur = cur.left
      else:
        return cur
