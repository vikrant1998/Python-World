# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.pathStr = ''
        self.currSum = 0
        self._sumNumbers(root)
        return self.currSum

    def _sumNumbers(self, root):
        if root == None: return

        self.pathStr += str(root.val)

        if root.left == None and root.right == None:
            self.currSum += int(self.pathStr)

        self._sumNumbers(root.left)

        if root.left != None:
            self.pathStr = self.pathStr[:-1]

        self._sumNumbers(root.right) 

        if root.right != None:
            self.pathStr = self.pathStr[:-1]

if __name__ == "__main__":
    n4 = TreeNode(4)
    n9 = TreeNode(9)
    n0 = TreeNode(0)
    n5 = TreeNode(5)
    n1 = TreeNode(1)

    n4.left = n9; n4.right = n0
    n9.left = n5; n9.right = n1

    s = Solution()
    print(s.sumNumbers(n4))
        