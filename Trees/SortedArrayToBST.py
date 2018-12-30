# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            n1 = TreeNode(nums[0])
            n2 = TreeNode(nums[1])
            n1.right = n2
            return n1
        else:
            mid = len(nums) / 2
            n1 = TreeNode(nums[mid])
            n1.left = self.sortedArrayToBST(nums[:mid])
            n1.right = self.sortedArrayToBST(nums[mid+1:])
            return n1

def InOrder(root):
    if root == None: return
    InOrder(root.left)
    print(root.val)
    InOrder(root.right)

if __name__ == "__main__":
    s = Solution()
    nums = [-10,-3,0,5,9]
    root = s.sortedArrayToBST(nums)
    InOrder(root)
