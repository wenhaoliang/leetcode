import collections
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
        for m in range(k + 1):
            dp[0][m][1] = -prices[0]
        for i in range(1, n):
            for j in range(1, k + 1):
                a = dp[i - 1][j][0]
                b = dp[i - 1][j][1] + prices[i]
                c = dp[i - 1][j][1]
                d = dp[i - 1][j - 1][0] - prices[i]
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        if n == 0:
            return 0
        d0 = 0
        d1 = -prices[0]
        for i in range(1, n):
            d0 = max(d0, d1 + prices[i])
            d1 = max(d1, d0 - prices[i])
        return d0


class Solution2:
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0:
            return 0
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
        for m in range(k + 1):
            dp[0][m][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                # aaaaaaaaaaaaa = dp[i - 1][j][0]
                # e = dp[i - 1][j][1]
                # f = prices[i]
                # bbbbbbbbbbbbb = dp[i - 1][j][1] + prices[i]
                # ccccccccccccc = dp[i - 1][j][1]
                # h = dp[i - 1][j - 1][0]
                # qwe = prices[i]
                # ddddddddddddd = dp[i - 1][j - 1][0] - prices[i]
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][k][0]


A = Solution2()
k = 2
prices = [2, 4, 8]
print(A.maxProfit(k, prices))
