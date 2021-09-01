"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
示例 1：
输入：n = 12
输出：5
示例 2：
输入：n = 13
输出：6

链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        """
        a 为当前位数前面的数
        cur 为当前数
        base 为当前位 × 10
        b 为当前位数后面的数
        3101592
        一、   [3101] 5 [92]
            1、[0-3101] 1 [0 - 99]
            所以可能出现的个数为：
                a: 0000 -> 3101
                cur: 1
                b: 0 -> 99
            所以：
                res += (a+1) * base

        二、   [310] 1 [592]
            1、 [0-309] 1 [0 - 999]
            2、 [310]   1 [0 - 592]
            所以可能出现的个数为：
            1、
                a: 000 -> 309
                cur: 1
                b: 0 -> 99
            所以：
                res += a * base
            2、
                a: 310
                cur: 1
                b: 0 -> 592
            所以：
                res += 1 * b + 1
            res += (a * base) + b + 1

        三、   [31] 0 [1592]
            1、[0-30] 1 [0 - 9999]
            所以可能出现的个数为：
                a: 0000 -> 30
                cur: 1
                b: 00 -> 9999
            所以：
                res += a * base
            res += a * base

        """
        res = 0
        base = 1
        while base <= n:
            b = n % base
            a = n // base
            cur = a % 10
            a = a // 10
            if cur > 1:
                res += (a + 1) * base
            elif cur == 1:
                res += (a * base) + b + 1
            elif cur == 0:
                res += a * base
            base = base * 10
        return res


if __name__ == "__main__":
    A = Solution()
    print(A.countDigitOne(12))
