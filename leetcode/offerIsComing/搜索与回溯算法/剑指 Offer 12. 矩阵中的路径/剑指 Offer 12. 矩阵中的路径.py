"""
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
示例 1：
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        深度优先搜索： 可以理解为暴力法遍历矩阵中所有字符串可能性。DFS 通过递归，先朝一个方向搜到底，再回溯至上个节点，沿另一个方向搜索，以此类推。
        剪枝： 在搜索中，遇到 这条路不可能和目标字符串匹配成功 的情况（例如：此矩阵元素和目标字符不同、此元素已被访问），则应立即返回，称之为 可行性剪枝 。

        对每一个字符可以向四个方向移动，即向右或下移动，向左向上回溯

        1、递归参数：当前矩阵的元素i,j，当前判断的字符word[k]
        2、终止条件：
            返回false：
                1、行或列越界
                2、当前元素与word[k]不同
                3、当前元素访问过
            返回rue：
                k = len(word) - 1，即字符串全部匹配
        3、递推工作：
            1、标记当前元素访问过board[i][j] == '',代表访问过
            2、向下、右、上、 左四个方向递推，使用 或 连接，有一个为True则返回，并将结果记录至res
            3、将board[i][j]元素返回为初始值，即word[k]
        4、返回值；
            返回res
        """
        row, col = len(board), len(board[0])

        def dfs(i, j, k):
            if not 0 <= i < row or not 0 <= j < col or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp = board[i][j]
            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = temp
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True
        return False


class Solution1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        对每一个字符board[i][j]进行遍历
        递归参数：当前矩阵元素board[i][j]，接下来要匹配的word[k]
        终止条件：
            返回false：
                1、行或列越界
                2、当前元素与word[k]不相符
                3、当前元素访问过
            返回true：
                k == len(word) - 1, 即字符串匹配完毕
        递推工作：
            1、将当前元素board[i][j]标记为‘ ’，代表访问过
            2、向下右上左四个方向递推，使用 或 连接， 有一个true则返回true
            3、复原当前元素
        返回值：res
        """
        row, col = len(board), len(board[0])

        def dfs(i, j, k):
            if not 0 <= i < row or not 0 <= j < col or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            temp = board[i][j]
            board[i][j] = ' '
            res = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = temp
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i, j, 0):
                    return True

        return False


if __name__ == "__main__":
    """
    输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    输出：true
    """
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "BCCED"
    A = Solution()
    print(A.exist(board, word))
    A = Solution1()
    print(A.exist(board, word))
