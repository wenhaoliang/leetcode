"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？
示例 1：
输入：m = 2, n = 3, k = 1
输出：3
示例 2：
输入：m = 3, n = 1, k = 0
输出：1
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
        深度优先搜索： 可以理解为暴力法遍历矩阵中所有字符串可能性。DFS 通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推。
        剪枝： 在搜索中，遇到 这条路不可能和目标字符串匹配成功 的情况（例如：此矩阵元素和目标字符不同、此元素已被访问），则应立即返回，称之为 可行性剪枝 。

        对每一个字符可以向四个方向移动

        1、递归参数：当前元素的矩阵索引i,j
        2、终止条件：
            返回 0：
                1、行或列越界
                2、数位和i,j > k
                3、当前元素访问过
        3、递推工作：
            1、标记当前元素访问过为 1，
            2、向下右两个方向递推
            3、将当前元素返回为初始值
        4、回溯返回值：
            返回 1 + 右方搜索的可达解总数 + 下方搜索的可达解总数，代表从本单元格递归搜索的可达解总数。
        """

        def dfs(i, j):
            if i >= m or j >= n or byteSum(i, j) > k or dp[i][j] == 1:
                return 0
            dp[i][j] = 1
            return 1 + dfs(i + 1, j) + dfs(i, j + 1)

        def byteSum(i, j):
            res = 0
            while i != 0:
                res += i % 10
                i = i // 10
            while j != 0:
                res += j % 10
                j = j // 10
            return res

        dp = [[0 for _ in range(n)] for _ in range(m)]
        return dfs(0, 0)


class Solution1:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def dfs(i, j):
            if i >= m or j >= n or byteSum(i, j) or dp[i][j] == 1:
                return 0
            dp[i][j] = 1

            return 1 + dfs(i + 1, j) + dfs(i, j + 1)

        def byteSum(i, j):
            res = 0
            while i != 0:
                res += i % 10
                i = i // 10
            while j != 0:
                res += j % 10
                j = j // 10
            if res > k:
                return True
            else:
                return False

        dp = [[0 for _ in range(m)] for _ in range(n)]
        return dfs(0, 0)


if __name__ == "__main__":
    """
    输入：m = 2, n = 3, k = 1
    输出：3
    """
    m, n, k = 2, 3, 1
    A = Solution()
    print(A.movingCount(m, n, k))
    A = Solution1()
    print(A.movingCount(m, n, k))
