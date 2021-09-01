"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n级的台阶总共有多少种跳法。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：
输入：n = 2
输出：2
示例 2：
输入：n = 7
输出：21
示例 3：
输入：n = 0
输出：1
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1] % 1000000007


class Solution1:
    def numWays(self, n: int) -> int:
        """
        dp[i]表示到第i台阶有多少种跳法
        dp[1] = 1
        dp[2] = 2
        dp[i] = dp[i-1] + dp[i-2]
        """
        dp = [0] * (n + 1)

        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


if __name__ == "__main__":
    A = Solution1()
    print(A.numWays(7))
