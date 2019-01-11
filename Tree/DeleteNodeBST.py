# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key == root.val:
            # Found the value to delete.
            # Leaf Node.
            if root.left == None and root.right == None:
                del(root)
                return None

            if root.left == None:
                temp = root.right
                del(root)
                return temp

            if root.right == None:
                temp = root.left
                del(root)
                return temp

            tempNode = root.right
            while tempNode.left != None:
                tempNode = tempNode.left

            root.val, tempNode.val = tempNode.val, root.val
            root.right = self.deleteNode(root.right, key)
        return root

def InOrder(root):
    if root == None: return
    print(root.val)
    InOrder(root.left)
    InOrder(root.right)

if __name__ == "__main__":
    n5 = TreeNode(5)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n4 = TreeNode(4)
    n7 = TreeNode(7)

    n5.left = n3; n5.right = n6
    n3.left = n2; n3.right = n4
    n6.right = n7

    s = Solution()
    root = s.deleteNode(n5, 7)
    InOrder(root)
