""" Timeout DFS """
"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        self.graph = dict()
        self._BuildGraph(edges)
        self.visited = set()
        minHeight = float("inf")
        heightDict = dict()

        for key, value in self.graph.items():
            self.visited.add(key)
            h = self._Recurse(key)

            if h not in heightDict: heightDict[h] = []
            heightDict[h].append(key)

            minHeight = min(minHeight, h)
            self.visited.clear()

        if minHeight == float("inf"): return [0]
        return heightDict[minHeight]

    def _Recurse(self, src):
        height = 0
        
        for neighbor in self.graph[src]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                height = max(height, self._Recurse(neighbor))

        return height + 1

    def _BuildGraph(self, edges):
        for edge in edges[::-1]:
            if edge[0] not in self.graph: self.graph[edge[0]] = []
            if edge[1] not in self.graph: self.graph[edge[1]] = []
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
"""

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        #:type n: int
        #:type edges: List[List[int]]
        #:rtype: List[int]
        """
        self.graph = dict()
        self._BuildGraph(edges)

        newSet = set()
        for i in range(n): newSet.add(i)
        
        while len(newSet) > 2:
            remSet = set()
            for val in newSet:
                if len(self.graph[val]) == 1:
                    remSet.add(val)

            newSet -= remSet
            for element in remSet:
                for neighbor in self.graph[element]:
                    if element in self.graph[neighbor]:
                        self.graph[neighbor].remove(element)

        return list(newSet)

    def _BuildGraph(self, edges):
        for edge in edges[::-1]:
            if edge[0] not in self.graph: self.graph[edge[0]] = []
            if edge[1] not in self.graph: self.graph[edge[1]] = []
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])       

if __name__ == "__main__":
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    s = Solution()
    print(s.findMinHeightTrees(n, edges))