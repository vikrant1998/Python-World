# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []
        self.mapSum = dict()
        self._findFrequentTreeSum(root)
        maxVal = float("-inf")
        freqSum = float("-inf")
        
        print(self.mapSum)

        rList = []
        for key, value in self.mapSum.items():
            if value > maxVal:
                maxVal = value
                freqSum = key

        for key, value in self.mapSum.items():
            if value == maxVal:
                rList.append(key)
        
        return rList

    def _findFrequentTreeSum(self, root):
        if root == None: return 0
        lSum = self._findFrequentTreeSum(root.left)
        rSum = self._findFrequentTreeSum(root.right)
        currSum = lSum + rSum + root.val
        if currSum in self.mapSum:
            self.mapSum[currSum] += 1
        else:
            self.mapSum[currSum] = 1
        return currSum

if __name__ == "__main__":
    n5 = TreeNode(5)
    n2 = TreeNode(2)
    n_3 = TreeNode(-3)

    n5.left = n2; n5.right = n_3
    s = Solution()
    print(s.findFrequentTreeSum(n5))
        