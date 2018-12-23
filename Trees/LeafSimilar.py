# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        listOne, listTwo = [], []
        self._PostOrder(root1, listOne)
        self._PostOrder(root2, listTwo)
        if listOne == listTwo: return True
        return False

    def _PostOrder(self, root, newList):
        if root == None: return
        self._PostOrder(root.left, newList)
        self._PostOrder(root.right, newList)
        if root.left == None and root.right == None: newList.append(root.val)

if __name__ == "__main__":
    an3 = TreeNode(3)
    an5 = TreeNode(5)
    an1 = TreeNode(1)
    an6 = TreeNode(6)
    an2 = TreeNode(2)
    an9 = TreeNode(9)
    an8 = TreeNode(8)
    an7 = TreeNode(7)
    an4 = TreeNode(4)

    an3.left = an5; an3.right = an1
    an5.left = an6; an5.right = an2
    an1.left = an9; an1.right = an8
    an2.left = an7; an2.right = an4

    root1 = an3

    bn3 = TreeNode(3)
    bn5 = TreeNode(5)
    bn1 = TreeNode(1)
    bn6 = TreeNode(6)
    bn2 = TreeNode(2)
    bn9 = TreeNode(9)
    bn8 = TreeNode(8)
    bn7 = TreeNode(7)
    bn4 = TreeNode(4)

    bn3.left = bn5; bn3.right = bn1
    bn5.left = bn6; bn5.right = bn2
    bn1.left = bn9; bn1.right = bn8
    bn2.left = bn7; bn2.right = bn4

    root2 = bn3

    s = Solution()
    print(s.leafSimilar(root1, root2))
