# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import deque
        stack = deque()
        res = []

        while stack or root:
            if root:
                res.insert(0, root.val)
                stack.append(root)
                root = root.right
            else:
                popVal = stack.pop()
                root = popVal.left

        return res

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
    n2.left = n7; n7.right = n8
    n3.left = n4; n3.right = n5
    n5.left = n6

    s = Solution()
    print(s.postorderTraversal(n1))