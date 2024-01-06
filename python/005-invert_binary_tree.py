## Problem 226. Invert Binary Tree
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        rootINV = root
        if rootINV == None:
            return rootINV
        
        # Backtrack nodes
        self.invertTree(rootINV.left)
        self.invertTree(rootINV.right)

        # Swap
        rootINV.left, rootINV.right = rootINV.right, rootINV.left
        return rootINV


# Test
if __name__ == '__main__':
  root = TreeNode(4)
  root.left = TreeNode(2)
  root.right = TreeNode(7)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(9)
  print(Solution().invertTree(root))