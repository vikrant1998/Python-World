class TreeNode(object):
    def __init__(self, inp):
        self.val = inp
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        root = None
        root = self.PostOrder(t1, t2, root)
        return root

    def PostOrder(self, t1, t2, root):
        if t1 == None and t2 == None:
            return None

        if t1 == None:
            root = TreeNode(t2.val)
            root.left = self.PostOrder(t1, t2.left, root.left)
            root.right = self.PostOrder(t1, t2.right, root.right)
            return root

        if t2 == None:
            root = TreeNode(t1.val)
            root.left = self.PostOrder(t1.left, t2, root.left)
            root.right = self.PostOrder(t1.right, t2, root.right)
            return root

        root = TreeNode(t1.val + t2.val)
        root.left = self.PostOrder(t1.left, t2.left, root.left)
        root.right = self.PostOrder(t1.right, t2.right, root.right)
        return root


    def InOrder(self, root):
        if root == None: return
        self.InOrder(root.left)
        print(root.val)
        self.InOrder(root.right)


if __name__ == "__main__":
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)

    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.right.right = TreeNode(7)

    s = Solution()
    r = s.mergeTrees(root1, root2)
    s.InOrder(r)
