"""
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
示例 1：
            s - - - - - -
            - - - - - - -
            - - - - - - *
输入：m = 3, n = 7
输出：28
示例 2：
输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：
输入：m = 7, n = 3
输出：28
示例 4：
输入：m = 3, n = 3
输出：6

链接：https://leetcode-cn.com/problems/unique-paths
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        状态定义:  dp[i][j] 为到i,j位置能走的路径和
        转移方程： dp[i][j] = dp[i-1][j] + dp[i][j-1]
        初始状态： dp[0] = 0, dp[-1] = 0
        返回结果：
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    A = Solution()
    print(A.uniquePaths(3, 3))


