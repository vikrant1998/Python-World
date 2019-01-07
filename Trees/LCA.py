# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None: return None
        if p == None and q == None: return None
        if p == None: return q
        if q == None: return p

        return self._lowestCommonAncestor(root, p, q)

    def _lowestCommonAncestor(self, root, p, q):
        if root == None: return None

        l = self._lowestCommonAncestor(root.left, p, q)
        r = self._lowestCommonAncestor(root.right, p, q)

        if root == p or root == q: return root
        if l != None and r != None: return root
        if l == None and r != None: return r
        if l != None and r == None: return l
        if l == None and r == None: return None


if __name__ == "__main__":
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    n3.left = n5; n3.right = n1
    n5.left = n6; n5.right = n2
    n1.left = n0; n1.right = n8
    n2.left = n7; n2.right = n4

    s = Solution()
    res = s.lowestCommonAncestor(n3, n2, n1)
    print(res.val)
