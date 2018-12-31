# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        sym = [True]
        self._isSymmetric(root, root, sym)
        return sym[0]

    def _isSymmetric(self, root1, root2, sym):
        if not sym[0]: return
        if not root1 and not root2: return
        if not root1 and root2:
            sym[0] = False
            return
        if root1 and not root2:
            sym[0] = False
            return

        self._isSymmetric(root1.left, root2.right, sym)
        self._isSymmetric(root1.right, root2.left, sym)
        if root1.val != root2.val:
            sym[0] = False
            return

if __name__ == "__main__":
    n1  = TreeNode(1)
    n2a = TreeNode(2)
    n2b = TreeNode(2)
    n3a = TreeNode(3)
    n4a = TreeNode(4)
    n4b = TreeNode(3)
    n3b = TreeNode(3)

    n1.left = n2a; n1.right = n2b
    n2a.left = n3a; n2a.right = n4a
    n2b.left = n4b; n2b.right = n3b

    s = Solution()
    print(s.isSymmetric(n1))
