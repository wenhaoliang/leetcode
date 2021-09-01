"""
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，
也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
"""


class Solution:
    def findRepeatNumber(self, nums) -> int:
        dic = [0] * len(nums)
        for i in nums:
            dic[i] += 1
            if dic[i] == 2:
                return i


class Solution1:
    def findRepeatNumber(self, nums) -> int:
        n = len(nums)
        dic = [0] * n
        for i in nums:
            dic[i] += 1
            if dic[i] == 2:
                return dic[i]


if __name__ == "__main__":
    A = Solution()
    s = [2, 3, 1, 0, 2, 5, 3]
    print(A.findRepeatNumber(s))
    A = Solution1()
    s = [2, 3, 1, 0, 2, 5, 3]
    print(A.findRepeatNumber(s))
