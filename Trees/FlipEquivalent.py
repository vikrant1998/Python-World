# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        res = self._flipEquiv(root1, root2)
        return res

    def _flipEquiv(self, root1, root2):
        if root1 == None and root2 == None: return True
        if root1 == None or root2 == None: return False
        if root1.val != root2.val: return False

        res1 = self._flipEquiv(root1.left, root2.right)
        res1 &= self._flipEquiv(root1.right, root2.left)

        res2 = self._flipEquiv(root1.left, root2.left)
        res2 &= self._flipEquiv(root1.right, root2.right)

        return res1 or res2

if __name__ == "__main__":
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a6 = TreeNode(6)
    a7 = TreeNode(7)
    a8 = TreeNode(8)

    a1.left = a2; a1.right = a3
    a2.left = a4; a2.right = a5
    a3.left = a6
    a5.left = a7; a5.right = a8

    b1 = TreeNode(1)
    b2 = TreeNode(2)
    b3 = TreeNode(3)
    b4 = TreeNode(4)
    b5 = TreeNode(5)
    b6 = TreeNode(6)
    b7 = TreeNode(7)
    b8 = TreeNode(8)

    b1.left = b3; b1.right = b2
    b3.right = b6
    b2.left = b4; b2.right = b5
    b5.left = b8; b5.right = b7

    s = Solution()
    print(s.flipEquiv(a1, b1))
