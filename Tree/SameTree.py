# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res = [True]
        self._isSameTree(p, q, res)
        return res[0]

    def _isSameTree(self, p, q, res):
        if (p == None and q == None) or res[0] == False:
            return
        if (p == None and q != None):
             res[0] = False
             return
        if (p != None and q == None):
            res[0] = False
            return

        self._isSameTree(p.left, q.left, res)
        self._isSameTree(p.right, q.right, res)

        if p.val != q.val:
            res[0] = False
            return


if __name__ == "__main__":
    na1 = TreeNode(1)
    na2 = TreeNode(2)
    na3 = TreeNode(3)
    na1.left = na2; na1.right = na3

    nb1 = TreeNode(1)
    nb2 = TreeNode(2)
    nb3 = TreeNode(3)
    nb1.left = nb2; nb1.right = nb3

    s = Solution()
    print(s.isSameTree(na1, nb1))
