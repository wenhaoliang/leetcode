"""
实现pow(x,n)，即计算 x 的 n 次幂函数（即，xn）。不得使用库函数，同时不需要考虑大数问题。
示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000
示例 2：
输入：x = 2.10000, n = 3
输出：9.26100
示例 3：
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
链接：https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1 / x, -n
        while n != 0:
            if n % 2 == 1:
                res = res * x
            x = x * x
            n = n // 2
        return res


if __name__ == "__main__":
    """
    输入：x = 2.00000, n = 10
    输出：1024.00000
    """

    A = Solution()
    print(A.myPow(2.00000, 10))
