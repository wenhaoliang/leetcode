"""
数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。
请写一个函数，求任意第n位对应的数字。
示例 1：
    输入：n = 3
    输出：3
示例 2：
    输入：n = 11
    输出：0
链接：https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        return n


if __name__ == "__main__":
    A = Solution()
    print(A.findNthDigit(11))
