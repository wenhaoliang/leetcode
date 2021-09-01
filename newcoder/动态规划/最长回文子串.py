from typing import List


# -*- coding:utf-8 -*-
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        begin = 1
        if n <= 1 or s == s[::-1]:
            return s
        dp = [[False for i in range(n)] for _ in range(n)]  # dp[i][j]表示字符串s[i:j+1]中最长回文子序列的长度
        for m in range(n):
            dp[m][m] = True
        # 填充dp数组时,需要考虑遍历顺序
        # 注意两点:
        # 1. 状态转移方程中,需要从已知状态转移到未知状态,可以画出二维dp表
        # 2. 若最终返回dp数组的值,从该值的元素索引也能看出遍历顺序

        # 遍历方式1
        for j in range(1, n):  # 右边界
            for i in range(j - 1, -1, -1):  # 左边界
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if (j - 1) - (i + 1) < 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    begin = i

        if maxLen == 0:
            return s[0]
        return s[begin:begin+maxLen]


if __name__ == "__main__":
    arr = "ac"
    A = Solution()
    print(A.longestPalindrome(arr))
