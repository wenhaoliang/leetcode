"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成两笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例1:
输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
    随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：
输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：
输入：prices = [7,6,4,3,1]
输出：0
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：
输入：prices = [1]
输出：0
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 结束时的最高利润=[天数][卖出次数][是否持有股票]
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


class Solution2:
    def maxProfit(self, prices):
        if not prices:
            return 0
        length = len(prices)
        # 结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp = [[[0, 0, 0], [0, 0, 0]] for _ in range(0, length)]
        # 第一天休息
        dp[0][0][0] = 0
        # 第一天买入
        dp[0][1][0] = -prices[0]
        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        # 第一天不可能已经卖出
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')
        for i in range(1, length):
            # 结束时的最高利润=[天数][是否持有股票][卖出次数]
            # 未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            # 未持股，卖出过1次，可能是今天卖的，可能是之前卖的
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])
            # 未持股，卖出过2次，可能是今天卖的，可能是之前卖的
            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])
            # 持股，未卖出过，可能是今天买的，可能是之前买的
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])
            # 持股，卖出过1次，可能是今天买的，可能是之前买的
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])
            # 持股，卖出过2次，不可能
            dp[i][1][2] = float('-inf')
        return max(dp[length - 1][0][1], dp[length - 1][0][2], 0)


if __name__ == "__main__":
    A = Solution()
    k = [3, 3, 5, 0, 0, 3, 1, 4]
    print(A.maxProfit(k))
