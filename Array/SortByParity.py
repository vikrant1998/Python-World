class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0; j = len(A) - 1
        while i < j:
            if A[i] % 2 != 0 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0: i += 1
            if A[j] % 2 != 0: j -= 1
        return A

if __name__ == "__main__":
    A = [0, 1, 2]
    s = Solution()
    print(s.sortArrayByParity(A))
