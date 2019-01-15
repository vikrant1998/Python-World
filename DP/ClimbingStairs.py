class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cache = dict()
        return self._recurse(0, n)

    def _recurse(self, ind, n):
        if ind == n:
            return 1
        
        if ind > n:
            return 0

        if ind in self.cache:
            return self.cache[ind]
        
        oneStep = self._recurse(ind + 1, n)
        twoStep = self._recurse(ind + 2, n)
        self.cache[ind] = oneStep + twoStep
        return oneStep + twoStep

if __name__ == "__main__":
    n = 3
    s = Solution()
    print(s.climbStairs(n))