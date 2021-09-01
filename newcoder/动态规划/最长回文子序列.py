from typing import List


# -*- coding:utf-8 -*-
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1 or s == s[::-1]:
            return len(s)
        dp = [[0] * n for _ in range(n)]  # dp[i][j]表示字符串s[i:j+1]中最长回文子序列的长度
        for m in range(n):
            dp[m][m] = 1

        # 填充dp数组时,需要考虑遍历顺序
        # 注意两点:
        # 1. 状态转移方程中,需要从已知状态转移到未知状态,可以画出二维dp表
        # 2. 若最终返回dp数组的值,从该值的元素索引也能看出遍历顺序

        # 遍历方式1
        for j in range(1, n):  # 右边界
            for i in range(j - 1, -1, -1):  # 左边界
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        # 遍历方式2
        # for i in range(n-2, -1, -1):  # 左边界
        #     for j in range(i+1, n):  # 右边界
        #         if s[i] == s[j]:
        #             dp[i][j] = dp[i+1][j-1] + 2
        #         else:
        #             dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        #
        return dp[0][n - 1]


class Solution1:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n <= 1 and s == s[::-1]:
            return n

        dp = [[0 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            dp[m][m] = 1

        for j in range(1, n):
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return dp[0][n - 1]


if __name__ == "__main__":
    arr = "cbbd"
    A = Solution1()
    print(A.longestPalindromeSubseq(arr))
