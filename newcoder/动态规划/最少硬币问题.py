from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int):
        dp = [float("inf")] * (amount + 1)
        coinDp = [float("inf")] * (amount + 1)
        coinsRes = []
        dp[0], coinDp[0] = 0, 0

        for j in range(len(coins)):
            for i in range(coins[j], amount + 1):
                coinDp[i] = coins[j]
                dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        if dp[amount] == float("inf"):
            dp[amount] = -1
        coinRes = amount
        while coinRes:
            coinsRes.append(coinDp[coinRes])
            coinRes = coinRes - coinDp[coinRes]
        return dp[amount], coinsRes


if __name__ == "__main__":
    arr, amount = [1, 2, 5], 11
    A = Solution()
    print(A.coinChange(arr, amount))
