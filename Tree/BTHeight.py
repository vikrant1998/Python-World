class TreeNode(object):
    def __init__(self, inp):
        self.val = inp
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # Insert node into tree.
    def InsertNode(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return

        self._InsertNode(self.root, val)

    def _InsertNode(self, root, val):
        if val < root.val:
            if root.left:
                self._InsertNode(root.left, val)
            else:
                root.left = TreeNode(val)
        elif val > root.val:
            if root.right:
                self._InsertNode(root.right, val)
            else:
                root.right = TreeNode(val)
        return

class Solution(object):
    def maxDepth(self, root):
        return self.FindDepth(root)

    def FindDepth(self, root):
        if root == None: return 0
        lh = self.FindDepth(root.left)
        rh = self.FindDepth(root.right)
        mh = max(lh, rh) + 1
        return mh

if __name__ == "__main__":
    b = BinarySearchTree()

    b.InsertNode(5)
    b.InsertNode(3)
    b.InsertNode(7)
    b.InsertNode(6)
    b.InsertNode(8)
    b.InsertNode(2)
    b.InsertNode(4)
    b.InsertNode(12)

    s = Solution()
    print(s.maxDepth(b.root))
