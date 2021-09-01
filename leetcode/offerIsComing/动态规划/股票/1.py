"""
给定一个数组 prices ，它的第i 个元素prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
"""

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
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        return dp[n - 1][0]


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
        dp = [0] * length
        for i in range(1, length):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[0:i]))
        return dp[length - 1]


class Solution2:
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


k = [7, 1, 5, 3, 6, 4]
print('Solution', Solution().maxProfit(k))
print('Solution1', Solution1().maxProfit(k))
print('Solution2', Solution2().maxProfit(k))
