# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None: return TreeNode(val)

        self._insertIntoBST(root, val)
        return root

    def _insertIntoBST(self, root, val):
        if root == None: return
        if val < root.val:
            if root.left != None:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right != None:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
