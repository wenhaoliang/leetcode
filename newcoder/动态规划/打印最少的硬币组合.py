from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i >= coins[j] and dp[i - coins[j]] != float("inf"):
                    dp[i] = min(dp[i - coins[j]] + 1, dp[i])

        if dp[amount] == float("inf"):
            dp[amount] = -1
        return dp[amount]


class Solution1:
    def coinChange(self, coins: List[int], amount: int):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for j in range(len(coins)):
            for i in range(coins[j], amount + 1):
                dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        if dp[amount] == float("inf"):
            dp[amount] = -1
        return dp[amount]


if __name__ == "__main__":
    arr, amount = [1, 2, 5], 11
    A = Solution1()
    print(A.coinChange(arr, amount))
