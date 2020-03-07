class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """

        ''' dp[m][k] is the number of floors you can test given
            that you have m moves and k eggs. '''
        dp = [[0] * (K + 1) for i in range(0, N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
            if dp[m][k] >= N: return m

if __name__ == "__main__":
    s = Solution()
    s.superEggDrop(3, 14)