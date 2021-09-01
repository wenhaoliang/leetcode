from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 动态规划,挺难理解的
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]  # 初始化m个长度为26的列表记录字母a-z的位置
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                # 记录字母a-z在t[i:]中的位置,如果第i个字符等于字符[a-z][j],那么j在i的位置,
                # 否则j在t[i+1:]范围,这里倒序遍历,如果j不存在那么f[i][j]的值就是m
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]

        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:  # 从t的第0个字符开始,如果f[0][j]==m,
                # 也就是说字母j不在t内,返回false,[ord(s[i]) - ord('a')]表示j,也就是在f数组中
                # 的位置
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1

        return True


if __name__ == "__main__":
    nums = 5
    A = Solution()
    print(A.isSubsequence(nums))
