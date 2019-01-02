# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.currMax = 0
        self.totalMax = -float("inf")
        self.prevValue = -float("inf")
        if root == None: return self.res
        self._findMode(root)
        return self.res

    def _findMode(self, root):
        if root == None: return
        self._findMode(root.left)
        if self.prevValue == root.val:
            self.currMax += 1
        else:
            self.currMax = 1
        if self.currMax > self.totalMax:
            del self.res[:]
            self.totalMax = self.currMax
            self.res.append(root.val)
        elif self.currMax == self.totalMax:
            self.res.append(root.val)

        self.prevValue = root.val
        self._findMode(root.right)

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2_a = TreeNode(2)
    n2_b = TreeNode(2)
    n1.right = n2_a
    n2_a.left = n2_b
    s = Solution()
    res = s.findMode(n1)
    print(res)
