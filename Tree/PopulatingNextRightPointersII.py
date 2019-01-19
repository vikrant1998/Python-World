# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return

        from collections import deque
        q = deque()
        root.next = None
        q.append(root)

        while q:
            qSize = len(q)
            while qSize > 0:
                element = q.popleft()
                if element.left != None:
                    q.append(element.left)
                if element.right != None:
                    q.append(element.right)
                qSize -= 1

            for i in range(len(q)):
                if i + 1 < len(q):
                    q[i].next = q[i+1]
                else:
                    q[i].next = None

if __name__ == "__main__":
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n7 = TreeLinkNode(7)

    n1.left = n2; n1.right = n3
    n2.left = n4; n2.right = n5
    n3.right = n7

    s = Solution()
    s.connect(n1)