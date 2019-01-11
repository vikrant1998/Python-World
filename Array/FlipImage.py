class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i, innerlist in enumerate(A):
            innerlist = innerlist[::-1]
            for j, elements in enumerate(innerlist):
                if elements == 0:
                    elements = 1
                else:
                    elements = 0
                innerlist[j] = elements
            A[i] = innerlist
        return A

if __name__ == "__main__":
    s = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(s.flipAndInvertImage(A))
