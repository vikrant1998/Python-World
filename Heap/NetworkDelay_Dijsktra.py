class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        # Initialize graph.
        graph = dict()
        for i in range(N): graph[i+1] = []
        for element in times:
            graph[element[0]].append([element[1], element[2]])

        distances = dict()
        for i in range(N): distances[i+1] = float("inf")
        distances[K] = 0

        import heapq
        q = []
        heapq.heappush(q, (0, K))

        while q:
            dist, node = heapq.heappop(q)
            for neighbor in graph[node]:
                if distances[neighbor[0]] > distances[node] + neighbor[1]:
                    distances[neighbor[0]] = distances[node] + neighbor[1]
                    heapq.heappush(q, (distances[neighbor[0]], neighbor[0]))

        maxVal = -float("inf")
        for key, value in distances.items():
            maxVal = max(maxVal, value)

        if maxVal == float("inf"):
            return -1
        return maxVal

if __name__ == "__main__":
    times = [[1, 4, 3], [1, 3, 3], [1, 2, 5], \
            [4, 2, 4], [3, 5, 4], [2, 5, 8]]

    K = 1
    N = 5
    s = Solution()
    print(s.networkDelayTime(times, N, K))
