# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if root == None: return []

        self.parentMap = dict()
        self._SetParent(root)
        self.targetFound = None
        self._Findtarget(root, target)
        if self.targetFound == None: return []

        self.nearList = []
        self.lrcount = 0

        self._FindNodes(self.targetFound, K)

        upVal = self.parentMap[self.targetFound]
        if upVal == None: return self.nearList
        prevVal = self.targetFound
        if upVal.left == prevVal:
            count = 1
            while upVal != None:
                if count == K:
                    self.nearList.append(upVal.val)
                    break

                if upVal.right == prevVal:
                    self._FindNodes(upVal.left, K - count - 1)
                else:
                    self._FindNodes(upVal.right, K - count - 1)
                prevVal = upVal
                upVal = self.parentMap[upVal]
                count += 1
        else:
            count = 1
            while upVal != None:
                if count == K:
                    self.nearList.append(upVal.val)
                    break
                if upVal.right == prevVal:
                    self._FindNodes(upVal.left, K - count - 1)
                else:
                    self._FindNodes(upVal.right, K - count - 1)
                prevVal = upVal
                upVal = self.parentMap[upVal]
                count += 1

        return self.nearList

    def _FindNodes(self, root, K):
        if root == None: return
        if self.lrcount == K:
            self.nearList.append(root.val)
        self.lrcount += 1
        self._FindNodes(root.left, K)
        self._FindNodes(root.right, K)
        self.lrcount -= 1

    def _Findtarget(self, root, target):
        if root == None or self.targetFound != None: return
        if root == target:
            self.targetFound = root
            return
        self._Findtarget(root.left, target)
        self._Findtarget(root.right, target)


    def _SetParent(self, root):
        from collections import deque
        q = deque()
        q.append(root)
        self.parentMap[root] = None
        while q:
            qSize = len(q)
            while qSize > 0:
                element = q.popleft()
                if element.left != None:
                    q.append(element.left)
                    self.parentMap[element.left] = element
                if element.right != None:
                    q.append(element.right)
                    self.parentMap[element.right] = element
                qSize -= 1

if __name__ == "__main__":
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    n3.left = n5; n3.right = n1
    n5.left = n6; n5.right = n2
    n1.left = n0; n1.right = n8
    n2.left = n7; n2.right = n4

    s = Solution()
    print(s.distanceK(n3, n2, 4))
