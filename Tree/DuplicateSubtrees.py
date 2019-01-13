# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root == None: return []
        self.serializeStringMap = dict()
        self._findDuplicateSubtrees(root)

        treeList = []
        for key, value in self.serializeStringMap.items():
            if len(value) > 1:
                treeList.append(value[0])

        return treeList

    def _findDuplicateSubtrees(self, root):
        if root == None: return
        self._findDuplicateSubtrees(root.left)
        self._findDuplicateSubtrees(root.right)
        self.serializeString = ''
        self._serialize(root)
        if self.serializeString not in self.serializeStringMap:
            self.serializeStringMap[self.serializeString] = list()
            self.serializeStringMap[self.serializeString].append(root)
        else:
            self.serializeStringMap[self.serializeString].append(root)

    def _serialize(self, root):
        if root == None:
            self.serializeString += '#'
            return

        self.serializeString += str(root.val)
        self._serialize(root.left)
        self._serialize(root.right)

def PreOrder(root):
    if root == None: return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2a = TreeNode(2)
    n3 = TreeNode(3)
    n4a = TreeNode(4)
    n2b = TreeNode(2)
    n4b = TreeNode(4)
    n4c = TreeNode(4)

    n1.left = n2a; n1.right = n3
    n2a.left = n4a
    n3.left = n2b; n3.right = n4b
    n2b.left = n4c

    s = Solution()
    treeList = s.findDuplicateSubtrees(n1)
    for root in treeList:
        PreOrder(root)