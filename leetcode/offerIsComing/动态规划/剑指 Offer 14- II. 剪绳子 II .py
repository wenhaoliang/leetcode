"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1]
可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
示例 1：
    输入: 2
    输出: 1
    解释: 2 = 1 + 1, 1 × 1 = 1
示例2:
    输入: 10
    输出: 36
    解释: 10 = 3 + 3 + 4, 3 ×3 ×4 = 36
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        """
        状态定义：dp[i]表示长度为i时最大值
        转移方程：
            dp[i]有两个判断：
            1、首先判断是否需要剪绳子来增加最大值，dp[i]为不剪绳子，else为剪绳子
                max(dp[i]，else)
            2、这时已经剪了一次绳子了【剪掉的绳子长度为j】，判断剩下的绳子是否需要剪短，
            即j * (i-j)表示剩下的绳子不剪了，j * dp[i-j]表示剩下的绳子也要剪掉
                max(j *(i-j), j *dp[i-j])
            dp[i] = max(dp[i], max(j *(i-j), j *dp[i-j]))
        初始值：dp[2] = 1
        返回值:dp[-1]
        """
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j * (i - j), j * dp[i - j]))

        return dp[-1] % 1000000007


if __name__ == "__main__":
    A = Solution()
    print(A.cuttingRope(10))
