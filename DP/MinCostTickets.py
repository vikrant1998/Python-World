class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        self.days = days
        self.costs = costs
        self._recurse(0)

    def _recurse(ind):
        if ind >= len(days): return 0
        
        while()
        
        for i in range(0, 3):
            self._recurse(ind)



if __name__ == "__main__":
    days = [1,4,6,7,8,20], costs = [2,7,15]
    s = Solution()
    s.mincostTickets(days, costs)