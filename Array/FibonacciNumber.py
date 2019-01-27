class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a = 0
        b = 1

        if N == 0: return a
        if N == 1: return b

        c = 0
        for i in range(N - 1):
            c = a + b
            a = b
            b = c

        return c

if __name__ == "__main__":
    N = 6
    s = Solution()
    print(s.fib(N))