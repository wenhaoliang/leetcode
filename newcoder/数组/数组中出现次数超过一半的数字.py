# -*- coding:utf-8 -*-
"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。1<=数组长度<=50000
示例1  输入[1,2,3,2,2,2,5,4,2] 输出  2
示例2  输入[3,3,3,3,2,2,2]     输出  3
示例3  输入[1]                 输出  1
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        n = len(numbers)
        if n == 1:
            return numbers
        target = n // 2 + 1
        numSet = {}
        for i in numbers:
            if i not in numSet:
                numSet[i] = 1
            else:
                numSet[i] += 1
                if numSet[i] == target:
                    return i
        return 0


class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        n = len(numbers)
        numSet = {}
        target = n // 2 + 1
        for i in numbers:
            if i not in numSet:
                numSet[i] = 1
            else:
                numSet[i] += 1
                if numSet[i] == target:
                    return i
        return None


if __name__ == "__main__":
    n = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    A = Solution()
    print(A.MoreThanHalfNum_Solution(n))
    A = Solution1()
    print(A.MoreThanHalfNum_Solution(n))
