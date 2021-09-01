"""
给定一个数组 prices ，其中prices[i] 是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1:
输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:
输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例3:
输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
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
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
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
            d1 = max(d1, d0 - prices[i])
        return d0


if __name__ == "__main__":
    """
    dp[i][0]表示第i天交易完成之后手里没有股票的最大利润
    dp[i][1]表示第i天交易完成之后手里有股票的最大利润
    """
    k = [7, 1, 5, 3, 6, 4]
    print('Solution', Solution().maxProfit(k))
    # print('Solution1', Solution1().maxProfit(k))

    dp = [[0 for _ in range(2)] for _ in range(7)]
    dp1 = [0 for _ in range(2)]
    print(dp)
    print(dp1)

    dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(7)]
    print(dp)

    dp = [[0, 0] for _ in range(7)]
    print(dp)

    dp = [[[0 for _ in range(2)] for _ in range(2 + 1)] for _ in range(3)]
    print(dp)

    dp = [[[0, 0] for _ in range(3)] for _ in range(3)]
    print(dp)

    k = 2
    n = 3
    dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
    print(dp)
