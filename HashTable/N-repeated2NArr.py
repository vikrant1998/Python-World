class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        for count, num in enumerate(A):
            if count < size - 1:
                if num == A[count + 1]:
                    return num
            if count < size - 2:
                if num == A[count + 2]:
                    return num
            if count < size - 3:
                if num == A[count + 3]:
                    return num

if __name__ == "__main__":
    s = Solution()
    A = [1, 5, 2, 5, 3, 5, 4, 5]
    A = [1, 2, 3, 3]
    print(s.repeatedNTimes(A))
