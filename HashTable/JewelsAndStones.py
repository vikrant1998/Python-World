class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewelSet = set()
        for jewel in J: jewelSet.add(jewel)
        num = 0

        for stone in S:
            if stone in jewelSet:
                num += 1

        return num

if __name__ == "__main__":
    s = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(s.numJewelsInStones(J, S))
