"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
示例 1：
输入: n = 3
输出:6
示例 2：
输入: n = 9
输出:45
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
题解： https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
"""


class Solution:
    def __init__(self):
        self.res = 0

    def sumNums(self, n: int) -> int:
        """
        逻辑运算符的短路效应：
            常见的逻辑运算符有三种，即 “与 && ”，“或 ∣∣ ”，“非 ! ” ；而其有重要的短路效应，如下所示：
            若 A 为 false ，则 B 的判断不会执行（即短路），直接判定 A && B 为 false:
                if(A && B)
            若 A 为 true ，则 B 的判断不会执行（即短路），直接判定 A || B 为 true:
                if(A || B)
            本题需要实现 “当 n = 1 时终止递归” 的需求，可通过短路效应实现。
            当 n = 1 时 n > 1 不成立 ，此时 “短路” ，终止后续递归
                n > 1 && sumNums(n - 1)
        """
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res


if __name__ == "__main__":
    A = Solution()
    print(A.sumNums(3))
