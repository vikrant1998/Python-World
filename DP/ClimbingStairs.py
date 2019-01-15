class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        self._recurse(0, n)
        print(self.count)

    def _recurse(ind, n):
        if ind == n:
            self.count += 1
            return

        self.count += 1
        self._recurse(ind + 1, n)
        self._recurse(ind + 2, n)

if __name__ == "__main__":
    n = 5
    s = Solution()
    print(s.climbStairs(n))