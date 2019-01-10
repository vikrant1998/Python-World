# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        elements = []
        self._postorder(root, elements)
        return elements

    def _postorder(self, root, elements):
        if root == None: return

        if root.children:
            for element in root.children:
                self._postorder(element, elements)

        elements.append(root.val)

if __name__ == "__main__":
    s = Solution()

    f2 = Node(2, None)
    f4 = Node(4, None)
    f5 = Node(5, None)
    f6 = Node(6, None)
    f3 = Node(3, [f5, f6])
    f1 = Node(1, [f3, f2, f4])

    print(s.postorder(f1))
