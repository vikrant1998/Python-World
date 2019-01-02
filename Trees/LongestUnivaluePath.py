# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        self.maxCount = 0
        self.cache = dict()
        self._longestUnivaluePath(root)
        if self.maxCount == 0: return 0
        return self.maxCount - 1

    def _dfs(self, root, valCheck, mainRoot):
        if root == None: return 0

        if root in self.cache and root.val == valCheck:
            return self.cache[root] + 1
        elif root in self.cache or root.val != valCheck:
            return 0

        lCount = self._dfs(root.left, valCheck, mainRoot)
        rCount = self._dfs(root.right, valCheck, mainRoot)

        if root.val == valCheck:
            if root is mainRoot:
                self.cache[root] = lCount + rCount + 1
                return lCount + rCount + 1
            self.cache[root] = max(lCount, rCount) + 1
            return max(lCount, rCount) + 1
        else:
            self.cache[root] = 0
            return 0


    def _longestUnivaluePath(self, root):
        if root == None: return
        count = self._dfs(root, root.val, root)
        #print(count)
        if count > self.maxCount:
            self.maxCount = count

        self._longestUnivaluePath(root.left)
        self._longestUnivaluePath(root.right)

if __name__ == "__main__":
    '''
    n5a = TreeNode(5)
    n4 = TreeNode(4)
    n5b = TreeNode(5)
    n1a = TreeNode(1)
    n1b = TreeNode(1)
    n5c = TreeNode(5)

    n5a.left = n4; n5a.right = n5b
    n4.left = n1a; n4.right = n1b
    n5b.right = n5c
    '''
    n1 = TreeNode(1)
    n4a = TreeNode(4)
    n5a = TreeNode(5)
    n4b = TreeNode(4)
    n4c = TreeNode(4)
    n5b = TreeNode(5)

    n1.left = n4a; n1.right = n5a
    n4a.left = n4b; n4a.right = n4c
    n5a.right = n5b
    '''
    n1 = TreeNode(1)
    n2a, n2b, n2c = TreeNode(2), TreeNode(2), TreeNode(2)
    n3a, n3b = TreeNode(4), TreeNode(3)
    n4a, n4b = TreeNode(4), TreeNode(4)
    n5 = TreeNode(4)

    n1.left = n2a; n1.right = n3a
    n2a.left = n2b; n2a.right = n3b
    n2b.right = n2c
    n3a.right = n4a
    n4a.left = n5; n4a.right = n4b
    '''
    s = Solution()
    print(s.longestUnivaluePath(n1))
