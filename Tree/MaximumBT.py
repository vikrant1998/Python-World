# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or nums == []: return None
        root = None
        root = self._constructMaximumBinaryTree(root, nums)
        return root

    def _findMax(self, inpArr):
        ind = -1
        num = -1
        max = float("-inf")
        for i, element in enumerate(inpArr):
            if element > max:
                max = element
                ind = i

        return ind, max

    def _constructMaximumBinaryTree(self, root, nums):
        if len(nums) == 0: return
        idx, maxNum = self._findMax(nums)
        root = TreeNode(maxNum)
        root.left = self._constructMaximumBinaryTree(root.left, nums[0:idx])
        root.right = self._constructMaximumBinaryTree(root.right, nums[idx+1:])
        return root

def PreOrder(root):
    if root == None: return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

if __name__ == "__main__":
    arr = [3, 2, 1, 6, 0, 5]
    s = Solution()
    root = s.constructMaximumBinaryTree(arr)
    PreOrder(root)
