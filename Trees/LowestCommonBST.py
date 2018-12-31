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
        if not root or not p or not q: return None
        return self._lowestCommonAncestor(root, p, q)

    def _lowestCommonAncestor(self, root, p, q):
        if root == None: return None
        if p.val < root.val and q.val < root.val:
            return self._lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self._lowestCommonAncestor(root.right, p, q)
        else:
            return root

if __name__ == "__main__":
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n8 = TreeNode(8)
    n0 = TreeNode(0)
    n4 = TreeNode(4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n6.left = n2; n6.right = n8
    n2.left = n0; n2.right = n4
    n8.left = n7; n8.right = n9
    n4.left = n3; n4.right = n5

    s = Solution()
    res = s.lowestCommonAncestor(n6, n2, n4)
    print(res.val)
