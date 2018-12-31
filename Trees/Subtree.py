# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s and not t: return True
        if not s and t: return False
        if s and not t: return False

        res = [False]
        finCheck = [False]
        self._isSubtree(s, t, res, finCheck)
        return res[0]

    def _isSubtree(self, s, t, res, finCheck):
        if s == None or finCheck[0]: return
        res[0] = True
        self._checkSubtree(s, t, res)
        if res[0] == True: finCheck[0] = True

        self._isSubtree(s.left, t, res, finCheck)
        self._isSubtree(s.right, t, res, finCheck)

    def _checkSubtree(self, s, t, res):
        if not s and not t: return
        if not s and t:
            res[0] = False
            return
        if s and not t:
            res[0] = False
            return
        if s.val != t.val:
            res[0] = False
        self._checkSubtree(s.left, t.left, res)
        self._checkSubtree(s.right, t.right, res)

if __name__ == "__main__":
    n3 = TreeNode(3)
    n4a = TreeNode(4)
    n5 = TreeNode(5)
    n1a = TreeNode(1)
    n2a = TreeNode(2)
    n3.left = n4a; n3.right = n5
    n4a.left = n1a; n4a.right = n2a

    n4b = TreeNode(4)
    n1b = TreeNode(1)
    n2b = TreeNode(2)
    n4b.left = n1b; n4b.right = n2b

    s = Solution()
    print(s.isSubtree(n3, n4b))
