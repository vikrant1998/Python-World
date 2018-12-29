# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root == None: return False

        res = [False]
        visited = set()
        self._findTarget(root, k, visited, res)
        return res[0]

    def _findTarget(self, root, k, visited, res):
        if root == None or res[0] == True: return
        if k - root.val in visited:
            res[0] = True
            return
        visited.add(root.val)
        self._findTarget(root.left, k, visited, res)
        self._findTarget(root.right, k, visited, res)

if __name__ == "__main__":
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n7 = TreeNode(7)

    n5.left = n3; n5.right = n6
    n3.left = n2; n3.right = n4
    n6.right = n7

    s = Solution()
    res = s.findTarget(n5, 9)
    print(res)
