# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        location = []
        self._searchBST(root, val, location)
        if location == []: return None
        return location[0]

    def _searchBST(self, root, val, location):
        if root == None: return

        if val < root.val:
            self._searchBST(root.left, val, location)
        elif val > root.val:
            self._searchBST(root.right, val, location)
        elif val == root.val:
            location.append(root)


if __name__ == "__main__":
    f4 = TreeNode(4)
    f2 = TreeNode(2)
    f7 = TreeNode(7)
    f1 = TreeNode(1)
    f3 = TreeNode(3)

    f4.left = f2
    f4.right = f7

    f2.left = f1
    f2.right = f3

    s = Solution()
    res = s.searchBST(f4, 2)
