class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        arrSize = len(cost)
        if len(cost) == 2:
            return min(cost[0], cost[1])

        ind = 0
        sumVal = 0

        while ind < arrSize:
            if ind < arrSize - 2 and cost[ind] + cost[ind + 2] <= cost[ind + 1]:
                sumVal += cost[ind]
                ind += 2
            elif ind < arrSize - 1:
                sumVal += cost[ind + 1]
                ind += 1
            else:
                sumVal += cost[ind]
                ind += 1
        return sumVal

if __name__ == "__main__":
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost3 = [1, 2]
    s = Solution()
    print(s.minCostClimbingStairs(cost1))