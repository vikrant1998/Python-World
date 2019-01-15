class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        self.cache = dict()
        return min(self._recurse(cost, 0), self._recurse(cost, 1))

    def _recurse(self, cost, ind):
        if ind >= len(cost):
            return 0

        if ind in self.cache:
            return self.cache[ind]

        sum1 = self._recurse(cost, ind + 1)
        sum2 = self._recurse(cost, ind + 2)

        self.cache[ind] = min(sum1 + cost[ind], sum2 + cost[ind])
        return self.cache[ind]

if __name__ == "__main__":
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost3 = [0, 1, 1, 0]
    cost4 = [0, 1, 2, 0]
    s = Solution()
    print(s.minCostClimbingStairs(cost1))