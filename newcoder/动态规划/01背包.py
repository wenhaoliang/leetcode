#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 计算01背包问题的结果
# @param V int整型 背包的体积
# @param n int整型 物品的个数
# @param vw int整型二维数组 第一维度为n,第二维度为2的二维数组,vw[i][0],vw[i][1]分别描述i+1个物品的vi,wi,体积，重量
# @return int整型
#
# dp[i][j]表示：对于前i个物品，当前背包的容量为j时，这种情况下可以装下的最大价值是dp[i][j]。
# 如果你没有把这第i个物品装入背包，那么很显然，最大价值dp[i][j]应该等于dp[i-1][j]。你不装嘛，那就继承之前的结果。
# 如果你把这第i个物品装入了背包，那么dp[i][j]应该等于dp[i-1] [ j-vm[j-vm[i-1][0] ] + vm[i-1][1]。但还是需要和不装入进行大小比较，取价值最大的。
class Solution:
    def knapsack(self, V, n, vw):
        # write code here
        # dp[i][j] 面对第i个物品且剩余j体积的最大重量
        dp = [[0 for _ in range(V + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, V + 1):
                if j < vw[i - 1][0]:  # 放不下
                    dp[i][j] = dp[i - 1][j]
                else:
                    a = j - vw[i - 1][0]
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - vw[i - 1][0]] + vw[i - 1][1])
        print(dp)
        return dp[n][V]


class Solution1:
    def knapsack(self, V, n, vw):
        # write code here
        # dp[i][j] 面对第i个物品且剩余j体积的最大重量
        dp = [0 for _ in range(V + 1)]
        for i in range(1, n + 1):
            for j in range(V, vw[i - 1][0] - 1, -1):
                dp[j] = max(dp[j], dp[j - vw[i - 1][0]] + vw[i - 1][1])

        print(dp)
        return dp[V]


if __name__ == "__main__":
    V, n, vw = 8, 3, [[1, 3], [3, 4], [5, 5]]
    A = Solution1()
    print(A.knapsack(V, n, vw))
    A = Solution()
    print(A.knapsack(V, n, vw))
