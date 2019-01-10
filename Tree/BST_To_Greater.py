# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

""" Reverse in-order """
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        total = [0]
        self._convertBST(root, total)
        return root

    def _convertBST(self, root, total):
        if root == None: return
        self._convertBST(root.right, total)
        total[0] += root.val
        root.val = total[0]
        self._convertBST(root.left, total)

def InOrder(root):
    if root == None: return
    InOrder(root.left)
    print(root.val)
    InOrder(root.right)

if __name__ == "__main__":
    n5 = TreeNode(5)
    n2 = TreeNode(2)
    n13 = TreeNode(13)
    n5.left = n2; n5.right = n13
    s = Solution()
    s.convertBST(n5)
    InOrder(n5)
