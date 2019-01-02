# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        return self._minDepth(root)

    def _minDepth(self, root):
        if root == None: return 0
        ld = self._minDepth(root.left)
        rd = self._minDepth(root.right)
        minVal = 0
        if ld == 0:
            minVal = rd + 1
        elif rd == 0:
            minVal = ld + 1
        else:
            minVal = min(ld, rd) + 1
        return minVal

if __name__ == "__main__":
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9; n3.right = n20
    n20.left = n15; n20.right = n7

    s = Solution()
    print(s.minDepth(n3))
