# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        if not root:
            return 0
        self.dfs(root)
        return sum(self.res)
    def dfs(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        leftsum = self.dfs(root.left)
        rightsum = self.dfs(root.right)
        self.res.append(abs(leftsum - rightsum))
        return root.val + leftsum + rightsum

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2; n1.right = n3
    s = Solution()
    print(s.findTilt(n1))
