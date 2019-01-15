class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        if N == 0: return 0

        from collections import defaultdict
        self.graph = defaultdict(list)

        # Initialize graph.
        self.graph[1] = [6, 8]
        self.graph[2] = [7, 9]
        self.graph[3] = [4, 8]
        self.graph[4] = [3, 9, 0]
        self.graph[5] = []
        self.graph[6] = [1, 7, 0]
        self.graph[7] = [2, 6]
        self.graph[8] = [1, 3]
        self.graph[9] = [2, 4]
        self.graph[0] = [4, 6]

        self.cache = dict()
        self.traveled = 1
        self.local = 0
        yeet = 0
        for i in range(0, 10):
            self.traveled = 1
            yeet += self._recurse(i, N)


        return (yeet % ((10**9) + 7))

    def _recurse(self, start, N):
        if self.traveled == N:
            self.cache[(start, 0)] = 1
            return 1

        if (start, N - self.traveled) in self.cache:
            return self.cache[(start, N - self.traveled)]

        local = 0
        for neighbor in self.graph[start]:
            self.traveled += 1
            local += self._recurse(neighbor, N)
            self.traveled -= 1

        self.cache[(start, N - self.traveled)] = local
        return local

if __name__ == "__main__":
    s = Solution()
    print(s.knightDialer(2))