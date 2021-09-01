"""
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
链接：https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof
"""
from typing import List


class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        """
        n个骰子，一共有6**n种情况
        F(n,s)表示投第N个骰子时，点数和为S的次数
        dp[n][s] 表示投第N个骰子时，点数和为S的次数
        n=1, 和为s的情况有 F(n,s)=1 s=1,2,3,4,5,6
        n>1 , F(n,s) = F(n-1,s-1)+F(n-1,s-2) +F(n-1,s-3)+F(n-1,s-4)+F(n-1,s-5)+F(n-1,s-6)
        这里的s-1,s-2,s-3,s-4,s-5,s-6种的1,2,3,4,5,6表示的是当前骰子骰出的值
        可以看作是从前(n-1)个骰子投完之后的状态转移过来。
        """
        dp = [[0] * (6 * n + 1) for _ in range(n + 1)]

        for i in range(1, 7):
            dp[1][i] = 1
        for i in range(2, n + 1):
            # j为【当前骰子】 与【前面的骰子】 投出的【点数和】
            # 当两个骰子时 ， 首先【点数和】j == 2
            for j in range(i, i * 6 + 1):
                # k 为【当前骰子】 投出的点数
                # 首先为 k = 1
                for k in range(1, 7):
                    # 判断， 当j也就是【点数和】
                    # 当两个骰子时， 首先为 j为2 k为1
                    # 2 >= 1 + 1 成立， 则表示可以由这两骰子骰出2
                    # 其概率为dp[i-1][j-k] == dp[1][1] == 1
                    # 接下来 第二个骰子 要投出来2，则 k + 1 == 2 + 1 == 3
                    # j == 2 >= 3 不成立，则概率为0，也就是说第一个骰子投1，
                    # 第二个骰子投2，不可能组成【点数和】2，则不加概率
                    if j >= k + 1:
                        # dp[i-1][j-k]
                        # i-1为前面的骰子
                        # j-k： k为当前骰子投出来的点数，j为点数和，j-k表示前面的骰子所需要投出来的点数
                        dp[i][j] += dp[i - 1][j - k]
        res = []
        for i in range(n, n * 6 + 1):
            # 这里取出点数和可以为i时的次数，然后将其除以 6的n次方
            # 最后 * 1.0转化为浮点数
            res.append(dp[n][i] / 6 ** n * 1.0)
        return res


class Solution1:
    def dicesProbability(self, n: int) -> List[float]:
        """
        状态定义:dp[i][j]表示用i个骰子投出点数和为j的次数
        转移方程：
            当只有一个骰子时:
                dp[1][1] = dp[1][2] = dp[1][3]= dp[1][4]= dp[1][5]= dp[1][6] = 1
            当有两个及以上的骰子时：
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j-2] + dp[i-1][j-3] + dp[i-1][j-4] + dp[i-1][j-5] + dp[i-1][j-6]
                i-1 表示前面的骰子 | j-1,j-2,j-3,j-4,j-5,j-6种的1,2,3,4,5,6表示的是当前骰子骰出的值
                dp[i-1][j-1]表示 j-1表示从点数和j种去掉当前骰子投出的1，剩下的为之前的骰子投出的值
        初始状态；dp[1][1] = dp[1][2] = dp[1][3] = dp[1][4] = dp[1][5] = dp[1][6] =  1
        返回结果：dp[-1][-1]
        """

        dp = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]

        for i in range(1, 7):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for k in range(1, 7):
                    if j >= k + 1:
                        dp[i][j] += dp[i - 1][j - k]

        res = []
        for i in range(n, n * 6 + 1):
            res.append(dp[-1][i] / 6 ** n * 1.0)
        return res


if __name__ == "__main__":
    """
    输入: n = 10
    输出: 12
    解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
    """
A = Solution()
print(A.dicesProbability(2))
A = Solution1()
print(A.dicesProbability(2))
