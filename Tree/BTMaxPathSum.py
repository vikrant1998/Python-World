# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.sumDict = dict()
        self._maxPathSum(root)
        maxVal = float("-inf")
        for key, value in self.sumDict.items():
            if value[0] > maxVal: maxVal = value[0]
            if value[1] > maxVal: maxVal = value[1]

        return maxVal

    def _maxPathSum(self, root):
        if root == None: return 0
        l = self._maxPathSum(root.left)
        r = self._maxPathSum(root.right)

        if l > 0 or r > 0:
            self.sumDict[root] = [max(l, r) + root.val, l + r + root.val]
            return max(l, r) + root.val
        else:
            self.sumDict[root] = [root.val, l + r + root.val]
            return root.val

if __name__ == "__main__":
    '''
    n_10 = TreeNode(-10)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n_10.left = n9; n_10.right = n20
    n20.left = n15; n20.right = n7
    '''
    n2 = TreeNode(2)
    n_1 = TreeNode(-1)
    n_2 = TreeNode(-2)

    n2.left = n_1; n2.right = n_2

    s = Solution()
    print(s.maxPathSum(n2))
        