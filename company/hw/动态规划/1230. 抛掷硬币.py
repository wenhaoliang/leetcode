"""
有一些不规则的硬币。在这些硬币中，prob[i] 表示第 i 枚硬币正面朝上的概率。
请对每一枚硬币抛掷 一次，然后返回正面朝上的硬币数等于 target 的概率。
示例 1：
输入：prob = [0.4], target = 1
输出：0.40000

示例 2：
输入：prob = [0.5,0.5,0.5,0.5,0.5], target = 0
输出：0.03125
"""
from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        状态定义:  dp[i][j] 表示前 i 个硬币中，有 j 个硬币朝上的概率
        转移方程：
            对于前 i 个硬币的最后一枚硬币，即第 i-1 枚硬币，它有两种状态：朝上或者朝下。
            1、第 i-1 枚硬币是朝上的，那么问题就转化为前 i-1 个硬币中，有 j-1 个硬币朝上的概率。此时，dp[i][j] = dp[i-1][j-1] × prob[i-1]
            2、第 i-1 枚硬币是朝下的，那么问题就转化为：前 i-1 个硬币中，有 j 个硬币朝上的概率，此时 dp[i][j] = dp[i-1][j] × (1 - prob[i-1])
            显然，两种情况都是可能的，因此状态转移方程为：
                dp[i][j] = dp[i - 1][j - 1] * prob[i - 1] + dp[i - 1][j] * (1 - prob[i - 1])
        初始状态： dp[0][0] = 1.0
        返回结果： dp[-1][-1]
        """

        n = len(prob)
        dp = [[0.0 for _ in range(target + 1)] for _ in range(n + 1)]
        # “一个硬币都没有，一个朝上的都没” 是确定事件，因此概率为 1
        dp[0][0] = 1.0

        for i in range(1, n + 1):
            for j in range(target + 1):
                # 当前这枚是反面
                dp[i][j] += dp[i - 1][j] * (1 - prob[i - 1])
                if j > 0:
                    # 当前这枚是正面
                    dp[i][j] += dp[i - 1][j - 1] * prob[i - 1]
        print(dp)
        return dp[n][target]


class Solution1:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        """
        状态定义： dp[i][j]表示在i枚硬币中有j枚朝上的概率
        转移方程： dp[i][j]，分两种情况：
                ps:这里的prob[i]表示为当前这枚硬币的概率
                【1】.当前这枚为朝下时，需要j枚硬币为朝上：dp[i-1][j] * (1 - prob[i])
                【2】.当前这枚为朝上时，需要j-1枚硬币为朝上：dp[i-1][j-1] * prob[i]
            当j=0时：只有 【1】 这种情况，即没有一枚是正面朝上的
            当j>0时：有 【1】【2】种情况。
        初始状态：dp[0][0] = 1.0 即一枚硬币都没有，一个朝上的都没有，这个事件概率为1
        返回结果：dp[-1][-1]
        """
        n = len(prob)
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]
        dp[0][0] = 1.0
        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j] * (1 - prob[i - 1])
                if j > 0:
                    dp[i][j] += dp[i - 1][j - 1] * prob[i - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    A = Solution()
    print(A.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 1))
    print('----------')
    A = Solution1()
    print(A.probabilityOfHeads([0.5, 0.5, 0.5, 0.5, 0.5], 1))
