# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        return self._maxDepth(root)

    def _maxDepth(self, root):
        if root == None or root.children == None: return 0

        mh = 0
        for element in root.children:
            mh = max(self._maxDepth(element), mh)
        return mh + 1


if __name__ == "__main__":
    s = Solution()

    f2 = Node(2, None)
    f4 = Node(4, None)
    f5 = Node(5, None)
    f6 = Node(6, None)
    f3 = Node(3, [f5, f6])
    f1 = Node(1, [f3, f2, f4])

    print(s.maxDepth(f1))
