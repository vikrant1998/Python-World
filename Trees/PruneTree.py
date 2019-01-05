# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        val, root = self._pruneTree(root)
        return root

    def _pruneTree(self, root):
        if root == None:
            return (True, root)

        l, root.left = self._pruneTree(root.left)
        r, root.right = self._pruneTree(root.right)

        if l and root != None:
            del(root.left)
            root.left = None
        if r and root != None:
            del(root.right)
            root.right = None

        # One side is wrong.
        if not l or not r or root.val == 1:
            return False, root
        else:
            return True, root

def PreOrder(root):
    if root == None: return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

if __name__ == "__main__":
    a1a = TreeNode(1)
    a0a = TreeNode(0)
    a0b = TreeNode(0)
    a1b = TreeNode(1)

    a1a.right = a0a
    a0a.left = a0b; a0a.right = a1b

    s = Solution()
    root = s.pruneTree(a1a)
    PreOrder(root)
