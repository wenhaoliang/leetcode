"""
剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：
0 翻译成 “a” ，
1 翻译成 “b”，……，
11 翻译成 “l”，……，
25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""


class Solution:
    def translateNum(self, num: int) -> int:
        """
        状态定义：dp[i]代表以Xi结尾的数字可以有的翻译种类
        转移方程：分为两种情况：判断 [10X(i-1) + Xi] 是否在 10 - 25 范围内
            1、若 X(i-1) 和 Xi 可以被翻译，即和在10-25之内。dp[i] = dp[i-1]+dp[i-2]
            2、若 X(i-1) 和 Xi 不可以被翻译，即和不在10-25之类。dp[i] = dp[i-1]
            这里举例，当i = 5 时： x1 x2 x3 x4 x5
            若x4 x5可以被翻译：
            f(5) = f(3) + f(4)
            f(3) 表示x1 x2 x3 翻译方法加上x4 x5
            f(4) 表示x1 x2 x3 x4 加上 x5
            若x4 x5 不可以被翻译：
            f(5) = f(4)
        初始状态:
            dp[0] = 1
            dp[1] = 1
            这里是因为当1，2位数字是属于10-25之内时，
            dp[2] = dp[1] + dp[0] = 2
            因为 dp[1] = 1
            所以 dp[0] = 1
        返回值:  dp[-1]
        """
        s = str(num)
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = dp[1] = 1
        for i in range(2, length + 1):
            flag = int(s[i - 2]) * 10 + int(s[i - 1])
            if 10 <= flag <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]


class Solution1:
    def translateNum(self, num: int) -> int:
        """
        状态定义：dp[i]表示第Xi]结束的数字可以被翻译的种类
        转移方程：
            判断条件时 表示第X[i-1] 和 表示第X[i] 是否可以被组合翻译，
            即10 * 表示第X[i-1] + 表示第X[i] 是否属于 [10-25] 之内
            若在则可以被组合翻译，否则不可
            当后两位可以被组合翻译时：
                dp[i] = dp[i-1] + dp[i-2]
            当后两位不可被组合翻译时
                dp[i] = dp[i-1]
        初始状态:
            当 1,2两位数字为10->25内时：
                dp[2] = dp[0] + dp[1] = 1 + 1 = 2
            所以：
                dp[0] = 1
                dp[1] = 1
        返回值: dp[-1]
        """
        s = str(num)
        print(s)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            if 10 <= int(s[i - 2]) * 10 + int(s[i - 1]) <= 25:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]

        return dp[-1]


if __name__ == "__main__":
    A = Solution()
    n = 12258
    print(A.translateNum(n))
    A = Solution1()
    n = 12258
    print(A.translateNum(n))
