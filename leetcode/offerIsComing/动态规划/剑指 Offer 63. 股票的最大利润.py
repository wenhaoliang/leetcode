"""
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
链接：https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        length = len(prices)
        dp = [0] * length
        for i in range(1, length):
            dp[i] = max(dp[i - 1], prices[i] - min(prices[0:i]))
        print(dp)
        return dp[length-1]


if __name__ == "__main__":
    """
    状态定义： 设动态规划列表 dp ，dp[i] 代表以 prices[i]为结尾的子数组的最大利润（以下简称为前i日的最大利润 ）。
    转移方程： 由于题目限定 “买卖该股票一次” ，因此前 i日最大利润 dp[i]等于
    前 i - 1日最大利润 dp[i-1]和第 i日卖出的最大利润中的最大值。
        前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格)
        dp[i] = max( dp[i - 1], prices[i] - min( prices[0:i] ) )
    初始状态： dp[0] = 0，即首日利润为 0；
    返回值： dp[n - 1]，其中n为 dp列表长度。
    """
    A = Solution()
    n = [7, 1, 5, 3, 6, 4]

    print(A.maxProfit(n))
