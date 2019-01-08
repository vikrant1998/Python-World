class DisjointNode(object):
    def __init__(self, inp):
        self.val = inp
        self.rank = 0
        self.parent = inp

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.nodeMap = dict()
        self.redundantSet = set()

        self._MakeNodes(edges)

        for edge in edges:
            self._Union(edge[0], edge[1])

        for edge in edges:
            if (edge[0], edge[1]) in self.redundantSet:
                return edge

        return []

    def _MakeNodes(self, edges):
        for edge in edges:
            el1, el2 = edge[0], edge[1]
            if el1 not in self.nodeMap: self.nodeMap[el1] = DisjointNode(el1)
            if el2 not in self.nodeMap: self.nodeMap[el2] = DisjointNode(el2)

    def _findParent(self, u):
        temp = self.nodeMap[u].parent
        if u == temp:
            return u
        self.nodeMap[u].parent = self._findParent(self.nodeMap[u].parent)
        return self.nodeMap[u].parent

    def _Union(self, u, v):
        p_u = self._findParent(u)
        p_v = self._findParent(v)

        if p_u == p_v:
            self.redundantSet.add((u, v))
            return

        if self.nodeMap[p_u].rank > self.nodeMap[p_v].rank:
            self.nodeMap[p_v].parent = self.nodeMap[p_u].val
        elif self.nodeMap[p_u].rank == self.nodeMap[p_v].rank:
            self.nodeMap[p_v].parent = self.nodeMap[p_u].val
            self.nodeMap[p_u].rank += 1
        else:
            self.nodeMap[p_u].parent = self.nodeMap[p_v].val

if __name__ == "__main__":
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    s = Solution()
    print(s.findRedundantConnection(edges))
