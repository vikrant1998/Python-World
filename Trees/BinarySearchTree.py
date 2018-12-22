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
        return

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

    def InOrder(self):
        self._InOrder(self.root)

    def _InOrder(self, root):
        if root == None: return

        self._InOrder(root.left)
        print(root.val)
        self._InOrder(root.right)

    def DeleteNode(self, val):
        self._DeleteNode(self.root, val)

    def _DeleteNode(self, root, val):
        if root == None: return root

        if val < root.val:
            root.left = self._DeleteNode(root.left, val)
        elif val > root.val:
            root.right = self._DeleteNode(root.right, val)
        elif val == root.val:
            # No children.
            if root.left == None and root.right == None:
                del(root)
                return None

            # One child.
            if root.left == None:
                temp = root.right
                del(root)
                return temp

            if root.right == None:
                temp = root.left
                del(root)
                return temp

            # Two children.
            successor = root.right
            while successor.left != None:
                successor = successor.left

            root.val, successor.val = successor.val, root.val
            root.right = self._DeleteNode(root.right, val)
        return root

    def DestroyTree(self):
        self._DestroyTree(self.root)

    def _DestroyTree(self, root):
        if root == None: return
        self._DestroyTree(root.left)
        self._DestroyTree(root.right)
        del(root)

if __name__ == "__main__":
    b = BinarySearchTree()

    b.InsertNode(5)
    b.InsertNode(3)
    b.InsertNode(7)
    b.InsertNode(6)
    b.InsertNode(8)
    b.InsertNode(2)
    b.InsertNode(4)

    b.InOrder()
    b.DeleteNode(2)
    b.DeleteNode(5)
    print('')
    b.InOrder()
    print('')

    b.DestroyTree()

    b.InsertNode(5)
    b.InsertNode(3)
    b.InsertNode(7)
    b.InsertNode(6)
    b.InsertNode(8)
    b.InsertNode(2)
    b.InsertNode(4)

    b.InOrder()
