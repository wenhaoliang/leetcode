"""
给定一个整数数组prices ，它的第 i 个元素prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        状态定义：dp[i][j][0/1]：第i天交易j次目前手里是否有股票
        转移方程：
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        初始状态：定义第 0天已经购买了，这样才能在第一天卖出时找最大值时保持为 0
            dp[0][0->k][1] = - prices[0]
        返回值：dp[n-1][k][0]
        """
        n = len(prices)
        if n == 0:
            return 0
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]
        for m in range(k + 1):
            dp[0][m][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        状态定义：dp[i][j][0/1]: 第i天交易j次，手里是否含有股票时挣到的钱
        转移方程：
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        初始状态：
        返回结果：
        """
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(k + 1)] for _ in range(n)]

        for m in range(k + 1):
            dp[0][m][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[-1][k][0]


if __name__ == "__main__":
    # A = Solution()
    # print(A.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
    A = Solution1()
    print(A.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4]))
