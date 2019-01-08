# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None: return None
        self.count = k
        self.val = 0
        self._kthSmallest(root)
        return self.val

    def _kthSmallest(self, root):
        if root == None: return
        self._kthSmallest(root.left)
        self.count -= 1
        if self.count == 0:
            self.val = root.val
            return
        self._kthSmallest(root.right)
