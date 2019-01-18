class Solution(object):
    def coinChange(self, coinsList, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins = coinsList
        self.arrSize = len(coinsList)
        self.numCoins = 0
        self.minCoins = float("inf")
        self._recurse(0, amount)
        if self.minCoins == float("inf"): self.minCoins = -1
        return self.minCoins

    def _recurse(self, index, amount):
        if amount < 0 or index < 0 or index >= self.arrSize:
            return

        if amount == 0:
            if self.numCoins < self.minCoins:
                self.minCoins = self.numCoins
            return

        for i in range(index, self.arrSize):
            self.numCoins += 1
            self._recurse(i, amount - self.coins[i])
            self.numCoins -= 1

if __name__ == "__main__":
    s = Solution()
    coins = [2]
    amount = 3
    print(s.coinChange(coins, amount))