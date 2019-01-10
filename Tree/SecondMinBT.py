# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minOne = [float("inf")]
        minTwo = [float("inf")]

        self._findSecondMin(root, minOne, minTwo)
        if minTwo[0] == float("inf"):
            return -1
        return minTwo[0]

    def _findSecondMin(self, root, minOne, minTwo):
        if root == None: return
        self._findSecondMin(root.left, minOne, minTwo)
        self._findSecondMin(root.right, minOne, minTwo)
        if root.val < minOne[0] and root.val < minTwo[0]:
            minTwo[0] = minOne[0]
            minOne[0] = root.val
        elif root.val < minTwo[0] and root.val > minOne[0]:
            minTwo[0] = root.val

if __name__ == "__main__":
    n2a = TreeNode(2)
    n2b = TreeNode(2)
    n5a = TreeNode(5)
    n5b = TreeNode(5)
    n7 = TreeNode(7)
    n2a.left = n2b; n2a.right = n5a;
    n5a.left = n5b; n5a.right = n7
    s = Solution()
    print(s.findSecondMinimumValue(n2a))

    n2c = TreeNode(2)
    n2d = TreeNode(2)
    n2e = TreeNode(2)
    n2c.left = n2d; n2c.right = n2e
    print(s.findSecondMinimumValue(n2c))
