# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        self.res = False
        self.currSum = 0
        self._hasPathSum(root, sum)
        return self.res

    def _hasPathSum(self, root, sum):
        if root == None or self.res == True: return
        self.currSum += root.val
        if root.left == None and root.right == None:
            if self.currSum == sum:
                self.res = True
                return
        self._hasPathSum(root.left, sum)
        self._hasPathSum(root.right, sum)
        self.currSum -= root.val

if __name__ == "__main__":
    n5 = TreeNode(5)
    n4a = TreeNode(4)
    n8 = TreeNode(8)
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    n4b = TreeNode(4)
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n1 = TreeNode(1)

    n5.left = n4a; n5.right = n8
    n4a.left = n11; n8.left = n13;
    n8.right = n4b; n11.left = n7
    n11.right = n2; n4b.right = n1

    s = Solution()
    print(s.hasPathSum(n5, 29))
