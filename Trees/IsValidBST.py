# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        self.prevVal = float("inf")
        self.res = True
        self._isValidBST(root)
        return self.res

    def _isValidBST(self, root):
        if root == None or self.res == False:
            return

        self._isValidBST(root.left)

        if self.prevVal != float("inf"):
            if self.prevVal >= root.val:
                self.res = False
        self.prevVal = root.val

        self._isValidBST(root.right)

if __name__ == "__main__":
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n6 = TreeNode(6)

    n5.left = n1; n5.right = n4
    n4.left = n3; n4.right = n6

    s = Solution()
    print(s.isValidBST(n5))
