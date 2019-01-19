# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []

        stack = []
        res = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                popVal = stack.pop()
                res.append(popVal.val)
                root = popVal.right

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
    s.inorderTraversal(n1)