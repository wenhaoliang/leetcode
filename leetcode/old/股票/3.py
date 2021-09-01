import collections
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        # dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        # dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        for i in range(1, n):
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])

        return dp[n - 1][2][0]


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        d0 = 0
        d1 = -prices[0]
        for i in range(1, n):
            d0 = max(d0, d1 + prices[i])
            d1 = max(d1, d0 - prices[i])
        return d0


A = Solution()
k = [3, 3, 5, 0, 0, 3, 1, 4]
print(A.maxProfit(k))
