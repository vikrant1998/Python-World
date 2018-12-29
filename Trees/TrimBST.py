# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None: return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        elif root.val > R:
            return self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root

def InOrder(root):
    if root == None: return
    InOrder(root.left)
    print(root.val)
    InOrder(root.right)

if __name__ == "__main__":
    n3 = TreeNode(3)
    n0 = TreeNode(0)
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    n1 = TreeNode(1)

    n3.left = n0; n3.right = n4
    n0.right = n2
    n2.left = n1

    s = Solution()
    newRoot = s.trimBST(n3, 1, 3)
    InOrder(newRoot)
