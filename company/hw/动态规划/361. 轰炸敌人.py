"""
给你一个二维的网格图，网格图中的每一个格子里要么是一堵墙 'W' ，要么是一个敌人 'E' ，
要么是一个空位 '0' （数字 0 ），返回你用一个炸弹最多能杀死敌人的数量。

由于墙体足够坚硬，炸弹的威慑力没有办法穿越墙体，所以炸弹只能把所在位置同一行和同一列所有没被墙挡住的敌人给炸死。

注意：你只能把炸弹放在一个空的格子里

示例:
输入: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
输出: 3
解释: 对于如下网格图，
        0 E 0 0
        E 0 W E
        0 E 0 0
在位置 (1,1) 放置炸弹可以杀死 3 个敌人。
"""
from typing import List


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        状态定义:  dp[i][j] 为到i,j能炸死的人数
        转移方程： dp[i][j] = dp[i-1][j] + dp[i][j-1]
        初始状态： dp[0] = 0, dp[-1] = 0
        返回结果：
        """
        return 1


class Solution1:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
        如果直接暴力，可以对每一个空格都计算往左往右往上往下能直接接触的敌人的数量。
        在暴力统计的基础上，重复利用已经计算的结果。

        比如，如果我已经计算好一个格子的左右能直接接触的敌人，如果它往右一步的格子也是空格，
        那么，按道理来说，这个空格的左侧敌人数量是一样的，我们得重复利用这个信息。

        定义一个 dp[][] ，其中 dp[i][j] 表示 (i,j) 格子上下左右能直接接触到的敌人的数量。
        对于一个空格 (i, j) 来说，我们需要从左到右统计才能直到它左侧有多少个敌人，从右到左统计才直到它右侧有多少个敌人。
        因此算法总共有四次非嵌套的遍历，左右、右左、上下、下上。
        最后遍历一次所有空格，找到 dp[i][j] 值最大的即可。
        算法虽然有多次遍历，但都不是嵌套的，所以时间复杂度还是 O(mn)
        """
        print('-----')
        row, col = len(grid), len(grid[0])
        ans = 0
        dp = [[0 for _ in range(col)] for _ in range(row)]
        # 遍历每一行
        for i in range(row):
            # 从左到右
            preLeft = 0
            for j in range(col):
                if grid[i][j] == 'W':
                    preLeft = 0
                elif grid[i][j] == 'E':
                    preLeft += 1
                else:
                    dp[i][j] += preLeft

                    # 从右到左
            preRight = 0
            for j in range(col - 1, -1, -1):
                if grid[i][j] == 'W':
                    preRight = 0
                elif grid[i][j] == 'E':
                    preRight += 1
                else:
                    dp[i][j] += preRight

                    # 遍历每一列
        for j in range(col):
            # 上到下
            preTop = 0
            for i in range(row):
                if grid[i][j] == 'W':
                    preTop = 0
                elif grid[i][j] == 'E':
                    preTop += 1
                else:
                    dp[i][j] += preTop

            # 下到上
            preBottom = 0
            for i in range(row - 1, -1, -1):
                if grid[i][j] == 'W':
                    preBottom = 0
                elif grid[i][j] == 'E':
                    preBottom += 1
                else:
                    dp[i][j] += preBottom
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    ans = max(ans, dp[i][j])

        return ans


if __name__ == "__main__":
    A = Solution()
    print(A.maxKilledEnemies([["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]))
    A = Solution1()
    print(A.maxKilledEnemies([["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]))
