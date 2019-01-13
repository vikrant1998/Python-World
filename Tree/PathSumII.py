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
        :rtype: List[List[int]]
        """
        if root == None: return []
        self.currPath = []
        self.allPaths = []
        self.currSum = 0
        self._pathSum(root, sum)
        return self.allPaths
        
    def _pathSum(self, root, sum):
        if root == None: return
        self.currPath.append(root.val)
        self.currSum += root.val

        if self.currSum == sum and root.left == None and root.right == None:
            import copy
            self.allPaths.append(copy.deepcopy(self.currPath))

        self._pathSum(root.left, sum)

        if root.left != None:
            self.currSum -= root.left.val
            self.currPath.pop()

        self._pathSum(root.right, sum)

        if root.right != None:
            self.currSum -= root.right.val
            self.currPath.pop()           

if __name__ == "__main__":
    n5a = TreeNode(5)
    n4a = TreeNode(4)
    n8 = TreeNode(8)
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    n4b = TreeNode(4)
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n5b = TreeNode(5)
    n1 = TreeNode(1)

    n5a.left = n4a
    n5a.right = n8
    n4a.left = n11
    n8.left = n13; n8.right = n4b
    n11.left = n7; n11.right = n2
    n4b.left = n5b; n4b.right = n1

    s = Solution()
    s.pathSum(n5a, 22)