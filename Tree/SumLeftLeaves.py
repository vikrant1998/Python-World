# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = [0]
        self._sumOfLeftLeaves(root, sum)
        return sum[0]

    def _sumOfLeftLeaves(self, root, sum):
        if root == None: return
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                sum[0] += root.left.val
        self._sumOfLeftLeaves(root.left, sum)
        self._sumOfLeftLeaves(root.right, sum)

if __name__ == "__main__":
    n3 = TreeNode(3)
    n9 = TreeNode(9)
    n20 = TreeNode(20)
    n15 = TreeNode(15)
    n7 = TreeNode(7)

    n3.left = n9; n3.right = n20
    n20.left = n15; n20.right = n7

    s = Solution()
    print(s.sumOfLeftLeaves(n3))
