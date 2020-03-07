class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = 0
        sumVal = 0

        for i in range(2, len(A)):
            if A[i - 2] - A[i - 1] == A[i - 1] - A[i]:
                dp += 1
                sumVal += dp
            else:
                dp = 0
                
        return sumVal

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    s = Solution()
    print(s.numberOfArithmeticSlices(A))