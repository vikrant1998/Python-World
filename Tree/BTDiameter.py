# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        diameter = [0]
        self._diameterOfBinaryTree(root, diameter)
        return diameter[0] - 1

    def _diameterOfBinaryTree(self, root, diameter):
        if root == None: return 0
        lh = self._diameterOfBinaryTree(root.left, diameter)
        rh = self._diameterOfBinaryTree(root.right, diameter)
        diameter[0] = max(diameter[0], lh + rh + 1)
        return max(lh, rh) + 1

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    s = Solution()
    print(s.diameterOfBinaryTree(n1))
