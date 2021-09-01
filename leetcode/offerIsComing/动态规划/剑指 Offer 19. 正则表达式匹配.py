"""
请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
示例 1:
输入:
    s = "aa"
    p = "a"
    输出: false
    解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:
    输入:
    s = "aa"
    p = "a*"
    输出: true
    解释:因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例3:
输入:
    s = "ab"
    p = ".*"
    输出: true
    解释:".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:
    输入:
    s = "aab"
    p = "c*a*b"
    输出: true
    解释:因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:
    输入:
    s = "mississippi"
    p = "mis*is*p*."
    输出: false

        s可能为空，且只包含从a-z的小写字母。
        p可能为空，且只包含从a-z的小写字母以及字符.和*，无连续的 '*'。

链接：https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        状态定义： dp[i][j] 代表字符串 s 的前 i 个字符和 p 的前 j 个字符能否匹配。
        转移方程：
            需要注意，由于 dp[0][0] 代表的是空字符的状态， 因此 dp[i][j] 对应的添加字符是 s[i - 1] 和 p[j - 1] 。
            当 p[j - 1] = '*' 时， dp[i][j] 在当以下任一情况为 true 时等于 true ：
                dp[i][j - 2]： 即将字符组合 p[j - 2] * 看作出现 0 次时，能否匹配；
                dp[i - 1][j] 且 s[i - 1] = p[j - 2]: 即让字符 p[j - 2] 多出现 1 次时，能否匹配；
                dp[i - 1][j] 且 p[j - 2] = '.': 即让字符 '.' 多出现 1 次时，能否匹配；
            当 p[j - 1] != '*' 时， dp[i][j] 在当以下任一情况为 true时等于 true ：
                dp[i - 1][j - 1] 且 s[i - 1] = p[j - 1]： 即让字符 p[j - 1] 多出现一次时，能否匹配；
                dp[i - 1][j - 1] 且 p[j - 1] = '.'： 即将字符 . 看作字符 s[i - 1] 时，能否匹配；
        初始化：
        需要先初始化 dp 矩阵首行，以避免状态转移时索引越界。
            dp[0][0] = true： 代表两个空字符串能够匹配。
            dp[0][j] = dp[0][j - 2] 且 p[j - 1] = '*'： 首行 s 为空字符串，
            因此当 p 的偶数位为 * 时才能够匹配（即让 p 的奇数位出现 0 次，保持 p 是空字符串）。
            因此，循环遍历字符串 p ，步长为 2（即只看偶数位）。
        返回值： dp 矩阵右下角字符，代表字符串 s 和 p 能否匹配。
        """
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        for i in range(2, n, 2):
            dp[0][i] = dp[0][i - 2] and p[i - 1] == '*'
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True
                    elif dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True
                    elif dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True
        return dp[-1][-1]


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        """
        状态定义：dp[i][j]表示s的i-1个字符与p的j-i个字符是否能匹配
        转移方程：通过判断p[j-1]是否'*'来分为两种个情况
            当p[j-1] == '*' 时, dp[i][j] 当以下条件为真时为真：
                s: aa   p: b*.*
                dp[i][j-2]: 即设 p[j-2]这个字符出现次数为0,'a*' 或 '.*'这种情况
                dp[i-1][j] 且 p[j-2] == s[j-1]: 即要匹配的s[j-1]和前面出现过的字符相匹配
                dp[i-1][j] 且 p[j-2] == '.' : 即要匹配的s[j-1]和前面出现过的字符相匹配，只不过那个字符变为通配符'.'
            当p[j-1] != '*' 时，dp[i][j] 当以下条件为真时为真：
                s: aa   p: a*.  | s: aa   p: a*a
                dp[i-1][j-1] 且 p[j-1] == s[i-1]
                dp[i-1][j-1] 且 p[j-1] == '.'
        初始化：
            需要先初始化dp矩阵首行，以避免状态转移时索引越界
            dp[0][0] = True : 代表两个空字符串能够匹配
            dp[0][j] =  dp[0][j-2] and p[j-1] == '*' 代表p的奇数位出现0次，保持p时空字符串。
            因此，循环遍历字符串p，步长为2，即只看偶数位。
        返回值： dp 矩阵右下角字符，代表字符串 s 和 p 能否匹配。
        """
        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True
        for i in range(2, n, 2):
            dp[0][i] = dp[0][i - 2] and p[i - 1] == '*'

        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    if dp[i - 1][j] and p[j - 2] == s[i - 1]:
                        dp[i][j] = True
                    if dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True
                else:
                    if dp[i - 1][j - 1] and p[j - 1] == s[i - 1]:
                        dp[i][j] = True
                    if dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True

        return dp[-1][-1]


if __name__ == "__main__":
    A = Solution1()
    s = "aaa"
    p = "b*.*"

    print(A.isMatch(s, p))
