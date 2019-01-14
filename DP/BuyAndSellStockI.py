class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        result = float("-inf")
        min_till_here = float("inf")

        for price in prices:
            profit = price - min_till_here
            if profit > result:
                result = profit

            min_till_here = min(min_till_here, price)

        if result < 0: return 0
        return result

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(prices))