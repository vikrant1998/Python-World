# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.completeCheck = True
        if root == None: return self.completeCheck
        self._isCompleteTree(root)
        return self.completeCheck

    def _isCompleteTree(self, root):
        from collections import deque
        q = deque()
        q.append(root)

        height = self._findHeight(root)
        count = 0

        if height == 1 and root.left == None and root.right == None:
            return

        while q:
            qSize = len(q)
            count += 1
            subList = []
            while qSize > 0:
                element = q.popleft()
                if count != height - 1:
                    if element.left != None:
                        q.append(element.left)
                        subList.append(element.left.val)
                    if element.right != None:
                        q.append(element.right)
                        subList.append(element.right.val)
                else:
                    if element.left != None:
                        q.append(element.left)
                        subList.append(element.left.val)
                    else:
                        subList.append(None)
                    if element.right != None:
                        q.append(element.right)
                        subList.append(element.right.val)
                    else:
                        subList.append(None)    
                qSize -= 1

            #print(subList, count)

            if count != height - 1 and len(subList) != 2**count and subList != []:
                self.completeCheck = False
                return
            elif count == height - 1 and len(subList) == 0:
                return
            elif count == height - 1:
                while subList[-1] == None:
                    subList.pop()
                if None in subList:
                    self.completeCheck = False
                    return

    def _findHeight(self, root):
        if root == None: return 0
        l = self._findHeight(root.left)
        r = self._findHeight(root.right)
        return max(l, r) + 1

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6

    s = Solution()
    print(s.isCompleteTree(n1))