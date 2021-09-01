import collections
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0 for _ in range(2)] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):



            # a = dp[i - 1][0]
            # b = dp[i - 1][1] + prices[i]
            # c = dp[i - 1][1]
            # d = -prices[i]
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        d0 = 0
        d1 = -prices[0]
        for i in range(n):
            d0 = max(d0, d1 + prices[i])
            d1 = max(d1, -prices[i])
        return d0


A = Solution1()
k = [7, 1, 5, 3, 6, 4]
print(A.maxProfit(k))
