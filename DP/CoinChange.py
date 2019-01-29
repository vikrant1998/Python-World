''' Recursion Timeout '''
'''
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
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins))]

        if amount == 0: return 0

        i = 0
        j = 0

        while i < len(dp):
            j = 0
            while j < len(dp[0]):

                # Nothing on top.
                if i - 1 < 0:
                    if j % coins[i] == 0:
                        dp[i][j] = j / coins[i]

                # Stuff on top.
                if i - 1 >= 0:
                    if j < coins[i]:
                        dp[i][j] = dp[i-1][j]
                    elif dp[i-1][j] == 0 and dp[i][j-coins[i]] == 0:
                        if j % coins[i] == 0:
                            dp[i][j] = j / coins[i]
                    elif dp[i][j-coins[i]] == 0:
                        dp[i][j] = dp[i-1][j]
                        if j % coins[i] == 0:
                            dp[i][j] = min(dp[i][j], j / coins[i])
                    elif dp[i-1][j] == 0:
                        dp[i][j] = 1 + dp[i][j-coins[i]]
                        if j % coins[i] == 0:
                            dp[i][j] = min(dp[i][j], j / coins[i])
                    else:
                        dp[i][j] = min(dp[i-1][j], 1 + dp[i][j-coins[i]])
                        if j % coins[i] == 0:
                            dp[i][j] = min(dp[i][j], j / coins[i])

                j += 1
            i += 1

        #print(dp)
        if dp[-1][-1] == 0: return -1
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    coins = [186,419,83,408]
    #coins = [1, 2]
    amount = 6249
    #amount = 2
    print(s.coinChange(coins, amount))