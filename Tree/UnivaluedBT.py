# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return False
        resVal = root.val
        res = [True]
        self._isUnivalTree(root, res, resVal)
        return res[0]

    def _isUnivalTree(self, root, res, resVal):
        if root == None or res[0] == False: return
        self._isUnivalTree(root.left, res, resVal)
        self._isUnivalTree(root.right, res, resVal)
        if root.val != resVal: res[0] = False

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(1)
    n3 = TreeNode(2)
    n4 = TreeNode(1)
    n5 = TreeNode(1)
    n6 = TreeNode(1)

    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.right = n6
    s = Solution()
    print(s.isUnivalTree(n1))
