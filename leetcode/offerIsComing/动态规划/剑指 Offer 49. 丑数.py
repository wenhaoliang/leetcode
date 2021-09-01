"""
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明

    1是丑数。
    n不超过1690。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chou-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        状态定义： dp[i]表示第i+1个丑数，dp[0]表示第一个丑数
        转移方程： dp[i] = min(dp[a]*2,dp[b]*3,dp[c]*5)
            1、当索引a,b,c满足以下条件时，dp[i]为三种情况最小值
                dp[a]×2 > dp[i−1] ≥ dp[a−1]×2
                dp[b]×3 > dp[i−1] ≥ dp[b−1]×3
                dp[c]×5 > dp[i−1] ≥ dp[c−1]×5
            2、每轮计算dp的值之后，需要更新a,b,c的值，使其始终满足方程条件，
                实现方法：独立判断dp[i]和dp[a]*2,dp[b]*3,dp[c]*5的大小关系，
                若相等则将对应a,b,c加1
        初始状态：dp[0] = 1
        返回值：dp[n-1]即第n个丑数
        """
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            aValue, bValue, cValue = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(aValue, bValue, cValue)
            if dp[i] == aValue:
                a += 1
            if dp[i] == bValue:
                b += 1
            if dp[i] == cValue:
                c += 1

        return dp[-1]


class Solution1:
    def nthUglyNumber(self, n: int) -> int:
        """
        状态定义： dp[i] 表示第i-1个丑数
        转移方程： 设置a,b,c三个索引来确保找到最小的丑数
                dp[i] = min(dp[a]*2, dp[b]*3, dp[c]*5)
                1、当索引a、b、c满足一下条件时，dp[i]为三种情况最小值
                    dp[a] * 2 > dp[i-1] > dp[a-1] * 2
                    dp[b] * 3 > dp[i-1] > dp[b-1] * 3
                    dp[c] * 5 > dp[i-1] > dp[c-1] * 5
                2、每轮计算dp[i]值之后，需要更新a、b、c的值，使其始终满足方程条件
                3、独立判断dp[i]到底是继承dp[a]*2, dp[b]*3, dp[c]*5种的哪一个
                    找到之后将对应a、b、c加 1
        初始状态：dp[0] = 1
        返回值：dp[-1]
        """
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            valueA, valueB, valueC = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(valueA, valueB, valueC)
            if dp[i] == valueA:
                a += 1
            if dp[i] == valueB:
                b += 1
            if dp[i] == valueC:
                c += 1

        return dp[-1]


if __name__ == "__main__":
    """
    输入: n = 10
    输出: 12
    解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
    """
    A = Solution()
    print(A.nthUglyNumber(10))
    A = Solution1()
    print(A.nthUglyNumber(10))
