# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        allPaths = []
        sublist = []
        self._binaryTreePaths(root, sublist, allPaths)
        strList = []

        for element in allPaths:
            newStr = ''
            for nums in element:
                newStr += str(nums) + '->'
            if newStr != '':
                newStr = newStr[:-2]
            strList.append(newStr)

        return strList

    def _binaryTreePaths(self, root, sublist, allPaths):
        if root == None: return
        sublist.append(root.val)
        self._binaryTreePaths(root.left, sublist, allPaths)
        self._binaryTreePaths(root.right, sublist, allPaths)
        if not root.left and not root.right:
            import copy
            newList = copy.deepcopy(sublist)
            allPaths.append(newList)
        sublist.pop()

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)

    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.left = n6; n3.right = n7
    n4.left = n8

    s = Solution()
    print(s.binaryTreePaths(n1))
