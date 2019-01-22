class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        self._BuildGraph(n, flights)
        self.distances = [float("inf") for i in range(n)]

        # Set the source.
        self.distances[src] = 0

        # Run Bellman Ford.
        # Needs to run Bellman Ford atleast v - 1 times.
        for i in range(k + 1):
            dn = list(self.distances)
            for source, neighbors in self.graph.items():
                for neighbor in neighbors:
                    if self.distances[source] + neighbor[1] < dn[neighbor[0]]:
                        dn[neighbor[0]] = self.distances[source] + neighbor[1]
            self.distances = dn

        if self.distances[dst] == float("inf"): return -1
        return self.distances[dst]

    """ Build the graph. """
    def _BuildGraph(self, n, flights):
        self.graph = dict()
        for i in range(n): self.graph[i] = []
        for point in flights: self.graph[point[0]].append((point[1], point[2]))

if __name__ == "__main__":
    n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0; dst = 2; k = 0
    s = Solution()
    print(s.findCheapestPrice(n, flights, src, dst, k))