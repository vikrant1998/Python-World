# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if root == None: return None

        if d == 1:
            tempNode = TreeNode(v)
            tempNode.left = root
            root = tempNode
            return root

        from collections import deque
        q = deque()
        q.append(root)
        level = 1
        check = 0
        while q:
            qSize = len(q)
            while qSize > 0:
                element = q.popleft()
                if element != None:
                    if level == d - 1:
                        if element.left != None:
                            tempNode = TreeNode(v)
                            tempNode.left = element.left
                            element.left = tempNode
                            q.append(element.left)
                        else:
                            element.left = TreeNode(v)
                            q.append(element.left)
                        if element.right != None:
                            tempNode = TreeNode(v)
                            tempNode.right = element.right
                            element.right = tempNode
                            q.append(element.right)
                        else:
                            element.right = TreeNode(v)
                            q.append(element.right)
                    else:
                        if element.left != None:
                            q.append(element.left)
                        if element.right != None:
                            q.append(element.right)
                qSize -= 1
            level += 1
        return root

def PreOrder(root):
    if root == None: return
    print(root.val)
    PreOrder(root.left)
    PreOrder(root.right)

if __name__ == "__main__":
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    n6 = TreeNode(6)
    n3 = TreeNode(3)
    n1 = TreeNode(1)
    n5 = TreeNode(5)

    n4.left = n2; n4.right = n6
    n2.left = n3; n2.right = n1
    n6.left = n5

    s = Solution()
    root = s.addOneRow(n4, 1, 2)
    PreOrder(root)
