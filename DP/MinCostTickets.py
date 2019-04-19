class Solution(object):
    def mincostTickets(self, days1, costs1):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        self.days = days1
        self.costs = costs1
        index, cost, valid = 0, 0, 0
        self.cache = dict()
        return self._recurse(index, cost, valid)

    def _recurse(self, index, cost, valid):
        if index >= len(self.days): return 0
        
        if valid >= self.days[index]:
            return self._recurse(index + 1, cost, valid)

        if index in self.cache: return self.cache[index]
            
        cost1 = self.costs[0] + self._recurse(index + 1, cost, self.days[index])
        cost2 = self.costs[1] + self._recurse(index + 1, cost, self.days[index] + 6)
        cost3 = self.costs[2] + self._recurse(index + 1, cost, self.days[index] + 29)
        self.cache[index] = min(cost1, cost2, cost3)
        return self.cache[index]

if __name__ == "__main__":
    days = [1,4,6,7,8,20]
    costs = [2,7,15]
    s = Solution()
    print(s.mincostTickets(days, costs))