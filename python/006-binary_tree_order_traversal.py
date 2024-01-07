## Problem 94. Binary Tree Inorder Traversal
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution(object):
  def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    if root == None:
      return root

    IOTroot = list()
    self.dfs(root, IOTroot)

    return IOTroot


  # Depth First Search
  def dfs(self, root, result):
    if root:
      self.dfs(root.left, result)
      result.append(root.val) 
      self.dfs(root.right, result)
    return 
    

# Test
if __name__ == '__main__':
  root = TreeNode(1)
  root.right = TreeNode(2)
  root.right.left = TreeNode(3)
  print(Solution().inorderTraversal(root))
        

        