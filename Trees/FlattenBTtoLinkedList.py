# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None: return
        self._flatten(root)

    def _flatten(self, root):
        if root == None: return None
        l = self._flatten(root.left)
        r = self._flatten(root.right)

        if l == None and r == None:
            return root
        if l != None and r != None:
            temp = l
            while temp != None and temp.right != None:
                temp = temp.right
            temp.right = r
            root.right = l
            root.left = None
            return root
        if l == None and r != None:
            return root
        if l != None and r == None:
            root.right = l
            root.left = None
            return root

def PreOrder(root):
    if root == None: return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n6 = TreeNode(6)

    n1.left = n2; n1.right = n5
    n2.left = n3; n2.right = n4
    n5.right = n6

    s = Solution()
    s.flatten(n1)
    PreOrder(n1)
