"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
            s - - - - - -
            - - - - - - -
            - - - - - - *
网格中的障碍物和空位置分别用 1 和 0 来表示。


示例 1：
            s - -
            - 1 -
            - - *

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：
            s 1
            - *
输入：obstacleGrid = [[0,1],[0,0]]
输出：1

链接：https://leetcode-cn.com/problems/unique-paths-ii
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        状态定义:  dp[i][j] 为到i,j位置能走的路径和
        转移方程： dp[i][j] = dp[i-1][j] + dp[i][j-1]
        初始状态： dp[0] = 0, dp[-1] = 0
        返回结果：
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if (i == 0 and j == 0) or obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


if __name__ == "__main__":
    A = Solution()
    print(A.uniquePathsWithObstacles([[1]]))
