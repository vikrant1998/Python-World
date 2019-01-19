# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.res = ''
        self._serialize(root)
        if self.res != '':
            self.res = self.res[:-1]
        return self.res

    def _serialize(self, root):
        if root == None:
            self.res += '#' + ' '
            return

        self.res += str(root.val) + ' '

        self._serialize(root.left)
        self._serialize(root.right) 

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None

        inpList = data.split()
        root = None
        self.index = 0
        root = self._deserialize(root, inpList)
        return root

    def _deserialize(self, root, inpList):
        if self.index >= len(inpList) or inpList[self.index] == '#':
            self.index += 1
            return None

        root = TreeNode(inpList[self.index])
        self.index += 1
        root.left = self._deserialize(root.left, inpList)
        root.right = self._deserialize(root.right, inpList)
        return root

# Your Codec object will be instantiated and called as such:
codec = Codec()
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2; n1.right = n3
n2.left = n4; n3.right = n5
ser = codec.serialize(n1)
#codec.deserialize(ser)
root = codec.deserialize(ser)
ser1 = codec.serialize(root)