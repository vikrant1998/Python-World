# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None: return 0
        numPaths = [0]
        allPaths = []
        self._pathSum(root, numPaths, allPaths, sum)
        return numPaths[0]

    def _pathSum(self, root, numPaths, allPaths, target):
        if root == None: return
        sublist = []
        sum = [0]
        self._DFS(root, numPaths, sublist, allPaths, sum, target)
        self._pathSum(root.left, numPaths, allPaths, target)
        self._pathSum(root.right, numPaths, allPaths, target)

    def _DFS(self, root, numPaths, sublist, allPaths, sum, target):
        if root == None: return
        sum[0] += root.val
        sublist.append(root.val)
        if sum[0] == target:
            numPaths[0] += 1
            import copy
            #temp = copy.deepcopy(sublist)
            allPaths.append(temp)

        self._DFS(root.left, numPaths, sublist, allPaths, sum, target)
        self._DFS(root.right, numPaths, sublist, allPaths, sum, target)
        sum[0] -= root.val
        sublist.pop()

# Optimized.
'''
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}

        # recursive to get result
        self.dfs(root, target, 0, cache)

        # return result
        return self.result

    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1
'''

if __name__ == "__main__":
    n10 = TreeNode(10)
    n5 = TreeNode(5)
    n_3 = TreeNode(-3)
    n3a = TreeNode(3)
    n2 = TreeNode(2)
    n11 = TreeNode(11)
    n3b = TreeNode(3)
    n_2 = TreeNode(-2)
    n1 = TreeNode(1)

    n10.left = n5; n10.right = n_3
    n5.left = n3a; n5.right = n2
    n3a.left = n3b; n3a.right = n_2
    n2.right = n1
    n_3.right = n11

    s = Solution()
    print(s.pathSum(n10, 8))
