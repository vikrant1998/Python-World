class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = dict()
        self.inDegreeSet = set()
        self._BuildGraph(numCourses, prerequisites)
        newSet = self._InDegreeCheck()

        toposortList = []

        import heapq
        q = []

        for key, value in self.graph.items():
            if key not in newSet:
                heapq.heappush(q, key)

        while q:
            element = q.pop()
            toposortList.append(element)

            # Neighbors.
            for neighbor in self.graph[element]:
                import copy
                currSet = copy.deepcopy(self.graph[element])
                currSet.remove(neighbor)
                self.graph[element] = currSet

                retSet = self._InDegreeCheck()
                if neighbor not in retSet:
                    heapq.heappush(q, neighbor)

        for key, value in self.graph.items():
            if len(value) > 0:
                return False

        return True

    def _BuildGraph(self, numCourses, prerequisites):
        for i in range(0, numCourses):
            self.graph[i] = set()

        for connections in prerequisites:
            self.graph[connections[1]].add(connections[0])

    def _InDegreeCheck(self):
        newSet = set()
        for key, value in self.graph.items():
            for element in value:
                newSet.add(element)
        return newSet

if __name__ == "__main__":
    s = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(s.canFinish(numCourses, prerequisites))
        
